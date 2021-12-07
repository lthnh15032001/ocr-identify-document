FROM python:latest

RUN apt-get update 

RUN apt-get -y install \
    tesseract-ocr \
    tesseract-ocr-jpn \
    libgl1-mesa-dev; 

WORKDIR /ocr

COPY . .

RUN apt-get clean

RUN pip install --upgrade pip

RUN pip install -r ./requirements.txt

CMD [ "python","server.py" ]