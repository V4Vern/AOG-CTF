#!/bin/sh
docker build -t web-easyauth .
docker run --restart always -d -p 15011:80 --name web-easyauth web-easyauth
docker start web-easyauth