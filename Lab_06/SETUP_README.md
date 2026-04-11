# Lab_06 — Setup Guide

Step-by-step instructions to create the GKE cluster and deploy the Sentiment Analysis API.

---

## 1. Install Prerequisites

```bash
# Install Google Cloud CLI (macOS)
brew install --cask google-cloud-sdk

# Install kubectl
gcloud components install kubectl

# Install GKE auth plugin
gcloud components install gke-gcloud-auth-plugin

# Verify installations
gcloud version
kubectl version --client
docker --version
```

## 2. Authenticate with Google Cloud

```bash
gcloud init
gcloud auth login
gcloud config set project kubernetes-labs-mlops-jcm
```

## 3. Enable Required APIs

```bash
gcloud services enable container.googleapis.com
gcloud services enable containerregistry.googleapis.com
```

## 4. Create the GKE Cluster

```bash
cd Lab_06
chmod +x create_cluster.sh
./create_cluster.sh
```

Wait for the cluster to be created (this takes 5-10 minutes). The script will
automatically fetch credentials, create the `sentiment-serving` namespace, and
set it as the default context.

## 5. Verify Cluster is Running

```bash
kubectl cluster-info
kubectl get nodes
kubectl get ns
```

## 6. Deploy the Sentiment Analysis API

```bash
chmod +x deploy.sh
./deploy.sh
```

Or deploy manually:

```bash
# Build the Docker image
docker build -t sentiment-api:v1 app/

# Configure Docker for GCR
gcloud auth configure-docker

# tag and push
docker tag sentiment-api:v1 gcr.io/kubernetes-labs-mlops-jcm/sentiment-api:v1
docker push gcr.io/kubernetes-labs-mlops-jcm/sentiment-api:v1

# deploy to Kubernetes
kubectl apply -f k8s/namespace.yaml
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
kubectl apply -f k8s/hpa.yaml
```

## 7. Verify Deployment

```bash
# check pods are running
kubectl get pods -n sentiment-serving

# check service has external IP
kubectl get service sentiment-api-service -n sentiment-serving

# check autoscaler
kubectl get hpa -n sentiment-serving
```

## 8. Test the API

```bash
EXTERNAL_IP=$(kubectl get svc sentiment-api-service -n sentiment-serving -o jsonpath='{.status.loadBalancer.ingress[0].ip}')

# welcome message
curl http://${EXTERNAL_IP}/

# health check
curl http://${EXTERNAL_IP}/health

# model information
curl http://${EXTERNAL_IP}/model-info

# predict sentiment
curl -X POST http://${EXTERNAL_IP}/predict \
  -H "Content-Type: application/json" \
  -d '{"text": "This movie was absolutely amazing, a true masterpiece!"}'

curl -X POST http://${EXTERNAL_IP}/predict \
  -H "Content-Type: application/json" \
  -d '{"text": "Terrible film, boring and a complete waste of time."}'
```

## 9. Cleanup

```bash
# delete the app resources
kubectl delete namespace sentiment-serving

gcloud container clusters delete jennisha-mlops-cluster --region us-east1 --project kubernetes-labs-mlops-jcm
```
