# 📘 Day 5 重點：Jinja2 模板語法與應用

---

## 🧠 Jinja2 語法基本介紹

| 類型       | 語法               | 用途                     |
|------------|--------------------|--------------------------|
| 表示式     | `{{ variable }}`   | 顯示變數資料             |
| 控制語句   | `{% statement %}`  | 用於 `if`、`for`、`include` 等 |

---

## ✅ 1. if 判斷式

### app.py：
```python
@app.route('/score/<int:value>')
def score(value):
    return render_template('score.html', score=value)
```

### score.html：
```html
<h1>成績評語</h1>
<p>你的分數是 {{ score }}</p>

{% if score >= 90 %}
    <p>🌟 優秀！</p>
{% elif score >= 60 %}
    <p>😊 及格，加油！</p>
{% else %}
    <p>😢 不及格，再接再厲！</p>
{% endif %}
```

---

## 🔁 2. for 迴圈

### app.py：
```python
@app.route('/fruits')
def fruits():
    fruit_list = ['🍎 蘋果', '🍌 香蕉', '🍇 葡萄']
    return render_template('fruits.html', fruits=fruit_list)
```

### fruits.html：
```html
<h1>水果清單</h1>
<ul>
    {% for fruit in fruits %}
        <li>{{ fruit }}</li>
    {% endfor %}
</ul>
```

---

## 🧩 3. 模板繼承（Template Inheritance）

讓多個頁面共用一個版型！（例如 header/footer）

### 📄 templates/base.html：
```html
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}我的網站{% endblock %}</title>
</head>
<body>
    <header><h1>網站標頭</h1></header>
    <main>
        {% block content %}{% endblock %}
    </main>
    <footer><p>網站底部</p></footer>
</body>
</html>
```

### 📄 templates/index.html：
```html
{% extends "base.html" %}

{% block title %}首頁{% endblock %}

{% block content %}
    <p>這是首頁的內容。</p>
{% endblock %}
```

---

這樣就能用 `base.html` 當模板，讓所有頁面看起來一致，並且只需修改一次版型即可應用到所有頁面！