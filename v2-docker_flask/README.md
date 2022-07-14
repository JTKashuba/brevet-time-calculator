# v2-docker_flask #

## Objectives ##

Tasks of this mini-project:

* Learn some new frameworks and technologies
    * `Docker` is used to deliver software in packages called "containers". More info found [here](https://docs.docker.com/)
    * `Flask` is a small and lightweight `Python` web framework that provides useful tools and features for creating web applications. More info found [here](https://flask.palletsprojects.com/en/2.1.x/)

* Write a `Dockerfile` to containerize the web app (see "Docker: Getting Started" section below for detail)

* Using `Flask`, implement the same "file checking" logic that was implemented in `v1-pageserver`
  * Go to the `/web/` directory in the repository. Read every line of the Dockerfile and the simple Flask app `app.py`

* Like in `v1-pageserver`, if a file `example.html` exists, respond with `HTTP/1.0 200 OK` and send that file's `HTML`

* If the file is forbidden or doesn't exist, transmit an error code in the header along with the appropriate page `HTML` in the body (done by creating error handlers)
  * Create error `HTML` files
    * `403.html` will display "File is forbidden!"
    * `404.html` will display "File not found!"

## User Instructions

* Save the v2-docker_flask repo locally

* From the command line, navigate to the directory `/v2-docker_flask/web`

* First, build the simple Flask app image with command ```docker build -t v2_docker_flask_container .```
  
* Next, run the Docker container using ```docker run -d -p 5000:5000 v2_docker_flask_container```

* You will now be able to view the app!
  * Enter URL `http://127.0.0.1:5000` in a web browser and check the output "Flask + Docker demo!"

## Docker Info

Reference [here](https://docs.docker.com/engine/reference/builder/)

* Command to get information about docker setup on your machine

  ```
  docker info
  ```

* List of docker containers running can be found using

  ```
  docker ps -a
  ```

* Remove containers using

  ```
  sudo docker rm <Container Name>
  ```

* To run docker container use

  ```
  docker run -h CONTAINER1 -i -t debian /bin/bash
  docker run -h CONTAINER1 -i -t ubuntu /bin/bash
  ```

  Here, -h is used to specify a container name, -t to start with tty, and -i means interactive. Note: second times will be quick because of caching

* Docker with networking

  ```
  docker run -h CONTAINER2 -i -t --net="bridge" debian /bin/bash
  ```

* When the containers are not running and when you're done, kill them using

  ```
  docker rm `docker ps --no-trunc -aq`
  ```

* Rename using

  ```
  docker rename name_v0 name_v1
  ```

* Start a container using

  ```
  docker start <container name>
  ```

* Stop a container using

  ```
  docker start <container name>
  ```

## Creating Images

* Create a Dockerfile. The name is case sensitive and it has to be "Dockerfile"

  ```
  vim Dockerfile
  ```

* FROM command specifies the base image you are going to use build your dockerfile and your new image. It's can an existing image, like ubuntu, alpine, debian, etc.

  ```
   FROM debian
  ```

* CMD command specifies all the commands you need to run

  ```
   CMD echo hello world
  ```

* Build the image with folder name ("." in this case)

  ```
   docker build .
  ```

* Output
  ```
  Sending build context to Docker daemon  2.048kB
  Step 1/2 : FROM alpine  
  latest: Pulling from library/alpine  
  ff3a5c916c92: Pull complete  
  Digest: sha256:7df6db5aa61ae9480f52f0b3a06a140ab98d427f86d8d5de0bedab9b8df6b1c0  
  Status: Downloaded newer image for alpine:latest  
  ---> 3fd9065eaf02  
  Step 2/2 : CMD ["echo hello world"]  
  ---> Running in 48cd3d25065d  
  Removing intermediate container 48cd3d25065d  
  ---> e2e741ea5f6f  
  Successfully built e2e741ea5f6f  
  ```

* Run the image using the image ID ("e2e741ea5f6f" in this case) and a test name of your choice

  ```
  docker run --name <test name> e2e741ea5f6f
  ```

* List images using

  ```
  sudo docker images
  ```

* Remove images using

  ```
  docker rmi <Image ID>
  ```

## Contact Info
[LinkedIn](https://www.linkedin.com/in/jtkashuba)

kashuba.jt@gmail.com