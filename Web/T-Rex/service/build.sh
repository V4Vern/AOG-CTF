#!/bin/sh
docker build -t web-t-rex .
docker run --restart always -d -p 15003:80 --name web-t-rex web-t-rex
docker start web-t-rex