# Agenda: 쓰기 기능 구현

from flask import Flask, request, redirect 

app = Flask(__name__)

nextId = 4  # 추가될 id의 시작
topics = [
    {'id': 1, 'title': 'html', 'body': 'html is ...'},
    {'id': 2, 'title': 'css', 'body': 'css is ...'},
    {'id': 3, 'title': 'javascript', 'body': 'javascript is ...'},
]

def template(contents, content):
    return f'''<!doctype html>
    <html>
        <body>
            <h1><a href="/">WEB</a></h1>
            <ol> 
                {contents}
            </ol> 
            {content}
            <ul>
                <li><a href="/create/">create</li>
            </ul>
        </body>
    </html>
    '''

def getContents():
    liTags = ''
    for topic in topics:
        liTags = liTags + f'<li><a href="/read/{topic["id"]}/">{topic["title"]}</a></li>'
    return liTags

@app.route('/')
def index():
    return template(getContents(), '<h2>Welcome</h2>Hello, WEB')

@app.route('/read/<int:id>/') 
def read(id):  
    '''
    접속한 id를 받아서(클릭한 리스트 id)
    그 id에 해당하는 topic body를 웹 페이즈 본문 내용에 표시
    '''
    title = ''
    body = ''
    for topic in topics:
        if id == topic['id']:
            title = topic['title']
            body = topic['body']
            break
    return template(getContents(), f'<h2>{title}</h2>{body}')

# POST 방식에 맞게 수정해야됨. 아무것도 안 넣으면 GET 방식
@app.route('/create/', methods=['GET', 'POST'])
def create():  # 쓰기 기능
    '''
    사용자에게 입력을 받기
    input, text: 한줄 입력
    input, submit: 전송 버튼
    textarea: 박스형 입력

    GET 방식: default, 주소에 입력 값이 포함됨
    POST 방식: route와 함수 내 조건문 수정 필요, 주소에 포함되지 않음
    '''
    if request.method == 'GET':  # GET/POST 방식 조회 가능
        content = '''
            <form action="/create/" method="POST">
                <p><input type="text" name="title" placeholder="title"></p>
                <p><textarea name="body" placeholder="body"></textarea></p>
                <p><input type="submit" value="create"></p>
            </form>
        '''
        return template(getContents(), content)
    elif request.method == 'POST':
        global nextId
        title = request.form['title']  # 입력 양식 가져올 수 있음
        body = request.form['body']  # 입력 양식 가져올 수 있음
        newTopic = {'id': nextId, 'title': title, 'body': body}
        topics.append(newTopic)  # topics 리스트 업데이트 됨
        url = '/read/' + str(nextId) + '/'
        nextId += 1
        return redirect(url)  # 강제로 지정된 주소로 리디렉션 
        

app.run(port=5001, debug=True)  