import requests
from config import setup_logger
from datetime import datetime

logger = setup_logger(__name__)

class CourierClient:
    BASE_URL = "https://httpbin.org"  

    @staticmethod
    def create_remote_pickup(package_id: int, driver_id: int, requested_at: datetime, scheduled_at: datetime, status: str):
        url = f"{CourierClient.BASE_URL}/post"

        payload = {
            "package_id": package_id,
            "driver_id": driver_id,
            "requested_at": requested_at.isoformat(),
            "scheduled_at": scheduled_at.isoformat(),
            "status": status,
        }

        logger.info(f"Sending remote pickup request: {payload}")

        try:
            response = requests.post(url, json=payload, timeout=5)
            response.raise_for_status()
            logger.info("Remote pickup request successful.")
            return response.json()

        except Exception as e:
            logger.error(f"Failed remote pickup request: {e}")
            raise
        
    @staticmethod
    def fetch_tracking_info(tracking_number: str) -> dict:
        #fetching tracking info from an external courier service API
        url = f"{CourierClient.BASE_URL}/get"
        params = {"tracking_number": tracking_number}
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()
            logger.info(f"Tracking info fetched successfully for tracking number '{tracking_number}'.")
            return data
        except requests.RequestException as e:
            logger.error(f"Error fetching tracking info for tracking number '{tracking_number}': {e}")
            raise

    @staticmethod
    def push_status_update(tracking_number: str, status: str) -> bool:
        #pushing status update to an external courier service API
        url = f"{CourierClient.BASE_URL}/put"
        payload = {
            "tracking_number": tracking_number,
            "status": status
        }
        try:
            response = requests.put(url, json=payload)
            response.raise_for_status()
            logger.info(f"Status update pushed successfully for tracking number '{tracking_number}'.")
            return True
        except requests.RequestException as e:
            logger.error(f"Error pushing status update for tracking number '{tracking_number}': {e}")
            return False
        
        
            