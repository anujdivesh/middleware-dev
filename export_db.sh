#!/bin/sh
# Export the local development database to a SQL file that deploy.sh can restore.
#
# Usage:  ./export_db.sh            -> ocean-middleware_<ddMonYYYY>.sql
#         ./export_db.sh out.sql
#
# Uses the same DB_* variables / defaults as settings.py (localhost:5432, ocean-middleware).

set -e
cd "$(dirname "$0")"

DB_NAME="${DB_NAME:-ocean-middleware}"
DB_USER="${DB_USER:-postgres}"
DB_HOST="${DB_HOST:-localhost}"
DB_PORT="${DB_PORT:-5432}"
export PGPASSWORD="${DB_PASSWORD:-Oceanportal2017*}"

OUT="${1:-${DB_NAME}_$(date +%d%b%Y).sql}"

echo "Exporting $DB_NAME from $DB_HOST:$DB_PORT to $OUT"
# --no-owner/--no-privileges so it restores cleanly into the production container
pg_dump -h "$DB_HOST" -p "$DB_PORT" -U "$DB_USER" --no-owner --no-privileges "$DB_NAME" > "$OUT"

echo "Done: $OUT ($(du -h "$OUT" | cut -f1))"
echo "Deploy it with:  ./deploy.sh --restore-db $OUT"
