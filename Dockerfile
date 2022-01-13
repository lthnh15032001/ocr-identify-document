FROM python:3.9.0

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

CMD [ "./env/bin/python3","server.py" ]