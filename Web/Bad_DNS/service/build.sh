#!/bin/sh
docker build -t web-bad-admin .
docker run --restart always -d -p 15007:80 --name web-bad-admin web-bad-admin
docker start web-bad-admin