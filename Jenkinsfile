
pipeline {
    agent any

    environment {
        IMAGE_NAME = 'flask-app-image'
        TAG = 'latest'
        CONTAINER_NAME = 'flask-app-container'
    }

    stages {
        stage('Clone Repository') {
            steps {
 git credentialsId: 'github-token', url: 'https://github.com/vishukanase/flask-app.git', branch: 'main'    
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker --version' // Check Docker is accessible
                    sh "docker build -t $IMAGE_NAME:$TAG ."
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    // Stop and remove old container if it exists
                    sh "docker rm -f $CONTAINER_NAME || true"

                    // Run new container
                    sh "docker run -d --name $CONTAINER_NAME -p 5000:5000 $IMAGE_NAME:$TAG"
                }
            }
        }

        stage('Show Container Logs') {
            steps {
                script {
                    sh "sleep 5"
                    sh "docker logs $CONTAINER_NAME"
                }
            }
        }
    }

    post {
        success {
            echo 'Flask app container is running. Access it on http://<Jenkins-Server-IP>:5000'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}
