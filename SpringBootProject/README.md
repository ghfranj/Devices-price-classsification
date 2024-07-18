# Devices Price Classification System

## Overview
This project consists of two main components:
- A Python-based ML model to predict device prices.
- A Spring Boot application to manage devices and interact with the ML model.

## Prerequisites
- Python 3.x
- Java 17
- Maven
- PostgreSQL

## Setup

### Flask Application
1. Navigate to the `flask_app` directory.
2. Install dependencies: `pip install -r requirements.txt`
3. Run the Flask app: `python flask_app.py`

### Spring Boot Application
1. Update `src/main/resources/application.properties` with your PostgreSQL credentials.
2. Build the project: `mvn clean install`
3. Run the application: `mvn spring-boot:run`

## API Endpoints

### Flask Application
- `POST /predict_single`: Predict price for a single device.

### Spring Boot Application
- `GET /api/devices`: Retrieve a list of all devices.
- `GET /api/devices/{id}`: Retrieve details of a specific device by ID.
- `POST /api/devices`: Add a new device.
- `POST /api/predict/{deviceId}`: Predict the price for a device and update its price range.

## Testing
1. Add a new device via `POST /api/devices`.
2. Predict the price for the device via `POST /api/predict/{deviceId}`.

## License
[Specify your license here]
