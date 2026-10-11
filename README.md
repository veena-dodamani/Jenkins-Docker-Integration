# Jenkins-Docker Integration

## Project Overview

This project demonstrates integrating Docker with Jenkins by creating a custom Jenkins Docker image with Docker tools installed.

## Technologies Used

- Jenkins
- Docker
- Dockerfile
- Linux
- Git and GitHub

## Project Structure

```text
Jenkins-Docker-Integration/
├── Dockerfile
└── README.md
```

## Dockerfile

The custom image uses Jenkins LTS with Java 21 and installs Docker tools.

```dockerfile
FROM jenkins/jenkins:lts-jdk21

USER root

RUN apt-get update \
    && apt-get install -y docker.io \
    && rm -rf /var/lib/apt/lists/*

USER jenkins
```

## Build the Image

```bash
docker build -t week9-jenkins .
```

## Run Jenkins

```bash
docker run -d --name week9-jenkins \
  -p 8081:8080 \
  -p 50000:50000 \
  -v jenkins_home:/var/jenkins_home \
  -v /var/run/docker.sock:/var/run/docker.sock \
  week9-jenkins
```

Open Jenkins at `http://localhost:8081`.

**Security note:** Mounting the Docker socket gives Jenkins significant control over the host Docker daemon. Use this setup only in a trusted development environment.

## Key Learnings

- Building a custom Jenkins Docker image.
- Installing Docker tools in Jenkins.
- Configuring Docker volumes and port mapping.
- Connecting Jenkins to the Docker daemon.

## Author

**Veena Shivappa Dodamani**

- GitHub: https://github.com/veena-dodamani
- LinkedIn: https://www.linkedin.com/in/veena-dodamani-b82265301/
