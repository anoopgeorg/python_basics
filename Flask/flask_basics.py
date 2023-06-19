from flask import Flask, request, render_template
import platform

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template('index.html')

@app.route("/dev")
def get_device():
    system_info = platform.uname()
    return("<h1>{}</h1>".format(system_info))

# Function for adding 2 numbers
def add(n1,n2):
    return n1 + n2

# Function for subtracting 2 numbers
def sub(n1,n2):
    return n1 - n2

# Function for dividing 2 numbers
def div(n1,n2):
    if n2 != 0:
        return n1 / n2
    else:
        return "Divide by Zero!"


@app.route("/calculate",methods=['POST'])
def calculator():
    if request.method == 'POST':
        ops = request.form['operation']
        num1 = int(request.form['number1'])
        num2 = int(request.form['number2'])
        if ops == 'add':
            res = add(num1,num2)
        if ops == 'sub':
            res = sub(num1,num2)
        if ops == 'div':
            res = div(num1,num2)
    return render_template('results.html',result = res)

@app.route('/redirect',methods=['POST'])
def redirect():
    return render_template('index.html')


if __name__=="__main__":
    app.run(host="0.0.0.0")
