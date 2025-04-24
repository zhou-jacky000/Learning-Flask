from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, Flask!'

@app.route('/about')
def about():
    return 'Home Page'

if __name__ == '__main__':
    app.run(debug=True)
