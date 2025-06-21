# Agenda: 나의 컴퓨터에 개발환경 세팅

from flask import Flask 

app = Flask(__name__)

@app.route('/')
def index():
    return 'hi'  
    
app.run(port=5001, debug=True)  
'''
default port는 5000, 
다른 서비스에서 사용중이라면 이렇게 변경해줘야됨, 
바뀌면 알아서 재실행되는 debug 모드 
'''