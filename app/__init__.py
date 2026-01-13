import flask
from flask import Flask

def create_app():
    app = Flask(__name__)
    if __name__ == "__main__":
        app.run(debug=True)
    return app