# 📘 Day 6 重點：Flask 配置管理

---

## ❓ 為什麼要做配置管理？

當你的網站越做越大，就會遇到這些情況：

| 情境                     | 需要設定什麼？                     |
|--------------------------|------------------------------------|
| 要開 debug 嗎？          | `DEBUG = True`                   |
| 資料庫位置不同？          | `SQLALCHEMY_DATABASE_URI`         |
| session 加密用的 key？    | `SECRET_KEY`                     |
| 切換開發、測試、正式環境？| `ENV = 'development'`            |

這些設定就可以集中寫在 config 裡面，讓專案更好管理。

---

## ✅ 設定方式 1：直接在 `app.config` 設定

```python
from flask import Flask

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'mysecret'
```

---

## ✅ 設定方式 2：使用 `config.from_pyfile()`

### 建立一個 `config.py`：
```python
# config.py
DEBUG = True
SECRET_KEY = 'mysecret'
```

### 在 `app.py` 載入它：
```python
app = Flask(__name__)
app.config.from_pyfile('config.py')
```

---

## ✅ 設定方式 3：建立多組環境設定

### 建立 `config.py`：
```python
# config.py
class Config:
    SECRET_KEY = 'base_secret'

class DevConfig(Config):
    DEBUG = True
    ENV = 'development'

class ProdConfig(Config):
    DEBUG = False
    ENV = 'production'
```

### 在 `app.py` 指定載入哪一組：
```python
from flask import Flask
from config import DevConfig  # 換成 ProdConfig 就切到正式機設定

app = Flask(__name__)
app.config.from_object(DevConfig)
```

這樣就可以輕鬆切換不同環境，超好用！

---

## 🧠 Flask 常用設定總覽

| 設定項目                | 說明                                |
|-------------------------|-------------------------------------|
| `DEBUG`                | 是否啟用除錯模式                   |
| `SECRET_KEY`           | session / cookie 加密用            |
| `ENV`                  | 可設 `'development'` 或 `'production'` |
| `TESTING`              | 啟用測試模式                       |
| `UPLOAD_FOLDER`        | 上傳檔案儲存路徑                   |
| `SQLALCHEMY_DATABASE_URI` | 資料庫連線位址                   |