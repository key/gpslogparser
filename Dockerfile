FROM python:2.7

MAINTAINER Mitsukuni `key' Sato <mitsukuni.sato@gmail.com>
ADD . /data
WORKDIR /data
RUN pip install -r requirements.txt
CMD [ "python", "run.py" ]
