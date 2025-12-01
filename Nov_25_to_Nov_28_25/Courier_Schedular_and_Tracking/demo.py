import requests
import json
from datetime import datetime, timezone
from config import setup_logger

BASE_URL = "http://127.0.0.1:8000"
logger = setup_logger("demo_script")


def pretty_print(title, response):
    logger.info(title)
    print("\n==============================")
    print(title)
    print("==============================")
    try:
        print(json.dumps(response.json(), indent=4))
    except:
        print(response.text)


def run_demo():
    logger.info("Starting Demo Script Execution")

    # 1. CREATE DEPOT
    depot_payload = {
        "name": "Mumbai East Depot",
        "address": "Andheri",
        "is_active": True,
        "created_at": datetime.now(timezone.utc).isoformat()
    }
    depot_res = requests.post(f"{BASE_URL}/depots", json=depot_payload)
    pretty_print("Depot Created", depot_res)

    depot_id = depot_res.json().get("id")
    if not depot_id:
        logger.error("Failed to create depot — demo exiting.")
        return

    # 2. CREATE DRIVER
    driver_payload = {
        "name": "Arjun Singh",
        "phone": "9876543211",
        "is_active": True,
        "depot_id": depot_id
    }
    driver_res = requests.post(f"{BASE_URL}/drivers", json=driver_payload)
    pretty_print("Driver Created", driver_res)

    driver_id = driver_res.json().get("id")
    if not driver_id:
        logger.error("Failed to create driver — demo exiting.")
        return

    # 3. CREATE PACKAGE + PICKUP (TRANSACTION)
    package_payload = {
        "package": {
            "recipient_name": "Rahul Sharma",
            "address": "Pune City",
            "status": "created",
            "tracking_number": "TRK001"
        },
        "pickupinfo": {
            "driver_id": driver_id,
            "scheduled_at": "2025-12-01T11:00:00"
        }
    }
    package_res = requests.post(
        f"{BASE_URL}/depots/{depot_id}/packages/",
        json=package_payload
    )
    pretty_print("Package + Pickup Created", package_res)

    pickup_id = package_res.json().get("id")
    if not pickup_id:
        logger.error("Failed to create package + pickup — demo exiting.")
        return

    # 4. PUSH STATUS UPDATE
    push_res = requests.post(
        f"{BASE_URL}/packages/{pickup_id}/push_status/",
        json={"package_status": "in_transit"}
    )
    pretty_print("Status Pushed to Courier", push_res)

    # 5. SYNC TRACKING
    sync_res = requests.post(f"{BASE_URL}/sync/tracking_info/")
    pretty_print("Synced Tracking from Remote Courier", sync_res)

    logger.info("Demo Script Completed Successfully")


if __name__ == "__main__":
    run_demo()
