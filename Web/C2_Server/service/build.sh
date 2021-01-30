sudo docker build -t frontier .
sudo docker run --name frontier \
  -d \
  -v ${PWD}/default-pages:/usr/share/nginx/html/default \
  -v ${PWD}/malware-home-pages:/usr/share/nginx/html/malwary \
  -p=192.168.75.140:13008:13008 --restart always frontier
docker ps -f name=frontier