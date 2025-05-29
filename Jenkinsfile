pipeline {
    agent any

    environment {
        IMAGE_NAME = 'flask-app-image'
        TAG = 'latest'
        CONTAINER_NAME = 'flask-app-container'
        DOCKER_HUB_REPO = '<your-docker-hub-username>/flask-app-image'
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
                    sh 'docker --version'
                    sh "docker build -t ${IMAGE_NAME}:${TAG} ."
                }
            }
        }

        stage('Tag & Push Image to Docker Hub') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', usernameVariable: 'DOCKER_HUB_USERNAME', passwordVariable: 'DOCKER_HUB_PASSWORD')]) {
                        sh "docker tag ${IMAGE_NAME}:${TAG} $DOCKER_HUB_REPO:${TAG}"
                        sh "echo $DOCKER_HUB_PASSWORD | docker login -u $DOCKER_HUB_USERNAME --password-stdin"
                        sh "docker push $DOCKER_HUB_REPO:${TAG}"
                    }
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    sh "docker rm -f ${CONTAINER_NAME} || true"
                    sh "docker run -d --name ${CONTAINER_NAME} -p 5000:5000 ${IMAGE_NAME}:${TAG}"
                }
            }
        }

        stage('Show Container Logs') {
            steps {
                script {
                    sh "sleep 5"
                    sh "docker logs ${CONTAINER_NAME}"
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
