#!/bin/bash
set -e

log() {
  echo -e "\033[0;32m$1\033[0m"
}

port=8000
image_name="my-fast-api-container:latest"
run_time_name="fastapi-app"


log "====== starting local deployment ======"

log "✅ Running unit tests.... %f"
pytest

log "creating latest image... "
docker build -t $image_name .

log "🧹cleaning up running containers"
docker docker rm -f "$(docker ps | grep $run_time_name | awk 'NR==1{print $1}')" || true

log "🚀 Starting new container..."
docker run -d  --name $run_time_name -p $port:$port $image_name

log "🌍 App is running at http://localhost:" $port