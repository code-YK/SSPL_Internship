from config import setup_logger
from models import Depot, Driver
from sqlalchemy.orm import Session
from schema import DriverCreate, DriverRead

logger = setup_logger(__name__)

class DriverService:

    @staticmethod
    def create_driver(db: Session, driver_create: DriverCreate) -> DriverRead:
        """Create a new driver in the database."""
        new_driver = Driver(
            name=driver_create.name,
            depot_id=driver_create.depot_id,
            phone=driver_create.phone,
            is_active=driver_create.is_active
        )
        try:
            if db.query(Depot).filter(Depot.id == driver_create.depot_id).first() is None:
                raise ValueError(f"Depot with ID {driver_create.depot_id} does not exist.")
            db.add(new_driver)
            db.commit()
            db.refresh(new_driver)
            logger.info(f"Driver '{driver_create.name}' created successfully.")
        except Exception as e:
            logger.error(f"Error creating driver '{driver_create.name}': {e}")
            db.rollback()
            raise
        return new_driver
    
    @staticmethod
    def get_driver_by_id(db: Session, driver_id: int) -> DriverRead:
        """Retrieve a driver by its ID."""
        driver = db.query(Driver).filter(Driver.id == driver_id).first()
        if driver:
            logger.info(f"Driver with ID {driver_id} retrieved successfully.")
        else:
            logger.warning(f"Driver with ID {driver_id} not found.")
        return driver
    
    @staticmethod
    def list_active_drivers(db: Session) -> list[DriverRead]:
        """List all active drivers."""
        drivers = db.query(Driver).filter(Driver.is_active == True).all()
        logger.info(f"Retrieved {len(drivers)} active drivers.")
        return drivers
    
    @staticmethod
    def update_driver(db: Session, 
                      driver_id: int, 
                      name: str = None, 
                      depot_id: int = None, 
                      phone: str = None, 
                      is_active: bool = None
                    ) -> DriverRead:
        """Update driver details."""
        driver = DriverService.get_driver_by_id(db, driver_id)
        if not driver:
            logger.error(f"Driver with ID {driver_id} not found for update.")
            return None
        try:
            if depot_id is not None:
                if db.query(Depot).filter(Depot.id == depot_id).first() is None:
                    raise ValueError(f"Depot with ID {depot_id} does not exist.")
                driver.depot_id = depot_id
            if name is not None:
                driver.name = name
            if phone is not None:
                driver.phone = phone
            if is_active is not None:
                driver.is_active = is_active
            db.commit()
            db.refresh(driver)
            logger.info(f"Driver with ID {driver_id} updated successfully.")
        except Exception as e:
            logger.error(f"Error updating driver with ID {driver_id}: {e}")
            db.rollback()
            raise
        return driver
    
    @staticmethod
    def delete_driver(db: Session, driver_id: int) -> bool:
        """Delete a driver by its ID."""
        driver = DriverService.get_driver_by_id(db, driver_id)
        if not driver:
            logger.error(f"Driver with ID {driver_id} not found for deletion.")
            return False
        try:
            db.delete(driver)
            db.commit()
            logger.info(f"Driver with ID {driver_id} deleted successfully.")
            return True
        except Exception as e:
            logger.error(f"Error deleting driver with ID {driver_id}: {e}")
            db.rollback()
            raise
        return False
