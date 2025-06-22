# Agenda: 수정 기능 구현

from flask import Flask, request, redirect 

app = Flask(__name__)

nextId = 4  # 추가될 id의 시작
topics = [
    {'id': 1, 'title': 'html', 'body': 'html is ...'},
    {'id': 2, 'title': 'css', 'body': 'css is ...'},
    {'id': 3, 'title': 'javascript', 'body': 'javascript is ...'},
]

def template(contents, content, id=None):
    contextUI = ''
    if id != None:  # read를 통해서 id를 전해받을 때, 즉 홈페이지가 아닐 때 
        contextUI = f'''
            <li><a href = "/update/{id}/">update</a></li>  <!-- update 페이지로 보내는 리스트(링크) -->
        '''
    return f'''<!doctype html>
    <html>
        <body>
            <h1><a href="/">WEB</a></h1>
            <ol> 
                {contents}  <!-- 목차 부분 -->
            </ol> 
            {content}  <!-- 본문 부분 -->
            <ul>
                <li><a href="/create/">create</li>  <!-- create 창으로 링크 리스트 -->
                {contextUI}  <!-- read 경로라면 수정 리스트 -->
            </ul>
        </body>
    </html>
    '''

def getContents():
    ''' 목록 부분 '''
    liTags = ''
    for topic in topics:
        # 목차, 누르면 read 페이지로 감
        liTags = liTags + f'<li><a href="/read/{topic["id"]}/">{topic["title"]}</a></li>'
    return liTags

@app.route('/')
def index():
    ''' 홈페이지 '''
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
    return template(getContents(), f'<h2>{title}</h2>{body}', id)

# POST 방식에 맞게 수정해야됨. 아무것도 안 넣으면 GET 방식
@app.route('/create/', methods=['GET', 'POST'])
def create():  # 쓰기 기능
    '''
    사용자에게 입력을 받기
    GET 방식: default, 주소에 입력 값이 포함됨
    POST 방식: route와 함수 내 조건문 수정 필요, 주소에 포함되지 않음
    '''
    if request.method == 'GET':  # GET/POST 방식 조회 가능
        content = '''
            <form action="/create/" method="POST">
                <p><input type="text" name="title" placeholder="title"></p>  <!-- input, text: 한줄 입력 -->
                <p><textarea name="body" placeholder="body"></textarea></p>  <!-- textarea: 박스형 입력 -->
                <p><input type="submit" value="create"></p>  <!-- input, submit: 전송 버튼 -->
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
    
@app.route('/update/<int:id>/', methods=['GET', 'POST'])
def update(id):  # 수정 기능
    if request.method == 'GET':
        title = ''
        body = ''
        for topic in topics:
            if id == topic['id']:
                title = topic['title']
                body = topic['body']
                break
        content = f'''
            <form action="/update/{id}/" method="POST">
                <p><input type="text" name="title" placeholder="title" value={title}></p>  
                <p><textarea name="body" placeholder="body">{body}</textarea></p>  
                <p><input type="submit" value="update"></p> 
            </form>
        '''
        return template(getContents(), content)
    elif request.method == 'POST':
        global nextId
        # 새로 입력 받은 값
        title = request.form['title']  
        body = request.form['body']  
        for topic in topics:
            if id == topic['id']:
                # 새로 입력받은 값으로 update
                topic['title'] = title
                topic['body'] = body
                break
        url = '/read/' + str(nextId) + '/'
        return redirect(url)  # 강제로 지정된 주소로 리디렉션 
        

app.run(port=5001, debug=True)  