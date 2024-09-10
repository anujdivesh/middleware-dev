#!/bin/bash

docker cp 10_sept_backup.sql middleware_db:/var/lib/postgresql/data/10_sept_backup.sql
docker exec -it middleware_db psql -U postgres -d "ocean-middleware" -f /var/lib/postgresql/data/10_sept_backup.sql
