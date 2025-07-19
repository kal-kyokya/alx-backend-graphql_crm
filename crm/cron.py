from datetime import datetime
import requests
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport
import json


def update_low_stock():
    query = """
    mutation {
      updateLowStockProducts {
        output {
          name
          stock
        }
        success
      }
    }
    """

    try:
        res = requests.post(
            "http://localhost:8000/graphql",
            json={"query": query},
            timeout=5
        )

        log_path = "/tmp/low_stock_updates_log.txt"
        with open(log_path, "a") as log:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            if res.ok:
                data = res.json().get("data", {}).get("updateLowStockProducts", {})
                products = data.get("output", [])
                success = data.get("success", "")

                log.write(f"{timestamp} - {success}\n")
                for product in products:
                    log.write(f"\tProduct: {product['name']} | New Stock: {product['stock']}\n")
            else:
                log.write(f"{timestamp} - Failed to execute mutation: {res.status_code}\n")
    except Exception as e:
        with open("/tmp/low_stock_updates_log.txt", "a") as log:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log.write(f"{timestamp} - Exception: {str(e)}\n")


def log_crm_heartbeat():
    timestamp = datetime.now().strftime("%d/%m?%Y-%H:%M:%S")
    status = "CRM is alive"

    try:
        # Optional: Ping GraphQL hello field
        res = requests.post(
            "http://localhost:8000/graphql",
            json={"query": "{ hello }"},
            timeout=3
        )
        if res.ok and res.json().get("data", {}).get("hello") == "Hello, GraphQL!":
            status = "CRM is alive and GraphQL responsive"
        else:
            status = "CRM is alive but GraphQL failed"

    except Exception as e:
        status = f"CRM alive but GraphQL error: {str(e)}"

    with open("/tmp/crm_heartbeat_log.txt", "a") as f:
        f.write(f"{timestamp} {status}\n")
