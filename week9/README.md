# Week 9: Kubernetes Rolling Updates and Rollback

## 1. Project Overview

This project demonstrates hands-on practice with Kubernetes rolling updates, application verification, and rollback using a local Kubernetes cluster created with kind.

## 2. Objectives

- Perform rolling updates of a Kubernetes Deployment.
- Verify application and Pod status after deployment.
- Roll back to a previously working application version.
- Document deployment and recovery procedures.

## 3. Technologies Used

- Docker
- Kubernetes
- kind
- kubectl
- Git and GitHub

## 4. Implementation

### 4.1 Rolling Update

Updated the `week4-frontend` Deployment from image version `1.1` to `1.2`.

Commands used:

```bash
kind load docker-image veena74/week4-web:1.2 --name k8s-app
kubectl rollout status deployment/week4-frontend --timeout=120s
kubectl get deployment week4-frontend -o wide
kubectl get pods -l app=week4-frontend
```

### 4.2 Rollback

Restored the previous working image version `1.1` using Kubernetes rollout undo.

Commands used:

```bash
kubectl rollout undo deployment/week4-frontend
kubectl rollout status deployment/week4-frontend --timeout=120s
kubectl get deployment week4-frontend -o wide
```

## 5. Verification and Results

- Successfully updated the frontend image to version `1.2`.
- Verified that three frontend Pods were running and ready.
- Successfully rolled back to image version `1.1`.
- Confirmed that the frontend welcome page was accessible through port forwarding.

## 6. Key Learnings

- Kubernetes rolling updates and deployment strategies.
- Deployment and Pod health verification.
- Application availability checks.
- Rollback and recovery using kubectl.

## 7. Conclusion

This hands-on exercise demonstrates Kubernetes deployment management, rolling updates, application verification, and rollback in a local development environment.

## 8. Author

**Veena Shivappa Dodamani**

GitHub: https://github.com/veena-dodamani
