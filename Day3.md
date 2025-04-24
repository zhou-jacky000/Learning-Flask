# 📘 Day 3 - Flask 快速啟動教學

今天會帶你快速理解 Flask 最常用的幾個基本操作：

- `app.run()` 的參數
- `@app.route()` 設定路由
- 支援不同的 HTTP 方法（GET / POST）

---

## 🧱 1. `app.run()` 的參數說明

我們常常看到這樣的啟動方式：

```python
if __name__ == '__main__':
    app.run(debug=True)
```

🔍 `app.run()` 參數常見說明：

| 參數名稱 | 說明                                                                 |
|----------|----------------------------------------------------------------------|
| `host`   | 預設是 `127.0.0.1`，設為 `'0.0.0.0'` 可讓區網內其他電腦也能連線       |
| `port`   | 預設是 `5000`，你可以改成其他數字                                     |
| `debug`  | 設為 `True` 時，程式變動會自動重新載入，方便開發                       |

📌 例如：

```python
app.run(host='0.0.0.0', port=8080, debug=True)
```

---

## 🔗 2. `@app.route()` - 註冊路由（URL）

Flask 使用 `@app.route()` 來告訴伺服器：當使用者訪問某個網址時，該執行哪段函數。

```python
@app.route('/')
def home():
    return '這是首頁'

@app.route('/about')
def about():
    return '這是關於頁面'
```

👉 當你開啟 [http://localhost:5000/](http://localhost:5000/) 時，會執行 `home()`  
👉 開啟 [http://localhost:5000/about](http://localhost:5000/about)，會執行 `about()`

---

## 🔄 3. 支援不同的 HTTP 方法（GET / POST）

預設情況下，Flask 路由只接受 `GET` 請求。  
如果你要接收 `POST`，就要這樣寫：

```python
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        return '這是 POST'
    else:
        return '這是 GET'
```

✅ 請先加這行 import：

```python
from flask import request
```

這樣你就可以根據不同的請求方法做出不同行為（像處理表單、上傳檔案等）。


