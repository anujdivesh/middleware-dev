#!/bin/bash

docker cp 8Julywidget.sql middleware_db:/var/lib/postgresql/data/8Julywidget.sql
docker exec -it middleware_db psql -U postgres -d "ocean-middleware" -f /var/lib/postgresql/data/8Julywidget.sql
