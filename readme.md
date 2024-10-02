
# Sensor Monitoring Web Application

This project is a sensor monitoring web application built using **Vue.js 3.x** for the frontend and **Django 5.x** for the backend. The solution is containerized using **Docker**, allowing for easy setup and deployment.

## Features

- Displays sensor data with sorting, filtering, and searching capabilities.
- Data retrieved from a Django-based API.
- Configurable ports and URLs for easy customization.
- Fully Dockerized for streamlined deployment.

## Prerequisites

Ensure you have the following installed on your system:

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Node.js](https://nodejs.org/en/download/) (for local frontend development, optional)

# Getting Started

## 1. Clone the Repository
```bash
git clone https://github.com/MartinAbilev/SAF-SENSORS
cd SAF-SENSORS
```

## 2. Configuration

### Backend (Django)
To allow the application to work with custom URLs or ports, you need to configure the following settings:

- **Allowed Hosts**: Add your desired hostname or IP address to `ALLOWED_HOSTS` in `backend/settings.py`.

```python
ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'your-custom-url']
```

- **CORS Configuration**: If you need to allow custom URLs for the frontend, modify the `CORS_ALLOWED_ORIGINS` in `backend/settings.py`:

```python
CORS_ALLOWED_ORIGINS = [
    'http://localhost:3333',
    'http://your-custom-url'
]
```

### Frontend (Vue.js)
Update the frontend request URLs in `SensorTable.vue` to match your backend API's URL:

```javascript
axios.get('http://localhost:8000/api/sensors/')  // or your custom backend URL
```

## 3. Running the Application with Docker
This project uses Docker for easy setup and running of the frontend and backend services. The default configuration uses:

- Backend (Django): Runs on port 8000
- Frontend (Vue.js): Runs on port 3333

### Build and Run the Docker Containers
From the project root, you can build and start the services using Docker Compose.

```bash
docker-compose up --build
```

This will:

- Build the Docker images for the backend and frontend.
- Start both services in separate containers.

### Access the Application
Once the services are up, you can access the frontend in your browser at:

```arduino
http://localhost:3333
```

If you’ve configured a custom port, replace `3333` with your desired port.

## 4. Customizing Ports and URLs
You can easily customize the ports for the frontend and backend by modifying the `docker-compose.yml` file.

For example, to change the frontend port to 5000 and backend port to 9000:

```yaml
services:
  frontend:
    build:
      context: ./frontend
    ports:
      - "5000:80"  # Change frontend port here

  backend:
    build:
      context: ./backend
    ports:
      - "9000:8000"  # Change backend port here
```

## 5. Running Locally Without Docker (Optional)

### Backend (Django)
Install the required dependencies:

```bash
pip install -r backend/requirements.txt
```

Run the development server:

```bash
python backend/manage.py runserver 0.0.0.0:8000
```

### Frontend (Vue.js)
Install the required dependencies:

```bash
cd frontend
npm install
```

Start the Vue.js development server:

```bash
npm run serve
```

By default, the Vue.js frontend runs on `http://localhost:8080`. To change the port, edit the `vue.config.js` file or pass a port flag when running the server:

```bash
npm run serve -- --port 3333
```

## 6. Running the Application
To run the application after Docker is set up, use the following command:

```bash
sh run.sh
```

The application will be available at `http://localhost:3333` unless you’ve modified the configuration.

## 7. Stopping the Containers
To stop the Docker containers, run:

```bash
docker-compose down
```

## Troubleshooting

- **CORS Issues**: If you encounter CORS errors when trying to access the API from the frontend, ensure that the `CORS_ALLOWED_ORIGINS` setting in `backend/settings.py` includes the correct URL.
- **Port Conflicts**: If you have other services running on ports 3333 (frontend) or 3004 (backend), you can modify the ports in the `docker-compose.yml` file.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements
Special thanks to all contributors and the open-source community for their valuable tools and support.
