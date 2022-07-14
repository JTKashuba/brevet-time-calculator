# v1-pageserver #

## Objectives ##

Tasks of this mini-project:

* Learn some new frameworks and technologies
  * A `Makefile` is a utility used as a set of rules to determine which parts of a program need to recompile, and issues command to recompile them. GNU make man page found [here](https://www.gnu.org/software/make/manual/make.html) and a more beginner-friendly tutorial [here] (https://www.cs.colby.edu/maxwell/courses/tutorials/maketutor/)
  * Extend a tiny `web server` in `Python`, to check understanding of `basic web architecture`
  * The `Linux` `curl` command can be used for `automated testing`. curl man page [here](https://www.mit.edu/afs.new/sipb/user/ssen/src/curl-7.11.1/docs/curl.html) and a more beginner-friendly tutorial [here](https://phoenixnap.com/kb/curl-command)
  * `Bash` scripting. Cheat sheet [here](https://devhints.io/bash)
  * `HTTP`, `TCP`, `UDP`, and `IP` protocols

* If URL ends with a file name that exists: respond with `HTTP/1.0 200 OK` and send that file `HTML` or `CSS`
  * For example, `example.html` or `example.css`. i.e., if `path/to/example.html` is in document path (from DOCROOT)
  * The only HTML/CSS files that are included, and thus the only ones that will work "out-of-the-box" are `trivia.html` and `trivia.css` 

* If `example.html` is not in current directory: respond with `HTTP/1.0 404 Not Found`

* If a page starts with `~`, `//`, or `..`: respond with `HTTP/1.0 403 Forbidden`
  * For example, `localhost:5000/..example.html` or `/~example.html` gives 403 Forbidden

* Test the server manually in the browser

* Use `Bash` scripting and `curl` to create and utilize an automated test suite

## User Instructions

* Save the v1-pageserver repo locally

* From the command line, navigate to the directory `/v1-pageserver`

* Execute the Makefile with command ```make run```

* You will now be able to test the pageserver! From a browser, enter the following URL: `127.0.0.1:5000/trivia.html` 

* Manually test different URL's in your browser now, while the server is running in a background process

* Use the automated test suite (README in the `/tests/` directory and comments inside `tests.sh`) 
  * First, open a different terminal window and navigate to `/v1-pageserver`
  * Next, run the test suite script with command `./tests/tests.sh http://127.0.0.1:5000/`

* When you're finished, stop the server with command ```make stop```

* Remove unwanted files with command ```make clean```

## What do I need?  Where will it work? ##

* Designed for Unix, mostly interoperable on Linux (Ubuntu) or macOS. May also work on Windows or a Linux virtual machine, but no promises

* Requires Python version 3.4 or higher

* Designed to work in "user mode" (unprivileged), therefore using a port number above 1000 (rather than port 80 that a privileged web server would use)


## Contact Info
[LinkedIn](https://www.linkedin.com/in/jtkashuba)

kashuba.jt@gmail.com
