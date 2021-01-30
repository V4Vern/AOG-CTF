#!/bin/sh
docker build -t web-cheese .
docker run --restart always -d -p 15012:80 --name web-cheese web-cheese
docker start web-cheese