pipeline {
    agent any 

    environment {
        // This looks for the credential ID 'docker-hub-credentials' you created in Jenkins
        DOCKER_CREDS = credentials('docker-hub-credentials')
        // Change 'your-dockerhub-username' to your actual Docker Hub username
        IMAGE_FRONTEND = "swapnaraut28/finlog-frontend:latest"
        IMAGE_BACKEND  = "swapnaraut28/finlog-backend:latest"
        IMAGE_POSTGRES  = "swapnaraut28/postgres:15-alpine"
    }

    stages {
        stage('Checkout') {
            steps {
                // Jenkins pulls your code from the GitHub repository configuration
                checkout scm
            }
        }

        stage('Build with Compose') {
            steps {
                echo 'Building production Docker images using docker compose...'
                // Docker Compose will read your setup and build the images locally
                sh "docker compose build"
            }
        }

        stage('Push to Registry') {
            steps {
                echo 'Logging into Docker Hub and pushing images...'
                // Securely logs into Docker Hub using the credentials masked by Jenkins
                sh "echo \$DOCKER_CREDS_PSW | docker login -u \$DOCKER_CREDS_USR --password-stdin"
                sh "docker push ${IMAGE_FRONTEND}"
                sh "docker push ${IMAGE_BACKEND}"
                sh "docker push ${IMAGE_POSTGRES}"
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application locally via Docker Compose...'
                // Restarts your local containers with the newly updated images
                sh "docker compose down"
                sh "docker compose up -d"
            }
        }
    }

    post {
        always {
            echo 'Cleaning up intermediate Docker build caches to save disk space...'
            sh "docker image prune -f"
        }
    }
}