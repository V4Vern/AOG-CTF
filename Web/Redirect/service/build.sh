#!/bin/sh
docker build -t web-redirect .
docker run --restart always -d -p 15010:80 --name web-redirect web-redirect
docker start web-redirect