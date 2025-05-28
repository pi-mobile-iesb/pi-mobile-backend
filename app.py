from flask import  Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

@app.route("/", methods=["GET"])
def hello_world():
    return {"message": "Hello, World!"}  


if '__name__' == '__main__':
    app.run()