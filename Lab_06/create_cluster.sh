#!/bin/bash
# =============================================================================
# GKE Cluster Creation Script
# Creates a regional GKE cluster optimized for a sentiment-analysis
# pipeline using a fine-tuned DistilBERT model on the IMDb dataset.
# =============================================================================

set -euo pipefail

# ---- customizable variables ------------------------------------------------
PROJECT_ID="kubernetes-labs-mlops-jcm"
CLUSTER_NAME="jennisha-mlops-cluster"
REGION="us-east1"
MACHINE_TYPE="e2-standard-2"
MIN_NODES=1
MAX_NODES=3
DISK_TYPE="pd-ssd"
DISK_SIZE=50
NAMESPACE="sentiment-serving"
# -----------------------------------------------------------------------------

echo "=============================================="
echo " Creating GKE cluster: ${CLUSTER_NAME}"
echo " Region: ${REGION}  |  Nodes: ${MIN_NODES}-${MAX_NODES}"
echo " Machine: ${MACHINE_TYPE}  |  Disk: ${DISK_SIZE}GB ${DISK_TYPE}"
echo "=============================================="

gcloud beta container --project "${PROJECT_ID}" \
  clusters create "${CLUSTER_NAME}" --region "${REGION}" --tier "standard" \
  --no-enable-basic-auth --cluster-version "1.32.3-gke.1140000" \
  --release-channel "stable" --machine-type "${MACHINE_TYPE}" --image-type "COS_CONTAINERD" \
  --disk-type "${DISK_TYPE}" --disk-size "${DISK_SIZE}" --metadata disable-legacy-endpoints=true \
  --scopes "https://www.googleapis.com/auth/devstorage.read_only","https://www.googleapis.com/auth/logging.write","https://www.googleapis.com/auth/monitoring","https://www.googleapis.com/auth/servicecontrol","https://www.googleapis.com/auth/service.management.readonly","https://www.googleapis.com/auth/trace.append" \
  --num-nodes "${MIN_NODES}" --logging=SYSTEM,WORKLOAD \
  --monitoring=SYSTEM,STORAGE,POD,DEPLOYMENT,STATEFULSET,HPA,CADVISOR,KUBELET \
  --enable-ip-alias --network "projects/${PROJECT_ID}/global/networks/default" \
  --subnetwork "projects/${PROJECT_ID}/regions/${REGION}/subnetworks/default" \
  --no-enable-intra-node-visibility --default-max-pods-per-node "64" --enable-autoscaling \
  --min-nodes "${MIN_NODES}" --max-nodes "${MAX_NODES}" --location-policy "ANY" --enable-ip-access \
  --security-posture=standard --workload-vulnerability-scanning=standard \
  --no-enable-google-cloud-access \
  --addons HorizontalPodAutoscaling,HttpLoadBalancing,GcePersistentDiskCsiDriver,GcsFuseCsiDriver \
  --enable-autoupgrade --enable-autorepair --max-surge-upgrade 1 --max-unavailable-upgrade 0 \
  --binauthz-evaluation-mode=DISABLED --enable-managed-prometheus --enable-shielded-nodes \
  --shielded-integrity-monitoring --shielded-secure-boot \
  --labels env=lab,owner=jennisha,model=distilbert,dataset=imdb

echo ""
echo ">>> Cluster '${CLUSTER_NAME}' created successfully!"

# fetches credentials
echo ">>> Fetching cluster credentials..."
gcloud container clusters get-credentials "${CLUSTER_NAME}" \
  --region "${REGION}" --project "${PROJECT_ID}"

# creates a dedicated namespace for the ml serving workload
echo ">>> Creating namespace '${NAMESPACE}'..."
kubectl create namespace "${NAMESPACE}" --dry-run=client -o yaml | kubectl apply -f -

# sets the new namespace as the default for this context
kubectl config set-context --current --namespace="${NAMESPACE}"

echo ""
echo ">>> Verifying cluster..."
kubectl cluster-info
kubectl get nodes -o wide
kubectl get ns

echo ""
echo "=============================================="
echo " Cluster ready. Current namespace: ${NAMESPACE}"
echo " Next step: deploy the sentiment-analysis model"
echo "=============================================="
