#!/bin/bash

docker cp 26_Aug_2.sql middleware_db:/var/lib/postgresql/data/26_Aug_2.sql
docker exec -it middleware_db psql -U postgres -d "ocean-middleware" -f /var/lib/postgresql/data/26_Aug_2.sql
