FROM python:latest

RUN apt-get update 

RUN apt-get -y install \
    tesseract-ocr \
    tesseract-ocr-jpn \
    libgl1-mesa-dev; 

RUN apt-get clean

WORKDIR /ocr

COPY . .

RUN python3 -m venv ./env

RUN ./env/bin/pip3 install --upgrade pip

RUN ./env/bin/pip3 install -r ./requirements.txt

RUN ./env/bin/pip3 install --upgrade https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-1.0.0-py3-none-any.whl

CMD [ "./env/bin/python3","server.py" ]