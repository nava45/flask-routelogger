# flask-routelogger
Flask Extension to log all meta request - response fields into the configured storage layer

### Description

This extension enables Logging of the each configured request and responses  of well structured meta-information to your backend for your flask based web application.

This is extremely configurable for the custom backend storage to store all the logs. Since, the storage module implemented in modular way.

Currently v1.0 supports for the elastic search as full fledged backend. Also, the flask application route endpoints can be configured to add or remove from logging activity as part of your web application configuration.

### To Install this extension:
`python setup.py install`

### Ok, How to run and test this extenstion for your flask application?

I hope you installed this extension in your virtual environment.

> You can take a look at the file `flask_app_example.py`, here we have configured this flask-routelogger with the minimal flask application

run this minimal flask app,

`python flask_app_example.py`

Once it starts running,

just hit the endpoint `http://localhost:5000/`

If you have your elastic search setup proper in your localhost, you could see in the index few structured documents will be created.

### Config_params:

`INCLUDE_ROUTES`(`list`) = The logging facility will be enabled to the routes which are availabe here
`EXCLUDE_ROUTES`(`list`) = The logging facility will be excluded to the routes which are availabe here
`log_everything`(`bool`) = Top level bool param to decide to log everything or only specically configured endpoints


