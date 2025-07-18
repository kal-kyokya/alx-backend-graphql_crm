#!/usr/bin/env python3
from gql import gql, Client
from gql.transport.requests import RequestHTTPTransport
from datetime import datetime, timedelta
import os

# Define GraphQL endpoint
transport = RequestHTTPTransport(
    url='http://localhost:8000/graphql',
    verify=False,
    retries=3,
)

client = Client(transport=transport, fetch_schema_from_transport=False)

# Calculate date range (last 7 days)
today = datetime.today()
seven_days_ago = today - timedelta(days=7)
today_str = today.strftime('%Y-%m-%d')
seven_days_ago_str = seven_days_ago.strftime('%Y-%m-%d')

# GraphQL query to fetch recent orders
query = gql(f"""
query {{
  allOrders(orderDate_Gte: "{seven_days_ago_str}", orderDate_Lte: "{today_str}") {{
    edges {{
      node {{
        id
        orderDate
        customer {{
          email
        }}
      }}
    }}
  }}
}}
""")

try:
    result = client.execute(query)
    log_lines = []
    for edge in result['allOrders']['edges']:
        order = edge['node']
        log_line = f"{datetime.now().isoformat()} - Order ID: {order['id']}, Customer Email: {order['customer']['email']}"
        log_lines.append(log_line)

    log_path = '/tmp/order_reminders_log.txt'
    with open(log_path, 'a') as log_file:
        for line in log_lines:
            log_file.write(line + '\n')

    print("Order reminders processed!")

except Exception as e:
    print("Error:", e)
