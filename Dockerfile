FROM python:3.6.1
MAINTAINER Gajovski Maxime <gajovski.maxime@gmail.com>

ENV APP_NAME="cafe"

RUN mkdir -p /usr/src/$APP_NAME
WORKDIR /usr/src/$APP_NAME

ADD ./requirements.txt /usr/src/$APP_NAME/requirements.txt

RUN pip install -r requirements.txt

ADD . /usr/src/$APP_NAME

RUN echo 'alias pmr="python manage.py recreate_database"' >> /root/.bashrc

CMD python manage.py runserver -h 0.0.0.0