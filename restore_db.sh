#!/bin/bash

docker cp backup_20_August.sql middleware_db:/var/lib/postgresql/data/6Septback.sql
docker exec -it middleware_db psql -U postgres -d "ocean-middleware" -f /var/lib/postgresql/data/6Septback.sql
