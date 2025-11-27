from models import *
from config import setup_logger, pickupStatus, packageStatus
from config import Base, engine, get_db, SessionLocal
from datetime import date, datetime

logger = setup_logger(__name__)

# initialize the database and create tables
def init_db():
    logger.info("Initializing the database and creating tables...")
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        seed_data(db)
    finally:
        db.close()


def seed_data(db):

    logger.info("Seeding initial data...")
    # Seed Depots
    depots = [
        Depot(name="Central Depot", 
              address="Gandhinagar, Sector 2", 
              is_active=True, 
              created_at=date(2024, 1, 10)),
        Depot(name="West Side Depot",
                address="Ahmedabad, Paldi", 
                is_active=True, 
                created_at=date(2024, 2, 15)),
        Depot(name="East End Depot",
                address="Surat, kamrej", 
                is_active=True, 
                created_at=date(2024, 3, 20)),
        Depot(name="North Hub Depot",
                address="Vadodara, Alkapuri",
                is_active=True,
                created_at=date(2024, 4, 25)),
        Depot(name="South Point Depot",
                address="Rajkot, Kalawad",
                is_active=False,
                created_at=date(2024, 5, 30))
    ]
    db.add_all(depots)
    db.commit()
    logger.info("Depots seeded successfully.")

    # Seed Drivers
    drivers = [
        Driver(name="Rahul Sharma",
                depot_id=1,
                phone="9876543210",
                is_active=True),
        Driver(name="Anita Desai",
                depot_id=2,
                phone="8765432109",
                is_active=True),
        Driver(name="Vikram Patel",
                depot_id=3,
                phone="7654321098",
                is_active=False),
        Driver(name="Sneha Mehta",
                depot_id=4,
                phone="6543210987",
                is_active=True),
        Driver(name="Karan Singh",
                depot_id=1,
                phone="5432109876",
                is_active=True),
        Driver(name="Pooja Nair",
                depot_id=5,
                phone="4321098765",
                is_active=False)
    ]
    db.add_all(drivers)
    db.commit()
    logger.info("Drivers seeded successfully.")

    # Seed Packages
    packages = [
        Package(recipient_name="Amit Kumar",
                address="123 MG Road, Ahmedabad",
                created_at=datetime(2024, 6, 1, 10, 30),
                updated_at=datetime(2024, 6, 1, 10, 30),
                status=packageStatus.PENDING,
                depot_id=1,
                tracking_number="TRK123456789"),
        Package(recipient_name="Neha Joshi",
                address="456 Park Street, Surat",
                created_at=datetime(2024, 6, 2, 11, 0),
                updated_at=datetime(2024, 6, 2, 11, 0),
                status=packageStatus.IN_TRANSIT,
                depot_id=2,
                tracking_number="TRK987654321"),
        Package(recipient_name="Rohit Verma",
                address="789 Lakeview Ave, Vadodara",
                created_at=datetime(2024, 6, 3, 9, 45),
                updated_at=datetime(2024, 6, 3, 9, 45),
                status=packageStatus.DELIVERED,
                depot_id=3,
                tracking_number="TRK112233445"),
        Package(recipient_name="Sneha Kapoor",
                address="321 Hilltop Rd, Rajkot",
                created_at=datetime(2024, 6, 4, 14, 15),
                updated_at=datetime(2024, 6, 4, 14, 15),
                status=packageStatus.CANCELLED,
                depot_id=4,
                tracking_number="TRK556677889"),
        Package(recipient_name="Vijay Malhotra",
                address="654 Ocean Drive, Gandhinagar",
                created_at=datetime(2024, 6, 5, 16, 0),
                updated_at=datetime(2024, 6, 5, 16, 0),
                status=packageStatus.SHIPPED,
                depot_id=5,
                tracking_number="TRK998877665")
    ]
    db.add_all(packages)
    db.commit()
    logger.info("Packages seeded successfully.")

    # Seed Pickup Requests
    pickup_requests = [
        PickupRequest(package_id=1,
                requested_at=datetime(2024, 6, 1, 12, 0),
                scheduled_at=datetime(2024, 6, 2, 10, 0),
                status=pickupStatus.SCHEDULED,
                driver_id=1),
        PickupRequest(package_id=2,
                requested_at=datetime(2024, 6, 2, 13, 30),
                scheduled_at=datetime(2024, 6, 3, 11, 0),
                status=pickupStatus.PENDING,
                driver_id=2),
        PickupRequest(package_id=3,
                requested_at=datetime(2024, 6, 3, 15, 0),
                scheduled_at=datetime(2024, 6, 4, 9, 0),
                status=pickupStatus.COMPLETED,
                driver_id=3),
        PickupRequest(package_id=4,
                requested_at=datetime(2024, 6, 4, 10, 15),
                scheduled_at=datetime(2024, 6, 5, 14, 0),
                status=pickupStatus.CANCELLED,  
                driver_id=4),
        PickupRequest(package_id=5,
                requested_at=datetime(2024, 6, 5, 11, 45),
                scheduled_at=datetime(2024, 6, 6, 16, 0),
                status=pickupStatus.SCHEDULED,
                driver_id=1)
    ]
    db.add_all(pickup_requests)
    db.commit()
    logger.info("Pickup Requests seeded successfully.")

    # Seed Tracking Events
    tracking_events = [
        TrackingEvent(package_id=1,
                event_time=datetime(2024, 6, 1, 12, 30),
                location="Ahmedabad Depot",
                description="Package received at depot"),
        TrackingEvent(package_id=2,
                event_time=datetime(2024, 6, 2, 14, 0),
                location="Surat Depot",
                description="Package dispatched from depot"),
        TrackingEvent(package_id=3,
                event_time=datetime(2024, 6, 3, 16, 15),
                location="Vadodara Depot",
                description="Package out for delivery"),
        TrackingEvent(package_id=4,
                event_time=datetime(2024, 6, 4, 11, 0),
                location="Rajkot Depot",
                description="Delivery attempted"),
        TrackingEvent(package_id=5,
                event_time=datetime(2024, 6, 5, 12, 30),    
                location="Gandhinagar Depot",
                description="Package delivered successfully")
    ]
    db.add_all(tracking_events)
    db.commit()
    logger.info("Tracking Events seeded successfully.")
    logger.info("Data seeding completed.")

if __name__ == "__main__":
    try:
        init_db()
    except Exception as e:
        logger.exception("Error while running seed_data:")