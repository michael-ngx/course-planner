# uofthacks2023

## Set up

Install the requirements for the backend by first creating a virtual environment in the backend directory:

```
cd backend
python -m venv venv
```

Set up Flask environment variables:

Unix Bash (Linux, Mac, etc.):
```
$ export FLASK_APP=hello
$ flask run
```
Windows CMD:
```
> set FLASK_APP=hello
> flask run
```
Windows PowerShell:
```
> $env:FLASK_APP = "hello"
> flask run
```

Then install the dependencies:
```
pip install flask flask-cors
```

## Running the project

Start the backend server using the following command (currently in backend directory):

```
python app.py
```

Start the frontend using [http-server](https://www.npmjs.com/package/http-server):

```
http-server
```

Navigate using a browser to the address the frontend is hosted at. This is `http://localhost:8080` by default.