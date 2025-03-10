# GeoFarmHub
GeoFarm Hub is a Django REST API with PostGIS, designed for managing clients, farms, and transactions in a real estate business.

------------------------------------------------------------

## Prerequisites

- **Docker** (version 20+ recommended)
- **Docker Compose** (version 1.29+ or the Docker Compose V2 plugin)
- **Make** (commonly available on Linux and macOS; on Windows, consider using WSL or a similar environment)

## Setup

### 1. Clone the Repository

```bash
git clone git@github.com:JoelenCruz/GeoFarmHub.git
cd GeoFarmHub
```

### 2. Run
```bash
make
```


###  3. Access the Application
Once the containers are up, open your browser and navigate to:
```bash
https://localhost:8443/
```

###  4. Additional Information
Services: The application uses Docker Compose to run the Django API, PostgreSQL with PostGIS, and Nginx as a reverse proxy.
Makefile: The Makefile includes common commands to build, start, and manage the application.

<img src="https://github.com/user-attachments/assets/e09c83fe-d620-4567-bfe5-35b1196fb353" alt="image" width="400" />


------------------------------------------------------------

## API

All API endpoints are relative to the base URL:

  https://localhost:8443/api/



### ENDPOINTS


#### Clients

https://localhost:8443/api/clients/
  

#### Farms

https://localhost:8443/api/farms/


#### Transactions

https://localhost:8443/api/transactions/

