#!/bin/sh
# Deploy / update the middleware in production with Docker.
#
# Usage:  ./deploy.sh                          pull latest code, back up the DB, rebuild, migrate
#         ./deploy.sh --no-pull                deploy the code already on disk
#         ./deploy.sh --restore-db FILE.sql    also REPLACE the production database with FILE.sql
#                                              (e.g. one made locally with ./export_db.sh)
#         ./deploy.sh --down                   just stop and remove the containers
#
# Containers are taken down (docker compose down, without -v) before rebuilding.
# Without --restore-db it never removes the database volume or ./media.
# The current database is always backed up to ./backups first.

set -e
cd "$(dirname "$0")"

PULL=1
RESTORE_FILE=""
DOWN_ONLY=0
while [ $# -gt 0 ]; do
    case "$1" in
        --no-pull) PULL=0 ;;
        --down) DOWN_ONLY=1 ;;
        --restore-db) RESTORE_FILE="$2"; shift ;;
        *) echo "Unknown option: $1"; exit 1 ;;
    esac
    shift
done

if docker compose version >/dev/null 2>&1; then
    COMPOSE="docker compose"
else
    COMPOSE="docker-compose"
fi

log() { echo; echo "==> $*"; }

if [ "$DOWN_ONLY" = 1 ]; then
    log "Stopping and removing containers (data volumes and ./media are kept)"
    $COMPOSE down --remove-orphans
    exit 0
fi

[ -f .env ] || { echo "ERROR: .env not found (needed for database settings)"; exit 1; }
mkdir -p media backups

if [ "$PULL" = 1 ]; then
    log "Pulling latest code"
    git pull --ff-only
fi

if [ -n "$RESTORE_FILE" ]; then
    [ -f "$RESTORE_FILE" ] || { echo "ERROR: $RESTORE_FILE not found"; exit 1; }
    echo
    echo "WARNING: the production database will be REPLACED with $RESTORE_FILE"
    printf "Type 'yes' to continue: "
    read CONFIRM
    [ "$CONFIRM" = "yes" ] || { echo "Aborted."; exit 1; }
fi

if [ -n "$(docker ps -q -f name=^middleware_db$)" ]; then
    BACKUP="backups/db_$(date +%Y%m%d_%H%M%S).sql"
    log "Backing up database to $BACKUP"
    docker exec middleware_db sh -c 'pg_dump -U "$POSTGRES_USER" "$POSTGRES_DB"' > "$BACKUP"
else
    log "Database container not running, skipping backup"
fi

log "Taking down running containers (data volumes and ./media are kept)"
$COMPOSE down --remove-orphans

log "Building and starting containers"
$COMPOSE up -d --build

if [ -n "$RESTORE_FILE" ]; then
    log "Restoring database from $RESTORE_FILE"
    $COMPOSE stop web
    docker exec middleware_db sh -c 'dropdb -U "$POSTGRES_USER" --if-exists --force "$POSTGRES_DB" && createdb -U "$POSTGRES_USER" "$POSTGRES_DB"'
    docker exec -i middleware_db sh -c 'psql -v ON_ERROR_STOP=1 -q -U "$POSTGRES_USER" -d "$POSTGRES_DB"' < "$RESTORE_FILE" > /dev/null
    $COMPOSE start web
fi

log "Applying migrations"
$COMPOSE exec -T web python manage.py migrate --noinput

log "Running Django checks"
$COMPOSE exec -T web python manage.py check

log "Deployment complete"
$COMPOSE ps
