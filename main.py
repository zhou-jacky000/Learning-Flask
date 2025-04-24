from flask import Flask

#初始化時傳入的 __name__ 參數，代表當前模組的名稱。
#是固定用法，這可以讓 Flask 知道在哪裡尋找資源。
app = Flask(__name__)

#Flask會利用route()裝飾器來告訴Flask什麼URL應該觸發我們的函數。
@app.route("/")

#該函數返回我們想要在用戶瀏覽器中顯示的消息。默認內容類型是 HTML，因此字符串中的 HTML 將由瀏覽器呈現，
#也一定是一個要執行的function，透過這樣子的設置，當你連接到’/'的時候，路由就知道要執行後面的function了。
def hello_world():
    return "<p>Hello, World!</p>"

# run是Flask內建的開發伺服器，在開發過程中可以通過run來快速啟動伺服器
# debug=True可以幫助我們在修改的時候可以快速地發現錯誤或自動重新加載
if __name__ == "__main__":
    app.run(debug=True)
