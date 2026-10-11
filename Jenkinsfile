
pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'veenadodaman/resilient-cicd-automation'
        IMAGE_TAG = '1.0'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/veena-dodamani/DevOps-Week-04.git'
            }
        }

        stage('Validate') {
            steps {
                sh 'test -f Dockerfile'
                sh 'test -f index.html'
                sh 'test -f nginx.conf'
                sh 'test -f compose.yaml'
                sh 'test -f backend/server.py'
                echo 'Required application files are present.'
            }
        }

        stage('Test') {
            steps {
                sh 'grep -q "location /api/" nginx.conf'
                sh 'grep -q "def do_GET" backend/server.py'
                echo 'Basic application checks passed.'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker --version'
                sh 'docker build -t $DOCKER_IMAGE:$IMAGE_TAG .'
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKERHUB_USER',
                    passwordVariable: 'DOCKERHUB_TOKEN'
                )]) {
                    sh '''
                        echo "$DOCKERHUB_TOKEN" | docker login \
                            --username "$DOCKERHUB_USER" --password-stdin
                        docker push "$DOCKER_IMAGE:$IMAGE_TAG"
                        docker logout
                    '''
                }
            }
        }
    }

    post {
        success {
            echo 'CI/CD build and Docker Hub publishing completed successfully.'
        }
        failure {
            echo 'Pipeline failed. Review the Console Output.'
        }
    }
}
