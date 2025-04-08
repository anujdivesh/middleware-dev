#!/bin/bash

docker cp 9_AprilFinal.sql middleware_db:/var/lib/postgresql/data/9_AprilFinal.sql
docker exec -it middleware_db psql -U postgres -d "ocean-middleware" -f /var/lib/postgresql/data/9_AprilFinal.sql
