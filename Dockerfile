# Below are the dependencies required for installing the common combination of numpy, scipy, pandas and matplotlib 
# in an Alpine based Docker image.

FROM alpine:3.7

RUN echo "http://dl-cdn.alpinelinux.org/alpine/v3.7/community" >> /etc/apk/repositories

RUN apk --no-cache --update-cache add libgfortran 

RUN apk --no-cache --update-cache add gcc gfortran python python3 python-dev python3-dev py-pip build-base wget freetype-dev libpng-dev  openblas-dev libpq postgresql-dev

RUN ln -s /usr/include/locale.h /usr/include/xlocale.h

RUN apk update && apk add libpq postgresql-dev
    

RUN pip3 install click django djangorestframework psycopg2-binary numpy rest-pandas

# I add a new line because rest-pandas 
# takes more than 15 minutes to be installed...
RUN pip3 install coverage

COPY . /usr/src/app

WORKDIR /usr/src/app

RUN ln -s core/infrastructure/api/drf/manage.py manage.py

EXPOSE 8990