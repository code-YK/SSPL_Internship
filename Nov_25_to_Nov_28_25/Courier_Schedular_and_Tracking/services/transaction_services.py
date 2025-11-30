from sqlalchemy import Session
from models import Driver, Package, PickupRequest
from schema import PackageCreate
from datetime import datetime
from config import setup_logger

logger = setup_logger(__name__)

class TransactionService:

    @staticmethod
    def create_transaction(db: Session, package_create: PackageCreate, driver_id: int, scheduled_at) -> PickupRequest:
        """Create a package and associated pickup request transactionally."""
        try:
            # create a new package
            new_package = Package(
                recipient_name=package_create.recipient_name,
                address=package_create.address,
                depot_id=package_create.depot_id,
                status=package_create.status,
                created_at=datetime.utcnow(),
                updated_at=datetime.utcnow(),
                tracking_number=package_create.tracking_number
            )
            db.add(new_package)
            db.flush()  # flush to get new_package.id

            #create a new pickup request (not all data)
            new_pickup_request = PickupRequest(
                package_id=new_package.id,
                requested_at=datetime.utcnow(),
                status="pending",
            )

            # assign driver and scheduled time
            if db.query(Driver).filter(Driver.id == driver_id).first() is None:
                raise ValueError(f"Driver with ID {driver_id} does not exist.")
            new_pickup_request.driver_id = driver_id
            new_pickup_request.scheduled_at = scheduled_at
            
            db.add(new_pickup_request)
            db.commit()
            db.refresh(new_package)
            db.refresh(new_pickup_request)
            logger.info(f"Transaction completed: Package '{new_package.tracking_number}' and Pickup Request created successfully.")
            return new_pickup_request
        except Exception as e:
            logger.error(f"Transaction failed: {e}")
            db.rollback()
            raise