# syntax=docker/dockerfile:1

# Base Python 3.8 image to build on
FROM python:3.8-slim-buster

# Example pip install
# Here, the package is installed from the source files,
# but this illustrates that we can easily run pip install in a container
# and then call python3 to run packages
COPY . /source_files
RUN pip3 install /source_files/
RUN rm -rf /source_files/

# Run the hello world module
CMD [ "python3", "-m" , "interview"]
