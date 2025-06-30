from bottle import Bottle
from bottle import run
app=Bottle()
@app.route('/jaiwin')
@app.route('/')
def homepage():
    return "<h1>Hello</h1>"

run(app,host='localhost',port=9090)
