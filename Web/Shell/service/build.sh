#!/bin/sh
while true;
do
docker kill web-shell
docker rm web-shell
docker build -t web-shell .
docker run --restart always -d -p 15013:80 --name web-shell web-shell
docker start web-shell
sleep 300
done;