# __OCR__

## __Setup environments__

### __Prerequisites__

Required python version <= __`3.9.4`__, recommended 3.9.4

- __Linux GNU & WSL__

Requirements all package python:

```shell
sudo apt-get install python=3.9.4 python3-pip \
    python3-venv
```

- __Drawin__

On macOS, first install Xcode from the App Store or using [Brew](https://brew.sh/):

```shell
brew install python@3.9.4 tesseract
```

- __Windows__

Required python [Download python](https://www.python.org/downloads/) or using [Chocolatey](https://chocolatey.org/install) verion recommended 3.9.4 

```powershell
choco install python --version=3.9.4
```

if the previous python installation is unsatisfactory

```powershell
choco install python --version=3.9.4 --force
```

### __Linux GNU & Drawin__

```bash
python3 -m venv env

source env/bin/activate

pip3 install --upgrade pip

pip3 install -r ./requirements.txt
```

### __Windows__

```powershell
python -m venv ./env

Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted

env/Scripts/activate

python -m pip install --upgrade pip

pip install -r ./requirements.txt
```

### __Script__

- __Linux GNU & Drawin__ 

```bash
./scripts/activate.sh
```

- __Windows__

```powershell
powershell ./scripts/activate.ps1
```

### __Docker__

Requirement docker compose

```bash
docker-compose up -d --build
```

### __Run project__

- __Linux GNU & Drawin__ 

```bash
source ./env/bin/activate
python3 ./server.py
```

- __Windows__

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted
./env/Scripts/activate 
python ./server.py
```