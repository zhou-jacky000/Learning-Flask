import os
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'uploads'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# 建立上傳資料夾
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['myfile']
        if file:
            filename = secure_filename(file.filename)  # 安全處理檔名
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return f'檔案 {filename} 上傳成功！'
    return render_template('upload.html')

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
