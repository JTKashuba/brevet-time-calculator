docker rm $(docker ps -a -q)
docker build -t v4_brevets_container .
docker run -d -p 5000:5000 v4_brevets_container