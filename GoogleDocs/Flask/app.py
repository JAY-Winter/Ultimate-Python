# from flask import Flask, render_template, request
# from werkzeug.utils import secure_filename

# app = Flask(__name__)  # Flask 객체 생성

# @app.route('/upload')
# def renderFile() :
#     return render_template('upload.html')

# @app.route('/fileUpload', methods = ['GET', 'POST'])
# def uploadFile() :
#     if request.method == 'POST' :
#         f = request.files['file']

#         f.save(secure_filename(f.filename))
#         return 'uploads 디렉토리 -> 파일 업로드 성공'




# if __name__ == "__main__":  # 모듈이 실행 됨을 알림
#     app.run(host="0.0.0.0", port=5000, debug=True)  # 서버 실행, 파라미터로 debug 여부, port 설정 가능

from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
app = Flask(__name__)

@app.route('/')
def mainPage():
    
    return render_template('index.html')


# # 업로드 HTML 렌더링
# @app.route('/upload')
# def render_file():
#     return render_template('upload.html')

# 파일 업로드 처리
@app.route('/fileUpload', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        # 저장할 경로 + 파일명
        f.save(secure_filename(f.filename))
        return 'uploads 디렉토리 -> 파일 업로드 성공!'

@app.route('/questionBox')
def questionBox() :
    return render_template("questionBox.html")



if __name__ == '__main__':
    # 서버 실행
    app.run(debug = True)