#!/bin/bash

docker cp backup18.sql middleware_db:/var/lib/postgresql/data/backup18.sql
docker exec -it middleware_db psql -U postgres -d "ocean-middleware" -f /var/lib/postgresql/data/backup18.sql
