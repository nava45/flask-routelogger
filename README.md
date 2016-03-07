# flask-routelogger
Flask Extension to log all meta request - response fields into the configured storage layer

### To Install this extension:
`python setup.py install`

### Ok, How to run and test this extenstion for your flask application?

I hope you installed this extension in your virtual environment.

> You can take a look at the file `test_flask_app.py`, here we have configured this flask-routelogger with the minimal flask application

run this minimal flask app,

`python test_flask_app.py`

Once it starts running,

just hit the endpoint `http://localhost:5000/`

If you have your elastic search setup proper in your localhost, you could see in the index few structured documents will be created.


