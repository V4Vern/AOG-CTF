#!/bin/sh
docker build -t web-mr_elliot_alderson .
docker run --restart always -d -p 15002:80 --name web-mr_elliot_alderson web-mr_elliot_alderson
docker start web-mr_elliot_alderson