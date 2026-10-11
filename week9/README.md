# Week 9: CI/CD and Kubernates Deployment

## Objective
Practise Kubernates rolling updates, application verification, and rollback.

## Environment
- Docker
- Kubernates with kind
- kubectl
- Git and GitHub

## Rolling Deployment
Updated the week4-frontend Deployment from image veena74/week4-web:1.1 to veena74/week4-web:1.2.

Commands used:
- kind load docker-image veena74/week4-web:1.2 --name k8s-app
- kubectl rollout status deployment/week4-frontend --timeout=120s
- kubectl get deployment week4-frontend -o wide
- kubectl get pods -l app=week4-frontend

## Rollback
Restored the previous working image using Kubernates rollout undo.

Commands:
- kubectl rollout undo deployment/week4-frontend
- kubectl rollout status deployment/week4-frontend --timeout=120s

## Verification
- Rolling update to image 1.2 completed successfully.
- Rollback restored image veena74/week4-web:1.1.
- Three frontend pods were Running and Ready.
- The frontend welcome page was accessible through port forwarding.

## Notes
This exercise demonstrates Kubernates rolling updates and rollback using an existing application. Jenkins pipeline automation and additional CI/CD evidence should be documented separately once verified.
