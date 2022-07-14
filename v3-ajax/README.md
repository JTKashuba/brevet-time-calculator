# v3-ajax #

Vocabulary anagrams game for primary school English language learners (ELL)

## Objectives ##

Tasks of this mini-project:

* Learn some new frameworks and technologies
    * `AJAX` is a set of web development techniques that uses various web technologies on the client-side to create asynchronous web applications. With `AJAX`, web applications can send and retrieve data from a server asynchronously without interfering with the display and behaviour of the existing page

* Enhance the user experience
    * Replace the `form` interaction in `flask_vocab.py` with `AJAX` interaction on each keystroke using `flask_minijax.py`
        * `flask_minijax.py` and `templates/minijax.html` are a tiny example of using jQuery with Flask for an AJAX application

* Get more familiar with Flask by running `flask_vocab.py` and `flask_minijax.py` separately
    * `flask_vocab.py` and the template `vocab.html` are a "skeleton" version of an anagram game. They use conventional interaction through a `form`, interacting only when the user submits the `form`

## Overview ##

A simple anagram game designed for English-language learning students in elementary and middle school. Students are presented with a list of vocabulary words (taken from a text file) and an anagram. The anagram is a jumble of some number of vocabulary words, randomly chosen. Students attempt to type words that can be created from the jumble. When a matching word is typed, it is added to a list of solved words

The vocabulary word list is fixed for one invocation of the server, so multiple students connected to the same server will see the same vocabulary list but may  have different anagrams

## User Instructions

* Save the v3-ajax repo locally

* From the command line, navigate to the directory `/v3-ajax/vocab`

* Build and run the Docker container with command `./run.sh`

NOTE: if you are unable to use `./run.sh` "out of the box", it should be an easy fix—use command `sudo chmod 777 run.sh`

* You will now be able to view the app! From a browser, enter the following URL `localhost:5000`

## Docker Info

* To build and run a docker container via Dockerfile manually (without using `./run.sh`):
    * Navigate to the directory in which the Dockerfile is located
    * First use command `docker build -t v3_ajax_container .`
    * Then use command `docker run -d -p 5000:5000 v3_ajax_container`

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

If you aren't familiar with Dockerfile or bash scripts, make sure you use the next command from inside the `/v3-ajax/vocab` directory in order to avoid any start-up issues

* Once you've deleted previous containers and images, build and run your new docker container (run.sh is included in the repo) with command 
```
./run.sh
```

* You will now be able to view the app! From a browser, enter the following URL: `localhost:5000` 

## Authors ##

Initial version by M Young; Docker version added by R Durairajan; revised by JT Kashuba

## Contact Info
[LinkedIn](https://www.linkedin.com/in/jtkashuba)

kashuba.jt@gmail.com