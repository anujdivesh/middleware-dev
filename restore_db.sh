#!/bin/bash

docker cp 25_Aug_2.sql middleware_db:/var/lib/postgresql/data/25_Aug_2.sql
docker exec -it middleware_db psql -U postgres -d "ocean-middleware" -f /var/lib/postgresql/data/25_Aug_2.sql
