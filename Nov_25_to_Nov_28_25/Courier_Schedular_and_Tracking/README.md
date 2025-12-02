📦 Courier Scheduler & Tracking System

A lightweight backend system built using FastAPI, SQLAlchemy, and Pydantic, simulating a real-world courier workflow including depots, drivers, packages, pickup scheduling, status updates, and tracking sync using a mock external API.

🚀 Features
    - ✔ Depot Management
        - Add, read, and manage courier depots.
    - ✔ Driver Management
        - Create drivers linked to a depot.
    - ✔ Package Management
        - Create packages, assign drivers, schedule pickups.
    - ✔ Pickup Requests
        - Automatically generated during a transaction.
    - ✔ Tracking Events
        - Simulated remote tracking sync via httpbin.
    - ✔ Logging
        - All actions logged with timestamps under /logs.
    - ✔ Demo Script
        - A fully automated demo.py that runs the full lifecycle.


🗄 Database
    - Uses SQLite
    - SQLAlchemy ORM models include:
        - Depot → Packages (1:M)
        - Driver → PickupRequests (1:M)
        - Package → PickupRequest (1:1)
        - Package → TrackingEvents (1:M)
        - Migration occurs automatically on first run.

🏗 Project Structure

    Courier_Schedular_and_Tracking/
    │
    ├── api/
    │   └── app.py                 # Main FastAPI application (routes)
    │
    ├── config/
    │   ├── db_config.py           # Database engine + SessionLocal + Base
    │   ├── enum_config.py         # packageStatus & pickupStatus enums
    │   ├── log_config.py          # Logger setup
    │
    ├── database/                  # Auto-generated SQLite DB file lives here
    │
    ├── integrations/
    │   └── courier_client.py      # httpbin-based fake remote courier API
    │
    ├── logs/
    │   └── app.log                # Rotating log files generated here
    │
    ├── models/
    │   ├── depot.py               # Depot model
    │   ├── driver.py              # Driver model
    │   ├── package.py             # Package model
    │   ├── pickup_request.py      # PickupRequest model
    │   └── tracking_event.py      # TrackingEvent model
    │
    ├── schema/
    │   ├── depot_schema.py
    │   ├── driver_schema.py
    │   ├── package_schema.py
    │   ├── pickup_request_schema.py
    │   ├── tracking_event_schema.py
    │   └── __init__.py
    │
    ├── services/
    │   ├── depot_services.py
    │   ├── driver_services.py
    │   ├── package_services.py
    │   ├── pickup_request_services.py
    │   ├── transaction_services.py
    │   ├── tracking_event_services.py
    │   └── seed_data.py           # Seeds default depots, drivers, packages
    │
    ├── demo.py                    # Full workflow demo script
    ├── main.py                    # Uvicorn entrypoint for FastAPI
    ├── requirements.txt           # Python dependencies
    └── README.md


▶ Running the Application
    - 1️⃣ Install dependencies:
        >> pip install -r requirements.txt
    - 2️⃣ Seed the Database (Important)
        - Before running the app or demo, populate the DB with sample data.
        >> python -m services.seed_data
    - 3️⃣ Start FastAPI Server
        >> uvicorn main:app --reload
        - API Documentation
            Swagger UI → http://127.0.0.1:8000/docs
    - 4️⃣ Run the Demo Script
        - This script performs full workflow automation:
            - Create a depot
            - Create a driver
            - Create a package + pickup (transaction)
            - Push package status
            - Sync tracking info
            - Run:
                >> python demo.py
            - Logs + nicely formatted output will appear.

🌐 External Courier API (Mock)
- The system uses httpbin.org to simulate:
    - Pickup creation (POST /post)
    - Status push (PUT /put)
    - Tracking retrieval (GET /get)
- Located in:
    - integrations/courier_client.py

🛡 Error Handling
- Pydantic request validation
- roper error responses
- Database transaction rollback
- Full logging on every failure


🧾 Logging
- Logs are saved to the /logs folder.
- Every major action (API, service, integration, demo) is logged with:
    - Timestamp
    - Severity
    - Message
    - Module

📄 License
This project is for educational and internship learning purposes.
Feel free to extend and customize.

