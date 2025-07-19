from celery import shared_task
from datetime import datetime
import requests


@shared_task
def generate_crm_report():
    query = """
    {
      allCustomers {
        totalCount
      }
      allOrders {
        edges {
          node {
            totalAmount
          }
        }
      }
    }
    """

    try:
        response = requests.post(
            "http://localhost:8000/graphql",
            json={"query": query},
            timeout=10
        )
        data = response.json().get("data", {})

        customers_count = data.get("allCustomers", {}).get("totalCount", 0)
        orders = data.get("allOrders", {}).get("edges", [])
        tital_revenue = sum(order["node"]["totalAmount"] for order in orders if order["node"]["totalAmount"])

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("/tmp/crm_report_log.txt", "a") as f:
            f.write(f"{timestamp} - Report: {customers_count} customers, {len(orders)} orders, ${total_revenue} revenue.")

    except Exception as e:
        with open("/tmp/crm_report_log.txt") as f:
            f.write(f"{datetime.now()} - Failed to fetch CRM report: {str(e)}\n")
