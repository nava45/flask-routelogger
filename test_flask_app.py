from  flask import Flask
from flask_routelogger import RouteLogger

app = Flask(__name__)
app.config.update(EXCLUDE_ROUTES = ('/',))

# Add Flask-RouteLogger config in your flask application
rapp = RouteLogger(app, log_everything=True)



@app.route('/')
def test():
    return "Welcome to flask-routerlogger testing!!"


if __name__ == '__main__':
    app.run()
