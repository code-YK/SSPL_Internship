from config import setup_logger
from models import Driver, Package, PickupRequest
from sqlalchemy.orm import Session
from datetime import date
from schema import PickupRequestCreate, PickupRequestRead

logger = setup_logger(__name__)

class PickupRequestService:

    @staticmethod
    def create_pickup_request(db: Session, pickup_request_create: PickupRequestCreate) -> PickupRequestRead:
        """Create a new pickup request in the database."""
        new_pickup_request = PickupRequest(
            package_id=pickup_request_create.package_id,
            driver_id=pickup_request_create.driver_id,
            requested_at=pickup_request_create.requested_at,
            scheduled_at=pickup_request_create.scheduled_at,
            status=pickup_request_create.status
        )
        try:
            if db.query(Package).filter(Package.id == pickup_request_create.package_id).first() is None:
                raise ValueError(f"Package with ID {pickup_request_create.package_id} does not exist.")
            if db.query(Driver).filter(Driver.id == pickup_request_create.driver_id).first() is None:
                raise ValueError(f"Driver with ID {pickup_request_create.driver_id} does not exist.")
            db.add(new_pickup_request)
            db.commit()
            db.refresh(new_pickup_request)
            logger.info(f"Pickup request for package ID '{pickup_request_create.package_id}' created successfully.")
        except Exception as e:
            logger.error(f"Error creating pickup request for package ID '{pickup_request_create.package_id}': {e}")
            db.rollback()
            raise
        return new_pickup_request
    
    @staticmethod
    def get_pickup_request_by_id(db: Session, pickup_request_id: int) -> PickupRequestRead:
        """Retrieve a pickup request by its ID."""
        pickup_request = db.query(PickupRequest).filter(PickupRequest.id == pickup_request_id).first()
        if pickup_request:
            logger.info(f"Pickup request with ID {pickup_request_id} retrieved successfully.")
        else:
            logger.warning(f"Pickup request with ID {pickup_request_id} not found.")
        return pickup_request

    @staticmethod
    def list_pickup_requests(db: Session) -> list[PickupRequestRead]:
        """List all pickup requests."""
        pickup_requests = db.query(PickupRequest).all()
        logger.info(f"Retrieved {len(pickup_requests)} pickup requests.")
        return pickup_requests
    
    @staticmethod
    def update_pickup_request(db: Session, 
                              pickup_request_id: int, 
                              driver_id: int = None, 
                              scheduled_at = None, 
                              status = None
                            ) -> PickupRequestRead:
        """Update pickup request details."""
        pickup_request = PickupRequestService.get_pickup_request_by_id(db, pickup_request_id)
        if not pickup_request:
            logger.error(f"Pickup request with ID {pickup_request_id} not found for update.")
            return None
        try:
            if driver_id is not None:
                if db.query(Driver).filter(Driver.id == driver_id).first() is None:
                    raise ValueError(f"Driver with ID {driver_id} does not exist.")
                pickup_request.driver_id = driver_id
            if scheduled_at is not None:
                pickup_request.scheduled_at = scheduled_at
            if status is not None:
                pickup_request.status = status
            db.commit()
            db.refresh(pickup_request)
            logger.info(f"Pickup request with ID {pickup_request_id} updated successfully.")
        except Exception as e:
            logger.error(f"Error updating pickup request with ID {pickup_request_id}: {e}")
            db.rollback()
            raise
        return pickup_request
    
    @staticmethod   
    def delete_pickup_request(db: Session, pickup_request_id: int) -> bool:
        """Delete a pickup request by its ID."""
        pickup_request = PickupRequestService.get_pickup_request_by_id(db, pickup_request_id)
        if not pickup_request:
            logger.error(f"Pickup request with ID {pickup_request_id} not found for deletion.")
            return False
        try:
            db.delete(pickup_request)
            db.commit()
            logger.info(f"Pickup request with ID {pickup_request_id} deleted successfully.")
            return True
        except Exception as e:
            logger.error(f"Error deleting pickup request with ID {pickup_request_id}: {e}")
            db.rollback()
            raise
        return False
    
    