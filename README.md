## Installation Required

```
python >= 3.6.9
Virtualenv
```

If all the above requirements are fullfilled

## Run local server

Activating/Running Virtual Environment
```
$ git clone https://github.com/knight-byte/Python-Compiler
$ cd Python-Compiler
$ virtualenv .

#linux 
source bin/activate 

#windows
source bin/activate

```

Installing all dependencies
```
pip install -r requirements.txt 
```

Sync and Running the local server
```
python manage.py migrate
python manage.py runserver
```

Deactivating the Virtual Environment
```
Deactivate
```
