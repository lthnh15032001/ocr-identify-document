# __OCR__

## __Setup environments__

### __Prerequisites__

- __Local Linux GNU & WSL__

Requirements all package python:

```shell
sudo apt-get install python python3-pip \
    python3-venv tesseract
```

- __Drawin__

On macOS, first install Xcode from the App Store or using [Brew](https://brew.sh/):

```shell
brew install python3 tesseract
```

- __Windows__

Required python 

```powershell

```

### __Local Linux GNU & Drawin__

```bash
python3 -m venv env

source env/bin/activate

pip3 install --upgrade pip

pip3 install -r ./requirements.txt
```

### __Local Windows__

```powershell
python -m venv ./env

Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted

env/Scripts/activate

python -m pip install --upgrade pip

pip install -r requirements.txt
```

### __Script__

Requied system Linux GNU & Drawin 

```bash
./scripts/activate.sh
```

### __Docker__

```bash
docker-compose up -d --build
```

### __Run project__

```bash

```