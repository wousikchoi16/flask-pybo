# 질문목록조회와 질문상세조회기능 구현

from flask import Blueprint, url_for

from werkzeug.utils import redirect

# Blueprint객체생성(이름,모듈명,URL프리픽스)
bp = Blueprint('main',__name__,url_prefix='/')

@bp.route('/hello')
def hello_pybo():
    return 'Hello,Pybo!!!'

# 질문목록 조회기능
@bp.route('/')
def index():
    return redirect(url_for('question._list')) #등록된블루프린트이름.등록된함수