from flask import Flask,render_template

app = Flask(__name__)

app.config['debug'] = True
app.config['SECRET_KEY'] =  '1234567890'
app.config['env'] = 'development'
app.config['TESTING'] = True    

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
    fruit_list = [
        {'name': '🍎 蘋果', 'price': 30},
        {'name': '🍌 香蕉', 'price': 20},
        {'name': '🍇 葡萄', 'price': 50}
    ]
    return render_template('fruits.html', fruits=fruit_list)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
