pipeline {
    agent any

    parameters {
        string(name: 'IMAGE_NAME', defaultValue: 'flask-app-image', description: 'Enter Docker image name')
        string(name: 'TAG', defaultValue: 'latest', description: 'Enter Docker image tag')
        string(name: 'CONTAINER_NAME', defaultValue: 'flask-app-container', description: 'Enter Docker container name')
        string(name: 'GIT_CREDENTIAL_ID', defaultValue: 'github-token', description: 'Enter GitHub credential ID')
        string(name: 'GIT_REPO_URL', defaultValue: 'https://github.com/vishukanase/flask-app.git', description: 'Enter GitHub repository URL')
        string(name: 'GIT_BRANCH', defaultValue: 'main', description: 'Enter Git branch name')        
    }

    stages {
        stage('Clone Repository') {
            steps {
                script {
                    git credentialsId: "${GIT_CREDENTIAL_ID}", url: "${GIT_REPO_URL}", branch: "${GIT_BRANCH}"
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker --version' // Check Docker installation
                    sh "docker build -t ${IMAGE_NAME}:${TAG} ."
                }
            }
        }
        
stage('Delete Old Docker Image from Hub') {
    steps {
        script {
            withCredentials([string(credentialsId: 'docker-hub-token', variable: 'DOCKER_HUB_TOKEN')]) {
                sh """
                curl -X GET -H 'Authorization: Bearer $DOCKER_HUB_TOKEN' \
                https://hub.docker.com/v2/repositories/vishvajitkanase/flask-app-image/tags | \
                jq -r '.results[] | select(.name != "latest") | .name' | \
                xargs -I {} curl -X DELETE -H 'Authorization: Bearer $DOCKER_HUB_TOKEN' \
                https://hub.docker.com/v2/repositories/vishvajitkanase/flask-app-image/tags/{}
                """
            }
        }
    }
}


stage('Push to Docker Hub') {
    steps {
        script {
            withCredentials([string(credentialsId: 'docker-hub-token', variable: 'DOCKER_HUB_TOKEN'),
                             string(credentialsId: 'docker-hub-username', variable: 'DOCKER_HUB_USERNAME')]) {
                sh "echo $DOCKER_HUB_TOKEN | docker login -u $DOCKER_HUB_USERNAME --password-stdin"
                sh "docker push $DOCKER_HUB_USERNAME/${IMAGE_NAME}:${TAG}"
            }
        }
    }
}



        stage('Run Docker Container') {
            steps {
                script {
                    // Stop and remove old container if it exists
                    sh "docker rm -f ${CONTAINER_NAME} || true"

                    // Run new container
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
            echo "Flask app container is running. Access it on http://<Jenkins-Server-IP>:5000"
        }
        failure {
            echo "Pipeline failed."
        }
    }
}
