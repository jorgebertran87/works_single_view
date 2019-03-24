from python:3.7-alpine

RUN apk update \
    && apk add libpq postgresql-dev \
    && apk add build-base

RUN pip3 install click django djangorestframework psycopg2-binary

COPY . /usr/src/app

WORKDIR /usr/src/app

RUN ln -s core/infrastructure/api/drf/manage.py manage.py

EXPOSE 8990

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8990"]