#!/bin/sh
docker build -t web-injection .
docker run --restart always -d -p 15001:80 --name web-injection web-injection
docker start web-injection