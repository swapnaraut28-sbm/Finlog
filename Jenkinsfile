pipeline {
    agent any 

    environment {
        // This looks for the credential ID 'docker-hub-credentials' you created in Jenkins
        DOCKER_CREDS = credentials('swapnaraut')
        // Change 'your-dockerhub-username' to your actual Docker Hub username
        IMAGE_FRONTEND = "swapnaraut28/myfrontend:latest"
        IMAGE_BACKEND  = "swapnaraut28/mybackend:latest"
        //IMAGE_POSTGRES  = "swapnaraut28/postgres:15-alpine"  

        ENV_FILE = credentials('postgresenv')

    }

    stages {
        stage('Checkout') {
            steps {
                // Jenkins pulls your code from the GitHub repository configuration
                checkout scm
            }
        }

        stage('Load and Use .env Variables') {
            steps {
                script {
                    // Method 1: Source the file directly within a single shell execution block
                    sh '''
                        # Export the variables from the secret file
                        export $(grep -v '^#' $ENV_FILE | grep -v '^$' | xargs)
                        
                        # Use your variables safely inside this shell session
                        echo "POSTGRES_USER: $POSTGRES_USER"
                        echo "POSTGRES_PASSWORD: $POSTGRES_PASSWORD"
                        echo "POSTGRES_DB: $POSTGRES_DB"
                        echo "DATABASE_URL: $DATABASE_URL"

                        docker compose build
                    '''
                }

            }
        }

        // stage('Build with Compose') {
        //     steps {

        //         echo 'Building production Docker images using docker compose...'
        //         // Docker Compose will read your setup and build the images locally
        //         sh "docker compose build"
        //     }
        // }

        stage('Push to Registry') {
            steps {
                echo 'Logging into Docker Hub and pushing images...'
                // Securely logs into Docker Hub using the credentials masked by Jenkins
                sh "echo \$DOCKER_CREDS_PSW | docker login -u \$DOCKER_CREDS_USR --password-stdin"
                // sh "echo docker tagging"
                // sh "docker tag ${IMAGE_FRONTEND} swapnaraut28/finlog-frontend:latest"
                // sh "docker tag ${IMAGE_BACKEND} swapnaraut28/finlog-backend:latest"
                // sh "docker tag ${IMAGE_POSTGRES} swapnaraut28/postgres:15-alpine"
                sh "echo docker pushing images"
                sh "docker push ${IMAGE_FRONTEND}"
                sh "docker push ${IMAGE_BACKEND}"
                //sh "docker push ${IMAGE_POSTGRES}"
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
            // Cleans up workspace files after the run is complete
            cleanWs()
            script {
                // Optionally, you can also clean up Docker images and containers to free up space
                echo 'Cleaning up Docker images and containers...'
                sh "docker system prune -af"
            }
        }
        success {
            echo 'Build, test, and deployment completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check the console logs for issues.'
        }
    }
}