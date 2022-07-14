docker rm $(docker ps -a -q)
docker build -t v3_ajax_container .
docker run -d -p 5000:5000 v3_ajax_container
