#!/bin/bash

log() {
  echo -e "\033[0;32m$1\033[0m"
}

NETWORK="dating-app-network"
FAPI_LOCAL_PORT=8000
FAPI_KUBE_PORT=9000
FAPI_IMAGE_NAME="my-fast-api:latest"
FAPI_CONTAINER_NAME="fastapi-app"
DB_PASS="pass123"
DB_USER="aiuser"
DB_CONTAINER_NAME="pg-play1"
DB_NAME="profiledb"
POSTGRES_IMAGE="postgres:15"
POSTGRES_PORT="5432"

cd ~/code/mcp/pythonProject/ || true