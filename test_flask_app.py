from  flask import Flask
from flask_routelogger import RouteLogger

app = Flask(__name__)
app.config.update(EXCLUDE_ROUTES = ('/',))

rapp = RouteLogger(app, log_everything=True)



@app.route('/')
def test():
    #raise "TTT"
    return "hai"


if __name__ == '__main__':
    app.run()
