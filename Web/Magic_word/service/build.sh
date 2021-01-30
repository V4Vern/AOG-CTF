#!/bin/sh
docker build -t web-obfuscation .
docker run --restart always -d -p 15008:80 --name web-obfuscation web-obfuscation
docker start web-obfuscation