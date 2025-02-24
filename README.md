1] Python Web Application:
Create a basic Python Flask app that serves a simple API returning a " " message.
= index.py is the Flask API which simply return the message => Good Day 24/02/2025 
Install dependencies using pip and create a requirements.txt file.
= for installing the requirement i am use the command => pip install -r requirements.txt 


2] Dockerize the Application:
Write a Dockerfile to containerize the Flask app.
=> Dockerfile which is using the base image of the => python:3-alpine3.15
  and all the command is in the Dockerfile 

Build and run the Docker image locally to ensure the app works in the container.
=> Runed the Dockerfile with the service of the loadbalancer which you see in the attached photos and 

3]  Push Docker Image to GitHub Container Registry:

Create a GitHub repository and push the Docker image to GitHub Container Registry.
=>i am created the flask-app repo inside my profile vishukanase on gitHub and push the local folder on gitHub Repo
echo "# flask-app" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/vishukanase/flask-app.git
git push -u origin main

github repo with git push origin main (git branch -m main)

=>login to the GitHub container Registry :
1) create the tocken setting->Develpoer setting -> personal access tocken -> tocken classic -> Genrate new tocken -> genrate new tocken (classic) -> add note , expiration and scopes and click on genrate  
2) login through vs code:
docker --username vishukanase --password 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 ghcr.io
Tag and push the image using the docker CLI.
=>docker tag flask ghcr.io/vishukanase/flask-app
=>docker push ghcr.io/vishukanase/flask-app
kubectl create secret docker-registry my-registry-key1   --docker-server=ghcr.io   
--docker-username=vishukanase   --docker-password=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   --docker-email=vishukanase0@gmail.com

4] Set Up Kubernetes Cluster:
Set up a Kubernetes cluster (using Minikube locally or Azure Kubernetes Service - AKS).
=>start the minikube i.e minikube start --driver=docker

Write a Kubernetes deployment.yaml file to deploy the Flask app as a Kubernetes deployment.
=>deployment file and service file which is included into the deployment folder 
 = kubectl apply -f deploy.yml
 = kubectl apply -f service.yml

Expose the app with a Kubernetes Service.
=> minikube service web-app-service (you can see in attached photos)

5] Deploy Azure Resources Using Python SDK:
Use the Azure Python SDK to create and manage Azure resources (like AKS or Azure Container Instances).
Write a Python script to authenticate with Azure and deploy/manage resources.
=>These packages are part of the Azure Python SDK and are essential for interacting with various Azure services.
-- pip install azure-mgmt-resource azure-mgmt-containerservice azure-identity-
-- sdk-script.py in the git repo contain the script of the file


6] clean up:After testing, you can clean up your Kubernetes environment by deleting the deployment and service you created:

kubectl delete deployment web-app-deployment
kubectl delete service web-app-service

SDK:
pip install -r requirements.txt (all the requirement whichi is mentioned in the is present in the requiement.txt files )
az login (login through azure cli)
python sdk-script.py
