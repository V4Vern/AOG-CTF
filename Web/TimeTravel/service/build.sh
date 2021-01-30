#!/bin/sh
docker build -t web-timetravel .
docker run --restart always -d -p 15004:80 --name web-timetravel web-timetravel
docker start web-timetravel
