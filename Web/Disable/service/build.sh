#!/bin/sh
docker build -t disable .
docker run --restart always -d -p 15006:80 --name disable disable
docker start disable