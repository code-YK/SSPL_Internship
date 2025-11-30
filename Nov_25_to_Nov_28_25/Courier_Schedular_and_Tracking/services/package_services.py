from config import setup_logger
from models import Depot, Driver, Package
from sqlalchemy.orm import Session
from datetime import datetime
from schema import PackageCreate, PackageRead

logger = setup_logger(__name__)

class PackageService:

    @staticmethod
    def create_package(db: Session, package_create: PackageCreate) -> PackageRead:
        """Create a new package in the database."""
        new_package = Package(
            recipient_name=package_create.recipent_name,
            address=package_create.address,
            depot_id=package_create.depot_id,
            status=package_create.status,
            created_at=package_create.created_at,
            updated_at=package_create.updated_at,
            tracking_number=package_create.tracking_number
        )
        try:
            if db.query(Depot).filter(Depot.id == package_create.depot_id).first() is None:
                raise ValueError(f"Depot with ID {package_create.depot_id} does not exist.")
            db.add(new_package)
            db.commit()
            db.refresh(new_package)
            logger.info(f"Package with tracking number '{package_create.tracking_number}' created successfully.")
        except Exception as e:
            logger.error(f"Error creating package with tracking number '{package_create.tracking_number}': {e}")
            db.rollback()
            raise
        return new_package
    
    @staticmethod
    def get_package_by_id(db: Session, package_id: int) -> PackageRead:
        """Retrieve a package by its ID."""
        package = db.query(Package).filter(Package.id == package_id).first()
        if package:
            logger.info(f"Package with ID {package_id} retrieved successfully.")
        else:
            logger.warning(f"Package with ID {package_id} not found.")
        return package
    
    @staticmethod
    def list_packages(db: Session) -> list[PackageRead]:
        """List all packages."""
        packages = db.query(Package).all()
        logger.info(f"Retrieved {len(packages)} packages.")
        return packages
    
    @staticmethod
    def update_package(db: Session, 
                       package_id: int, 
                       recipient_name: str = None, 
                       address: str = None, 
                       depot_id: int = None, 
                       status = None, 
                       tracking_number: str = None
                     ) -> PackageRead:
        """Update package details."""
        package = PackageService.get_package_by_id(db, package_id)
        if not package:
            logger.error(f"Package with ID {package_id} not found for update.")
            return None
        try:
            if recipient_name is not None:
                package.recipient_name = recipient_name
            if address is not None:
                package.address = address
            if depot_id is not None:
                if db.query(Depot).filter(Depot.id == depot_id).first() is None:
                    raise ValueError(f"Depot with ID {depot_id} does not exist.")
                package.depot_id = depot_id
            if status is not None:
                package.status = status
            if tracking_number is not None:
                package.tracking_number = tracking_number
            package.updated_at = datetime.utcnow()
            db.commit()
            db.refresh(package)
            logger.info(f"Package with ID {package_id} updated successfully.")
        except Exception as e:
            logger.error(f"Error updating package with ID {package_id}: {e}")
            db.rollback()
            raise
        return package
    
    @staticmethod
    def delete_package(db: Session, package_id: int) -> bool:
        """Delete a package by its ID."""
        package = PackageService.get_package_by_id(db, package_id)
        if not package:
            logger.error(f"Package with ID {package_id} not found for deletion.")
            return False
        try:
            db.delete(package)
            db.commit()
            logger.info(f"Package with ID {package_id} deleted successfully.")
            return True
        except Exception as e:
            logger.error(f"Error deleting package with ID {package_id}: {e}")
            db.rollback()
            raise
        return False
    