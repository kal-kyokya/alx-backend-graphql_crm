from datetime import datetime
import requests
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

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
