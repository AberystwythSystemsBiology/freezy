FROM ubuntu:18.04

MAINTAINER "Keiron O'Shea <keo7@aber.ac.uk>"

RUN apt-get update && apt-get install \
  -y curl python3 python3-venv gv

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN curl -sL https://deb.nodesource.com/setup_10.x | bash - \
    && apt-get install -y nodejs

RUN npm install yarn -g

WORKDIR /freezy
