#!/bin/bash

source ../venv/bin/activate
set -e

source ./common.sh

log "====== starting local deployment ======"
open -a Docker

log "====== installing dependencies locally ======"
pip install --upgrade pip
pip install --no-cache-dir -r requirements.txt

log "✅ Running unit tests.... %f"
pytest

log "creating latest image... "
docker build -t $FAPI_IMAGE_NAME .

log "🧹cleaning up running containers"
(
  set +e
  docker stop $FAPI_CONTAINER_NAME || true
  docker rm $FAPI_CONTAINER_NAME || true
  docker stop $DB_CONTAINER_NAME || true
  docker rm $DB_CONTAINER_NAME || true
)

log "🚀 Starting new containers..."
docker network create $NETWORK || true

docker run -d  --name $FAPI_CONTAINER_NAME --network $NETWORK \
  -p $FAPI_LOCAL_PORT:$FAPI_LOCAL_PORT  \
  -e DB_HOST=$DB_CONTAINER_NAME -e DB_USER=$DB_USER -e DB_PASS=$DB_PASS -e DB_NAME=$DB_NAME \
  $FAPI_IMAGE_NAME

docker run --name $DB_CONTAINER_NAME --network $NETWORK \
  -e POSTGRES_PASSWORD=$DB_PASS -e POSTGRES_USER=$DB_USER -e POSTGRES_DB=$DB_NAME -p $POSTGRES_PORT:$POSTGRES_PORT -d $POSTGRES_IMAGE


log "⏳ Waiting for PostgreSQL to be ready..."
until docker exec $DB_CONTAINER_NAME pg_isready -U $DB_USER; do sleep 1; done

log "🛠️ Initializing database..."
PGPASSWORD=$DB_PASS psql -h localhost -U $DB_USER -d $DB_NAME -f init_db.sql

log "🌍 App is running at http://localhost:" $LOCAL_PORT
log "✅ Database ready."
