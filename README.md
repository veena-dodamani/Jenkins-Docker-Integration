# DevOps Docker Containerization

## Project Overview

This project demonstrates containerization of a multi-tier web application using Docker and Docker Compose. It includes a frontend, backend, and database configured to run together in separate containers.

## Technologies Used

- Docker
- Docker Compose
- Nginx
- Python
- MySQL
- Docker Hub

## Topics Covered

- Docker Images and Containers
- Dockerfile Creation
- Container Port Mapping
- Docker Volumes for Persistent Storage
- Docker Networks for Container Communication
- Docker Compose for Multi-Container Applications
- Publishing Images to Docker Hub

## Application Architecture

- **Frontend:** Nginx
- **Backend:** Python
- **Database:** MySQL

Docker Compose manages the application services and their communication.

## Docker Hub

The frontend Docker image is published on Docker Hub.

- **Repository:** `veena74/week4-web`
- **Tag:** `1.0`
- **Image:** `veena74/week4-web:1.0`

**Docker Hub Repository:**  
https://hub.docker.com/r/veena74/week4-web

## Getting Started

### Prerequisites

Install Docker and Docker Compose on your system.

### Clone the Repository

```bash
git clone https://github.com/veena-dodamani/DevOps-Docker-Containerization.git
cd DevOps-Docker-Containerization
```

### Start the Application

If the repository contains a `docker-compose.yml` file, run:

```bash
docker compose up -d --build
```

### Check Running Containers

```bash
docker compose ps
```

### View Logs

```bash
docker compose logs
```

### Stop the Application

```bash
docker compose down
```

## Key Learnings

- Building and managing Docker images and containers.
- Configuring container networking and port mapping.
- Persisting data with Docker volumes.
- Running multi-container applications with Docker Compose.
- Publishing Docker images to Docker Hub.

## Author

**Veena Shivappa Dodamani**

- GitHub: https://github.com/veena-dodamani
- LinkedIn: https://www.linkedin.com/in/veena-dodamani-b82265301/
