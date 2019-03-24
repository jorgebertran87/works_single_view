from python:3.7-alpine

RUN pip3 install click django djangorestframework

COPY . /usr/src/app

WORKDIR /usr/src/app
