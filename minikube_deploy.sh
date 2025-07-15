#!/bin/bash

source ./common.sh

set -e

log "🚀 Starting minikube..."
minikube start

log "🚀 getting k8ts ready..."
eval "$(minikube docker-env)"
docker build -t $FAPI_IMAGE_NAME .
(
  set +e
  kubectl delete -f k8s/
  kubectl apply -f k8s/
)
kubectl port-forward service/fastapi-service $FAPI_KUBE_PORT:$FAPI_LOCAL_PORT
