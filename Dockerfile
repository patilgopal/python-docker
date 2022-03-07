# syntax=docker/dockerfile:1

FROM buildpack-deps:bullseye

COPY . .

RUN apt-get update

RUN apt-get install iputils-ping -y

CMD [ "python3", "checkLatency.py"]