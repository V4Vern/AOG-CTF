#!/bin/sh
docker build -t web-blog .
docker run --restart always -d -p 15014:80 --name web-blog web-blog
docker start web-blog