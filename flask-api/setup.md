To run the flask api:

Create a python virtual environment

```
python -m venv venv
```


Activate the venv
```
./venv/Scripts/Activate.ps1
```


Make sure your IDE interpreter is configured to use the virtual environment python interpreter.

Next, install the required packages to the virtual environment.

```
pip install -r requirements.txt
```

Finally you can run the api in development mode and copy and pasting the commands below.
Subsequent runs can be done with 'flask run'

```
$env:FLASK_APP = "api"
$env:FLASK_DEBUG = "1"
$env:FLASK_ENV = "development"
flask run
```

