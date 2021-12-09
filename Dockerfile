FROM python:latest

RUN apt-get update 

RUN apt-get -y install \
    tesseract-ocr \
    tesseract-ocr-jpn \
    libgl1-mesa-dev; 

RUN apt-get clean

WORKDIR /ocr

COPY . .

RUN sudo pip install --upgrade pip

RUN sudo pip install -r ./requirements.txt

CMD [ "python","server.py" ]