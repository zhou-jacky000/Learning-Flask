# 📘 Day 4 - Flask 的 Templates 與 Static 資料夾

---

## 🧠 為什麼需要 Templates？

之前我們的 `return` 都是直接回傳純文字字串：

```python
@app.route('/')
def home():
    return 'Hello, Flask!'
```

但實際開發網站時，我們會希望：

✅ 顯示 HTML  
✅ 支援變數動態內容  
✅ 有條件渲染、迴圈顯示列表內容等  

這就需要「模板引擎」來幫忙，Flask 預設使用 **Jinja2**。

---

## 📁 Flask 的預設資料夾結構

當 Flask 專案要使用模板與靜態資源時，請遵守下面結構：

```
project/
├── app.py
├── templates/
│   └── index.html
└── static/
    ├── css/
    ├── js/
    └── images/
```

---

## 📄 使用 Flask Templates：`render_template()`

### 建立一個 HTML 檔案：
📁 在 `templates/` 資料夾下新增 `index.html`：

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html>
<head>
    <title>首頁</title>
</head>
<body>
    <h1>你好，{{ name }}！</h1>
</body>
</html>
```

### 修改 `app.py` 使用模板：

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', name='Flask 學員')
```

---

## 🔍 {{ name }} 是什麼？

這是 **Jinja2** 的語法，可以讓你把後端變數放進 HTML 裡顯示。

---

## 🎨 Static 靜態檔案（CSS / JS / 圖片）

所有放在 `static/` 資料夾裡的檔案，都可以用網址 `/static/檔案路徑` 存取。

### 範例：加入 CSS 檔

建立 `static/css/style.css`：

```css
body {
    background-color: #f0f8ff;
    font-family: Arial;
}
```

然後在 `index.html` 裡加上：

```html
<link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
```

這樣你的 HTML 頁面就會變漂亮了！

---

## 🛠 自訂模板與靜態檔案位置（進階）

如果你不想用預設的 `templates` 和 `static` 資料夾名稱，可以自己指定：

```python
app = Flask(__name__, template_folder='my_templates', static_folder='assets')
```

這樣 Flask 就會到你指定的資料夾去找東西。