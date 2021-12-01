# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster
COPY . .
RUN pip3 install hello_world
CMD [ "python3", "-m" , "hello_world"]