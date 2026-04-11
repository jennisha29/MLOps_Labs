#!/bin/bash
# =============================================================================
# Deploy the Sentiment Analysis API to the GKE cluster
# Builds the Docker image, pushes to GCR, and applies K8s manifests
# Author: Jennisha Martin
# =============================================================================

set -euo pipefail

PROJECT_ID="kubernetes-labs-mlops-jcm"
IMAGE_NAME="sentiment-api"
IMAGE_TAG="v1"
GCR_IMAGE="gcr.io/${PROJECT_ID}/${IMAGE_NAME}:${IMAGE_TAG}"
NAMESPACE="sentiment-serving"

echo "=============================================="
echo " Deploying Sentiment Analysis API"
echo " Image: ${GCR_IMAGE}"
echo " Namespace: ${NAMESPACE}"
echo "=============================================="

echo ""
echo "=== Step 1: Build Docker image ==="
docker build -t ${IMAGE_NAME}:${IMAGE_TAG} app/
echo ">>> Image built successfully."

echo ""
echo "=== Step 2: Tag and push to Google Container Registry ==="
docker tag ${IMAGE_NAME}:${IMAGE_TAG} ${GCR_IMAGE}
docker push ${GCR_IMAGE}
echo ">>> Image pushed to ${GCR_IMAGE}"

echo ""
echo "=== Step 3: Apply Kubernetes manifests ==="
kubectl apply -f k8s/namespace.yaml
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
kubectl apply -f k8s/hpa.yaml
echo ">>> Manifests applied."

echo ""
echo "=== Step 4: Wait for rollout ==="
kubectl rollout status deployment/sentiment-api -n ${NAMESPACE} --timeout=120s

echo ""
echo "=== Step 5: Get service external IP ==="
kubectl get service sentiment-api-service -n ${NAMESPACE}

echo ""
echo "=============================================="
echo " Deployment complete!"
echo " Run: kubectl get svc -n ${NAMESPACE} to get the external IP"
echo "=============================================="
