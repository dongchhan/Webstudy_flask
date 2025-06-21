# Agenda: Routing

from flask import Flask 
import random 

app = Flask(__name__)


@app.route('/')
def index():
    return 'Welcome'

@app.route('/create/')
def create():
    return 'Create'

@app.route('/read/<int:id>/')  # 기본적으로 여기서 받는 값은 string, int:id로 해주면 int로 받을 수 있음
def read(id):
    print(id)  # 이거는 터미널에 출력
    # return 'Read ' + id  # default, string으로 받은 경우
    return 'Read ' + str(id)  # int type으로 받은 경우


    
app.run(port=5001, debug=True)  