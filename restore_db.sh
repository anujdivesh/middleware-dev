#!/bin/bash

docker cp backup_20_August.sql 8cb99d634f8d:/6Septback.sql
docker exec -it 8cb99d634f8d psql -U postgres -d "ocean-middleware" -f /6Septback.sql
