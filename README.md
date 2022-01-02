# __OCR__

## __Setup environments__

- __Local Linux GNU & Drawin__

```shell
python3 -m venv ./env

source env/bin/activate

pip3 install -r ./requirements.txt

python3 server.py
```

- __Local Windows__

```ps
python -m venv ./env

.\venv\Scripts\activate

pip install -r requirements.txt

python server.py
```

- __Docker__

```shell
docker-compose up -d --build
```