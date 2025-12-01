from fastapi import FastAPI, Depends, HTTPException
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

@app.get("/packages/{package_id}/tracking_events/")
def get_package_tracking_events(package_id: int, db: Session = Depends(get_db)) -> dict:
    # API endpoint to get tracking events for a package
    logger.info(f"Received request to get tracking events for package ID: {package_id}")
    # obtain package
    pkg = db.query(Package).filter(Package.id == package_id).first()
    if not pkg:
        logger.warning(f"Package with ID {package_id} not found.")
        raise HTTPException(status_code=404, detail="Package not found")
    try:
        # obtain tracking number and fetch events        
        tracking_num = pkg.tracking_number
        tracking_events = TrackingEventService.get_events_by_tracking_num(db, tracking_num)
        logger.info(f"Retrieved {len(tracking_events)} tracking events for package ID: {package_id}")
        return { "package": pkg , "tracking_events": tracking_events}
    except Exception as e:
        logger.error(f"Failed to retrieve tracking events for package ID {package_id}: {e}")
        return {"error": "Failed to retrieve tracking events"}

@app.post("/packages/{package_id}/push_status/")
def push_package_status(package_id: int, package_status: str, db: Session = Depends(get_db)) -> dict:
    # API endpoint to push package status to external courier service
    logger.info(f"Received request to push status for package ID: {package_id}")
    # obtain package
    pkg = db.query(Package).filter(Package.id == package_id).first()
    if not pkg:
        logger.warning(f"Package with ID {package_id} not found.")
        raise HTTPException(status_code=404, detail="Package not found")
    try:
        tracking_num = pkg.tracking_number
        success = courier_client.push_status_update(tracking_num, package_status)
        if success:
            logger.info(f"Status '{package_status}' pushed successfully for package ID: {package_id}")
            return {"message": "Status pushed successfully"}
        else:
            logger.error(f"Failed to push status for package ID: {package_id}")
            return {"error": "Failed to push status"}
    except Exception as e:
        logger.error(f"Error pushing status for package ID {package_id}: {e}")
        return {"error": "Error pushing status"}
    
@app.post("/sync/tracking_info/")
def sync_tracking_info(db : Session = Depends(get_db)) -> dict:
    # API endpoint to sync tracking info for all packages
    logger.info("Received request to sync tracking info for all packages.")
    pkg = db.query(Package).filter(Package.tracking_number != None).all()
    if not pkg:
        logger.warning("No packages with tracking numbers found.")
        raise HTTPException(status_code=404, detail="No packages with tracking numbers found")
    
    try:
        results = []
        for package in pkg:
            tracking_num = package.tracking_number
            tracking_info = courier_client.fetch_tracking_info(tracking_num)
            results.append({
                "package_id": package.id,
                "tracking_number": tracking_num,
                "tracking_info": tracking_info
            })
        logger.info(f"Successfully synced tracking info for {len(results)} packages.")
        return {"synced_tracking_info": results}
    except Exception as e:
        logger.error(f"Failed to sync tracking info: {e}")
        return {"error": "Failed to sync tracking info"}