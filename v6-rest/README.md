# v6-rest

## Objectives ##

Tasks of this mini-project:

* Gain experience with `REST API`, also known as `RESTful API` (technical documentation can be found [here](https://restfulapi.net/rest-api-design-tutorial-with-example/))

* Design a `RESTful` service to expose specific information from the `MongoDB` database at appropriately named URL's (used an example/template in the `DockerRestAPI` directory to create the following three basic APIs):
    * `http://<host:port>/listAll` returns all open and close times in the database
    * `http://<host:port>/listOpenOnly` returns open times only
    * `http://<host:port>/listCloseOnly` returns close times only

* Design two different representations: one in csv and one in json. JSON is our default representation for the above three basic APIs.
    * `http://<host:port>/listAll/csv` returns all open and close times, and in CSV format
    * `http://<host:port>/listOpenOnly/csv` returns open times only, and in CSV format
    * `http://<host:port>/listCloseOnly/csv` returns close times only, and in CSV format

    * `http://<host:port>/listAll/json` returns all open and close times, and in JSON format
    * `http://<host:port>/listOpenOnly/json` returns open times only, and in JSON format
    * `http://<host:port>/listCloseOnly/json` returns close times only, and in JSON format

    NOTE: `<host:port>` is `localhost:5001` unless you went around tinkering with the source code

* Design consumer programs in `jQuery` to use the service that's exposed. `website` inside the `DockerRestAPI` directory is an example that uses `PHP`. NOTE: the consumer program is in a different container like the example in `DockerRestAPI`

## User Instructions ##

* Save the v6-rest repo locally

* From the command line, navigate to the directory `/v6-rest/DockerRestAPI`

* Build and run the Docker container by activating the `docker-compose.yml` file with the following command:
```
docker-compose up
```

* You will now be able to view the app! From a browser, enter the following URL to view the landing page for the brevet time calculator web app `localhost:5001`
    * If you want to view *only the database info*, from a browser enter the following URL `localhost:5000`

NOTE: the port numbers are set (and can be changed) in `docker-compose.yml`

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

## How To Continue Improving ##

Future functionality (started working on this, saved it in `safekeep.py` but pushed this repo to build/run a container sans the beginnings of future functionality code): 
* Add a query parameter to get the "top-k" open and close times. For examples, see below
    * `http://<host:port>/listOpenOnly/csv?top=3` should return top 3 open times only (in ascending order) in CSV format
    * `http://<host:port>/listOpenOnly/json?top=5` should return top 5 open times only (in ascending order) in JSON format
    * `http://<host:port>/listCloseOnly/csv?top=6` should return top 5 close times only (in ascending order) in CSV format
    * `http://<host:port>/listCloseOnly/json?top=4` should return top 4 close times only (in ascending order) in JSON format

## Authors ##

Initial version by R Durairajan and M Young; revised by JT Kashuba

## Contact Info
[LinkedIn](https://www.linkedin.com/in/jtkashuba)

kashuba.jt@gmail.com