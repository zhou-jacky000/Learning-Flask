# 📘 Day 2 - Flask 的簡單開發環境設定

今天我們要準備一個乾淨的 Flask 開發環境，並建立第一個可以跑的 Flask App！

---

## 🔧 1. 安裝 Python（如果你還沒裝）

建議使用 Python 3.9 以上版本  
Windows / macOS / Linux 都支援

可以在終端機或命令提示字元中輸入確認：

```bash
python --version
```

---

## 📁 2. 建立虛擬環境（建議一定要用！）

虛擬環境可以讓你在不同專案中使用不同版本的套件，避免衝突。

```bash
# 建立虛擬環境（venv 是資料夾名稱，可自訂）
python -m venv venv

# 啟用虛擬環境
# Windows：
venv\Scripts\activate

# macOS/Linux：
source venv/bin/activate
```

啟用後，指令列前面會出現 `(venv)`，表示虛擬環境已啟動。

---

## 📦 3. 安裝 Flask

在虛擬環境中執行：

```bash
pip install flask
```

確認是否安裝成功：

```bash
python -m flask --version
```

---

## 📄 4. 建立你的第一個 Flask App

新建一個檔案，例如 `app.py`，內容如下：

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, Flask!'

if __name__ == '__main__':
    app.run(debug=True)
```

---

## 🚀 5. 啟動 Flask 伺服器

執行以下指令：

```bash
python app.py
```

你會看到：

```text
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

打開瀏覽器 → 前往 [http://127.0.0.1:5000/](http://127.0.0.1:5000/)  
看到「Hello, Flask!」就代表你成功了 🎉
