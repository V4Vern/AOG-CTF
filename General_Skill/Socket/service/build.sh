#!/bin/sh
while true;
do
docker kill prog-socks
docker rm prog-socks
docker build -t prog-socks .
docker run -d --restart always -p 13502:13502 --name prog-socks prog-socks
docker start prog-socks
sleep 60
done;