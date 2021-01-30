#!/bin/sh
docker build -t inspector.
docker run --restart always -d -p 15000:80 --name inspector inspector
docker start inspector