# v5-mongo

## Objectives ##

Tasks of this mini-project:

* Learn some new frameworks and technologies
    * `MongoDB` is a `NoSQL` database program which uses `JSON`-like documents. More general info [here](https://www.mongodb.com/) and technical man pages can be found [here](https://www.mongodb.com/docs/manual/reference/program/mongod/)
    * `docker compose` "is a tool for defining and running multi-container Docker applications. With Compose, you use a YAML file to configure your application’s services. Then, with a single command, you create and start all the services from your configuration." More info found [here](https://docs.docker.com/compose/)

* Build onto `v4-brevets` by adding `MongoDB` database functionality
    * Create two buttons ("Submit" and "Display") on the landing page where we have control times
    * On clicking the "Submit" button, the control times should be entered into the database
    * On clicking the "Display" button, the browser should display a new page with entries from the database

* Write a `docker-compose.yml` file to configure the brevets web app with a MongoDB database

* Handle error cases appropriately. For example:
    * "Submit" button
        * Returns an error if there are no control times to submit to the database
        * On-click only sends the populated control open/close times to the database *once* (i.e.—if a user accidentally clicks "Submit" multiple times, we don't want to keep updating the database with unnecessary repeats)
    * "Display" button
        * Does not display old database information. We don't want a database to be maintained between sessions, so it must be cleared (i.e.—if a user refreshes the page, we want them to be able to create a new database)
        * *However*—if we *do* want to maintain the database across sessions, this can be changed very easily. line 37 in `flask_brevets.py` reads `db.controlPoints.drop()`. This command is deleting the previous database entries. Simply remove or comment out this line to maintain the database between sessions 

## User Instructions ##

* Save the v5-mongo repo locally

* From the command line, navigate to the directory `/v5-mongo/DockerMongo`

* Build and run the Docker container with the following command:
```
docker-compose up
```

* After activating the docker-compose.yml file with `docker-compose up`, you will now be able to view the app! From a browser, enter the following URL `localhost:5000`

* To end the process, use command `ctrl-C`

* To clear the containers off your local machine, use the following commands:
```
docker-compose stop
docker-compose down
```

* To see changes reflected in the browser (e.g., if/when you want to build a different web app container), use the following commands:
```
docker images
docker rmi <IMAGE ID>
```

## Authors ##

Initial version by M Young; revised by JT Kashuba

## Contact Info
[LinkedIn](https://www.linkedin.com/in/jtkashuba)

kashuba.jt@gmail.com