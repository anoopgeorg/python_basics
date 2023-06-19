from flask import Flask
from flask import request
import platform

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"

@app.route("/dev")
def get_device():
    system_info = platform.uname()
    return("<h1>{}</h1>".format(system_info))

@app.route('/input')
def input_value():
    data = request.args.get('i')
    return("<h3>Input provided is {}</h3>".format(data))

if __name__=="__main__":
    app.run(host="0.0.0.0")
