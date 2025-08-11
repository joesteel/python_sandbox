#!/bin/bash

source ./common.sh
RELEASE_TYPE=$1
if [ -z "$RELEASE_TYPE" ]; then
  echo "No RELEASE_TYPE provided. Running in default mode."
  RELEASE_TYPE="default"
fi

set -e

log "🚀 Starting minikube..."
minikube start

log "🚀 getting k8ts ready..."
eval "$(minikube docker-env)"
docker build -t $FAPI_IMAGE_NAME .
minikube image load  $FAPI_IMAGE_NAME
if [ "$RELEASE_TYPE" == "ff" ]; then
 (
  set +e
  kubectl delete -f k8s/
  kubectl apply -f k8s/
)
else
  kubectl rollout restart deployment fastapi
fi

kubectl port-forward service/fastapi-service $FAPI_KUBE_PORT:$FAPI_LOCAL_PORT
