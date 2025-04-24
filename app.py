from flask import Flask,request

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, Flask!'

@app.route('/about')
def about():
    return 'Home Page'

@app.route('/form', methods=['GET', 'POST'])
def f():
    if request.method == 'POST':
        return '這是 POST'
    else:
        return '這是 GET'


@app.route('/hello/<name>')
def say_hello(name):
    return f'你好，{name}！'


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
