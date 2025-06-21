# Agenda: 플라스크를 사용하는 이유

from flask import Flask 
import random 

app = Flask(__name__)

@app.route('/')
def index():
    # return 'hi'  # 이전 강의 내용
    return 'random : <strong>' + str(random.random()) + '</strong>'  
    '''
    flask를 이용하면 파이썬 코드를 html에 적용시킬 수 있다. 
    이렇게 랜덤 숫자를 웹페이지에 표시 가능
    '''
    
app.run(port=5001, debug=True)  