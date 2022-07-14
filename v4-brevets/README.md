# v4-brevets

## Objectives ##

Tasks of this mini-project:

* Create the foundation for a web app to calculate brevet control times
    * Utilize concepts that were applied in `v1-pageserver`, `v2-docker_flask`, and `v3-ajax`
    * Plan to improve upon this foundation in the future with two more mini-projects (implementing `MongoDB` and `REST API` functionalities)

* Learn some new frameworks and technologies 
    * `nosetests` is an automated testing suite. More info found [here](https://nose.readthedocs.io/en/latest/)
    * `arrow` is a `Python` module to format date/time according to ISO8601 date/time standard. More info found [here](https://arrow.readthedocs.io/en/latest/)

* Get more familiar with web app development tools like `Docker`, `Flask`, and `AJAX`

## Overview ##

* This program is a functioning calculator for randonneurs (long distance cyclists) to schedule a "brevet" (a long race w/ control points which individuals have a certain amount of time to reach without being disqualified) and determine when the open and close times for control points of their choosing

* The nosetests testing suite checks many specific instances of control points open/close times that adhere to a strict ruleset. The specific things they are checking are documented in their corresponding docstrings. More info on how to run the test suite below in "User Instructions"

* More info on official acp brevet calculations found [here](https://rusa.org/pages/acp-brevet-control-times-calculator), and additional info and rules for riders can be found [here](https://rusa.org/pages/rulesForRiders)

## User Instructions

* Save the v4-brevets repo locally

* From the command line, navigate to the directory `/v4-brevets/brevets`

* Build and run the Docker container with command `./run.sh`

NOTE: if you are unable to use `./run.sh` "out of the box", it should be an easy fix—use command `sudo chmod 777 run.sh`

* You will now be able to view the app! From a browser, enter the following URL `localhost:5000`

* To run nosetests, use command 
```
docker exec -it <container id> nosetests --tests=<filename.py>
```

* The nosetests test suite for the v4-brevets web app is `test_open_and_close_times.py`

## Docker Info

* To build and run a docker container via Dockerfile manually (without using `./run.sh`):
    * Navigate to the directory in which the Dockerfile is located
    * First use command `docker build -t v4_brevets_container .`
    * Then use command `docker run -d -p 5000:5000 v4_brevets_container`

* List of docker containers running on your machine can be found with command 
```
docker ps -a
```

* If a container is running and you want to delete it, first copy the container id from the previous command and then use the following commands in order:

```
docker kill <container_id>
docker rm <container_id>
docker images
docker rmi <image_id>
```

If you aren't familiar with Dockerfile or bash scripts, make sure you use the next command from inside the `/v4-brevets/brevets` directory in order to avoid any start-up issues.

* Once you've deleted previous containers and images, build and run your new docker container (run.sh is included in the repo) with command 
```
./run.sh
```

* You will now be able to view the app! From a browser, enter the following URL: `localhost:5000` 

## Authors ##

Initial version by M Young; revised by JT Kashuba

## Contact Info
[LinkedIn](https://www.linkedin.com/in/jtkashuba)

kashuba.jt@gmail.com