FROM python:3.9.4

WORKDIR /ocr

COPY . .

RUN python3 -m venv ./env

RUN ./env/bin/pip3 install --upgrade pip

RUN ./env/bin/pip3 install -r ./requirements.txt

CMD [ "./env/bin/python3","server.py" ]