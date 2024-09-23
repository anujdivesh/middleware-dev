#!/bin/bash

docker cp 23SeptBack.sql middleware_db:/var/lib/postgresql/data/23SeptBack.sql
docker exec -it middleware_db psql -U postgres -d "ocean-middleware" -f /var/lib/postgresql/data/23SeptBack.sql
