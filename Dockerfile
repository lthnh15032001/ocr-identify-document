FROM python:latest

RUN apt-get update 

RUN apt-get -y install \
    tesseract-ocr \
    tesseract-ocr-jpn \
    libgl1-mesa-dev; 

RUN apt-get clean

WORKDIR /ocr

COPY . .

RUN python3 -m venv /ocr/env

RUN source -m /ocr/env/bin/activate

RUN pip install --upgrade pip

RUN pip install -r ./requirements.txt

CMD [ "python","server.py" ]