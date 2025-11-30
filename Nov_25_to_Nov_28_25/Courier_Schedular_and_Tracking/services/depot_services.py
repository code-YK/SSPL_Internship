from config import setup_logger
from models import Depot
from schema import DepotCreate, DepotRead
from sqlalchemy.orm import Session
from datetime import datetime

logger = setup_logger(__name__)

class DepotService:

    @staticmethod
    def create_depot(db: Session, depot_create: DepotCreate) -> Depot:
        """Create a new depot in the database."""
        new_depot = Depot(
            name=depot_create.name,
            address=depot_create.address,
            is_active=depot_create.is_active,
            created_at=datetime.utcnow()
        )
        try:
            db.add(new_depot)
            db.commit()
            db.refresh(new_depot)
            logger.info(f"Depot '{new_depot.name}' created successfully.")
        except Exception as e:
            logger.error(f"Error creating depot '{new_depot.name}': {e}")
            db.rollback()
            raise
        return new_depot

    @staticmethod
    def get_depot_by_id(db: Session, depot_id: int) -> DepotRead:
        """Retrieve a depot by its ID."""
        depot = db.query(Depot).filter(Depot.id == depot_id).first()
        if depot:
            logger.info(f"Depot with ID {depot_id} retrieved successfully.")
        else:
            logger.warning(f"Depot with ID {depot_id} not found.")
        return depot

    @staticmethod
    def list_active_depots(db: Session) -> list[DepotRead]:
        """List all active depots."""
        depots = db.query(Depot).filter(Depot.is_active == True).all()
        logger.info(f"Retrieved {len(depots)} active depots.")
        return depots

    @staticmethod
    def update_depot(db: Session, depot_id: int, name: str = None, address: str = None, is_active: bool = None) -> Depot:
        """Update depot details."""
        depot = DepotService.get_depot_by_id(db, depot_id)
        if not depot:
            logger.error(f"Depot with ID {depot_id} not found for update.")
            return None
        try:
            if name is not None:
                depot.name = name
            if address is not None:
                depot.address = address
            if is_active is not None:
                depot.is_active = is_active
            db.commit()
            db.refresh(depot)
            logger.info(f"Depot with ID {depot_id} updated successfully.")
        except Exception as e:
            logger.error(f"Error updating depot with ID {depot_id}: {e}")
            db.rollback()
            raise
        return depot
    
    @staticmethod
    def delete_depot(db: Session, depot_id: int) -> bool:
        """Delete a depot by its ID."""
        depot = DepotService.get_depot_by_id(db, depot_id)
        if not depot:
            logger.error(f"Depot with ID {depot_id} not found for deletion.")
            return False
        try:
            db.delete(depot)
            db.commit()
            logger.info(f"Depot with ID {depot_id} deleted successfully.")
            return True
        except Exception as e:
            logger.error(f"Error deleting depot with ID {depot_id}: {e}")
            db.rollback()
            raise
        return False
    
