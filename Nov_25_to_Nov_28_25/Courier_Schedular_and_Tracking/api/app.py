from fastapi import FastAPI, Depends
from config import get_db, setup_logger
from sqlalchemy.orm import Session
from services import DepotService, TransactionService, TrackingEventService
from integrations import CourierClient
from schema import DepotCreate, PackagePickupCreate
from datetime import datetime
from models import Package

app = FastAPI()
courier_client = CourierClient()
logger = setup_logger(__name__)

@app.post("/depots/")
def create_depot(depot: DepotCreate, db: Session = Depends(get_db)):
    # API endpoint to create a new depot
    logger.info("Received request to create a new depot.")
    try:
        new_depot = DepotService.create_depot(db, depot)
        logger.info(f"Depot created successfully with ID: {new_depot.id}")
        return new_depot
    except Exception as e:
        logger.error(f"Failed to create depot: {e}")
        return {"error": "Failed to create depot"}
    finally:
        db.close()

@app.post("/depots/{depot_id}/packages/")
def create_package_with_pickup(
    depot_id: int,
    data: PackagePickupCreate,
    db: Session = Depends(get_db)
):
    logger.info(f"Received request to create package for depot ID: {depot_id}")

    try:
        pickup_request = TransactionService.create_transaction(
            db=db,
            package_create=data.package,
            depot_id=depot_id,
            driver_id=data.pickupinfo.driver_id,
            scheduled_at=data.pickupinfo.scheduled_at
        )
        logger.info(f"Package + Pickup Request created successfully with ID: {pickup_request.id}")
        return pickup_request

    except Exception as e:
        logger.error(f"Failed to create package + pickup: {e}")
        return {"error": "Failed to create package + pickup request"}
    finally:
        db.close()

@app.get("/packages/{package_id}/tracking_events/")
def get_package_tracking_events(package_id: int, db: Session = Depends(get_db)) -> dict:
    # API endpoint to get tracking events for a package
    logger.info(f"Received request to get tracking events for package ID: {package_id}")
    try:
        # obtain package
        pkg = db.query(Package).filter(Package.id == package_id).first()
        if not pkg:
            logger.warning(f"Package with ID {package_id} not found.")
            return {"error": "Package not found"}
        # obtain tracking number and fetch events        
        tracking_num = pkg.tracking_number
        tracking_events = TrackingEventService.get_events_by_tracking_num(db, tracking_num)
        logger.info(f"Retrieved {len(tracking_events)} tracking events for package ID: {package_id}")
        return pkg, tracking_events
    except Exception as e:
        logger.error(f"Failed to retrieve tracking events for package ID {package_id}: {e}")
        return {"error": "Failed to retrieve tracking events"}
    finally:
        db.close()

