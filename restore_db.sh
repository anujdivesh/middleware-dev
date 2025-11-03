#!/bin/bash

docker cp 3Nov_unit.sql middleware_db:/var/lib/postgresql/data/3Nov_unit.sql
docker exec -it middleware_db psql -U postgres -d "ocean-middleware" -f /var/lib/postgresql/data/3Nov_unit.sql
