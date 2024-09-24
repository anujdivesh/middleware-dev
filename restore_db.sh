#!/bin/bash

docker cp 24Sept2.sql middleware_db:/var/lib/postgresql/data/24Sept2.sql
docker exec -it middleware_db psql -U postgres -d "ocean-middleware" -f /var/lib/postgresql/data/24Sept2.sql
