FROM python:3.8.10

LABEL MAINTAINER="ndh, lvt, bkd"

RUN apt-get update -y

RUN apt-get -y install python3-pip

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y

RUN apt-get clean

RUN mkdir /app

COPY . /app

WORKDIR /app

# RUN python3 -m venv ./env

RUN pip3 install --upgrade pip

# RUN ./env/bin/pip3 install -r ./requirements.txt

# CMD [ "./env/bin/python3","server.py" ]

RUN pip3 install -r requirements.txt