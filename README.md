# python-interview
Python Interview Code

## How to build
You will find the relevant interview files in the `/interview/` folder.\
The python files have been made into a package that can be run with:\
`python3 -m interview`\
\
This will run all tests at once.

### Optional: Docker
To illustrate how Docker can be used to run a python environment, a `Dockerfile` has been included.\
This will build an image containing Python 3.8 and an install of the `interview` package.\
The container will automatically run the module at startup and will display the results of the tests.\
\
Docker can be installed on a Windows machine via Docker Desktop:\
https://www.docker.com/get-started\
\
To build the container, from the root folder, run:\
`docker build --tag python_interview .`\
\
To start the containter, run:\
`docker run python_interview`
