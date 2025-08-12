#!/bin/bash

docker cp 12Aug_1.sql middleware_db:/var/lib/postgresql/data/12Aug_1.sql
docker exec -it middleware_db psql -U postgres -d "ocean-middleware" -f /var/lib/postgresql/data/12Aug_1.sql
