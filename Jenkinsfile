pipeline {
    agent any 

    environment {
        // This looks for the credential ID 'docker-hub-credentials' you created in Jenkins
        DOCKER_CREDS = credentials('swapnaraut')
        // Change 'your-dockerhub-username' to your actual Docker Hub username
        IMAGE_FRONTEND = "swapnaraut28/myfrontend:latest"
        IMAGE_BACKEND  = "swapnaraut28/mybackend:latest"

        ENV_FILE = credentials('postgresenv')

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

                echo 'Building production Docker images with environment using docker compose...'
                sh '''
                cp "$ENV_FILE" .env
                docker compose build --no-cache -env-file .env
                '''              
                
            }
        }

        stage('Push to Registry') {
            steps {
                echo 'Logging into Docker Hub and pushing images...'
                // Securely logs into Docker Hub using the credentials masked by Jenkins
                sh '''
                    echo \$DOCKER_CREDS_PSW | docker login -u \$DOCKER_CREDS_USR --password-stdin
                    echo docker pushing images
                    docker push ${IMAGE_FRONTEND}
                    docker push ${IMAGE_BACKEND}
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application locally via Docker Compose...'
                // Restarts your local containers with the newly updated images
                sh '''
                    cp "$ENV_FILE" .env
                    docker compose down --remove-orphans
                    docker network prune -f
                    docker compose up -d
                '''
            }
        }
    }

    post {
        success {
            echo 'Build, test, and deployment completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check the console logs for issues.'
            sh "docker system prune -af"
        }
    }
}