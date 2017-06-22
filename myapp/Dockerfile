FROM ubuntu:16.04

RUN apt-get update -y
RUN apt-get install python-flask -y

ADD . /webapp

EXPOSE 8000

CMD python /webapp/app.py
