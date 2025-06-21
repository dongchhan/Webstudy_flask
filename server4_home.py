# Agenda: 홈페이지 구현

from flask import Flask 
import random 

app = Flask(__name__)

topics = [
    {'id': 1, 'title': 'html', 'body': 'html is ...'},
    {'id': 2, 'title': 'css', 'body': 'html is ...'},
    {'id': 3, 'title': 'javascript', 'body': 'javascript is ...'},
]

@app.route('/')
def index():  # 홈페이지 구성
    liTags = ''
    for topic in topics:
        liTags = liTags + f'<li><a href="/read/{topic["id"]}/">{topic["title"]}</a></li>'
        '''
        liTags 결과(줄바꿈없음): 
        <li><a href="/read/1/">html</a></li>
        <li><a href="/read/2/">css</a></li>
        <li><a href="/read/3/">javascript</a></li>
        '''
    return f'''<!doctype html>
    <html>
        <body>
            <h1><a href="/">WEB</a></h1>
            <ol> 
                {liTags}
            </ol> 
            <h2>Welcome</h2>
            Hello, Web
        </body>
    </html>
    '''

@app.route('/create/')
def create():
    return 'Create'

@app.route('/read/<int:id>/')  # 기본적으로 여기서 받는 값은 string, int:id로 해주면 int로 받을 수 있음
def read(id):
    print(id)  # 이거는 터미널에 출력
    # return 'Read ' + id  # default, string으로 받은 경우
    return 'Read ' + str(id)  # int type으로 받은 경우


    
app.run(port=5001, debug=True)  