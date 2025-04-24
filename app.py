from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', name='Flask 學員')

@app.route('/about')
def about():
    return render_template('about.html', name='123Flask 學員')

@app.route('/user/<name>/<int:value>')
def age(name,value):
    return render_template('age.html', age=value,name=name)


@app.route('/fruits')
def fruits():
    fruit_list = ['🍎 蘋果', '🍌 香蕉', '🍇 葡萄']
    return render_template('fruits.html', fruits=fruit_list)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
