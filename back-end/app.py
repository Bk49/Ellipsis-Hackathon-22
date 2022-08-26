from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)


api = Api(app)
# api.add_resource()

@app.route("/")
def root_page():
    return "Hello world!"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001, debug=True)