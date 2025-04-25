# 📘 Day 7 重點：檔案上傳與管理

---

## 建立 HTML 上傳表單  
處理上傳的檔案  
儲存到指定資料夾  
限制檔案類型 & 檔名安全處理  

---

## ✅ 1. 預備設定

### app.py：
```python
import os
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'uploads'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# 建立上傳資料夾
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
```

---

## ✅ 2. 建立上傳表單 HTML

### templates/upload.html：
```html
<h1>上傳檔案</h1>
<form method="POST" enctype="multipart/form-data">
    <input type="file" name="myfile">
    <input type="submit" value="上傳">
</form>
```

---

## ✅ 3. Flask 接收檔案並儲存

### app.py 加上路由：
```python
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['myfile']
        if file:
            filename = secure_filename(file.filename)  # 安全處理檔名
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return f'檔案 {filename} 上傳成功！'
    return render_template('upload.html')
```

✅ `secure_filename()` 是 Flask 提供的方法，可避免中文亂碼/路徑注入等問題。

---

## ✅ 4. 限制檔案類型（進階）

### 定義允許的檔案類型：
```python
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
```

### 搭配使用：
```python
if file and allowed_file(file.filename):
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
```

---

## ✅ 5. 顯示上傳的檔案列表（進階）

### app.py：
```python
@app.route('/files')
def list_files():
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('files.html', files=files)
```

### templates/files.html：
```html
<h2>已上傳檔案</h2>
<ul>
  {% for f in files %}
    <li>{{ f }}</li>
  {% endfor %}
</ul>
```

---

這樣就完成了檔案上傳功能，並能顯示已上傳的檔案列表！如果需要進一步的功能，例如刪除檔案或下載檔案，請告訴我！