from config import setup_logger
from models import TrackingEvent, Package
from sqlalchemy.orm import Session
from datetime import date
from schema import TrackingEventCreate, TrackingEventRead

logger = setup_logger(__name__)

class TrackingEventService:
    @staticmethod
    def create_tracking_event(db: Session, tracking_event_create: TrackingEventCreate) -> TrackingEventRead:
        """Create a new tracking event in the database."""
        new_tracking_event = TrackingEvent(
            package_id=tracking_event_create.package_id,
            status=tracking_event_create.status,
            location=tracking_event_create.location,
            timestamp=tracking_event_create.timestamp
        )
        try:
            if db.query(Package).filter(Package.id == tracking_event_create.package_id).first() is None:
                raise ValueError(f"Package with ID {tracking_event_create.package_id} does not exist.")
            db.add(new_tracking_event)
            db.commit()
            db.refresh(new_tracking_event)
            logger.info(f"Tracking event for package ID '{tracking_event_create.package_id}' created successfully.")
        except Exception as e:
            logger.error(f"Error creating tracking event for package ID '{tracking_event_create.package_id}': {e}")
            db.rollback()
            raise
        return new_tracking_event
    
    @staticmethod
    def get_tracking_event_by_id(db: Session, tracking_event_id: int) -> TrackingEventRead:
        """Retrieve a tracking event by its ID."""
        tracking_event = db.query(TrackingEvent).filter(TrackingEvent.id == tracking_event_id).first()
        if tracking_event:
            logger.info(f"Tracking event with ID {tracking_event_id} retrieved successfully.")
        else:
            logger.warning(f"Tracking event with ID {tracking_event_id} not found.")
        return tracking_event
    
    @staticmethod
    def list_tracking_events(db: Session) -> list[TrackingEventRead]:
        """List all tracking events."""
        tracking_events = db.query(TrackingEvent).all()
        logger.info(f"Retrieved {len(tracking_events)} tracking events.")
        return tracking_events
    
    @staticmethod
    def update_tracking_event(db: Session, 
                              tracking_event_id: int, 
                              status: str = None, 
                              location: str = None, 
                              timestamp = None
                            ) -> TrackingEventRead:
        """Update tracking event details."""
        tracking_event = TrackingEventService.get_tracking_event_by_id(db, tracking_event_id)
        if not tracking_event:
            logger.error(f"Tracking event with ID {tracking_event_id} not found for update.")
            return None
        try:
            if status is not None:
                tracking_event.status = status
            if location is not None:
                tracking_event.location = location
            if timestamp is not None:
                tracking_event.timestamp = timestamp
            db.commit()
            db.refresh(tracking_event)
            logger.info(f"Tracking event with ID {tracking_event_id} updated successfully.")
        except Exception as e:
            logger.error(f"Error updating tracking event with ID {tracking_event_id}: {e}")
            db.rollback()
            raise
        return tracking_event
    
    @staticmethod
    def delete_tracking_event(db: Session, tracking_event_id: int) -> bool:
        """Delete a tracking event by its ID."""
        tracking_event = TrackingEventService.get_tracking_event_by_id(db, tracking_event_id)
        if not tracking_event:
            logger.error(f"Tracking event with ID {tracking_event_id} not found for deletion.")
            return False
        try:
            db.delete(tracking_event)
            db.commit()
            logger.info(f"Tracking event with ID {tracking_event_id} deleted successfully.")
            return True
        except Exception as e:
            logger.error(f"Error deleting tracking event with ID {tracking_event_id}: {e}")
            db.rollback()
            raise
        return False
    
    @staticmethod
    def get_events_by_tracking_num(db: Session, tracking_number: str) -> list[TrackingEventRead]:
        """Retrieve all tracking events for a given package tracking number."""
        package = db.query(Package).filter(Package.tracking_number == tracking_number).first()
        if not package:
            logger.warning(f"Package with tracking number {tracking_number} not found.")
            return []
        tracking_events = sorted(db.query(TrackingEvent).filter(TrackingEvent.package_id == package.id).all(), key=lambda x: x.timestamp)
        logger.info(f"Retrieved {len(tracking_events)} tracking events for package with tracking number {tracking_number}.")
        return tracking_events
    