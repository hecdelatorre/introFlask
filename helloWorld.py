from flask import Flask, request, url_for, redirect, abort, render_template
from flask.templating import render_template
from db import selectDataBase, insertData

app = Flask(__name__)

@app.route('/')
def index(): return 'Hello World'

# GET, POST, PUT, PATCH, DELETE
@app.route('/post/<int:post_id>', methods = ['GET'])
def lala(post_id):
    # return 'The post id is ' + str(post_id)
    if request.method == 'GET': return f'The post id is {post_id}'
    else: abort(403, 'This is another method and not GET')

@app.route('/form', methods = ['POST'])
def form():
    form = request.form
    key1 = request.form['key1']
    path = url_for('index')
    path_post = url_for('lala', post_id = 1)
    ret = f'Form: {form}\nKey1: {key1}\nPath: {path}\nPath POST: {path_post}'
    print(ret)
    return ret

@app.route('/redirect', methods = ['GET'])
def redirectX(): return redirect(url_for('lala', post_id = 1))

@app.route('/template', methods = ['GET'])
def template(): return render_template('template.html')

@app.route('/json', methods = ['GET'])
def json(): return {"username": "Chanchito", "email": "chanchito@gmail.com"}

@app.route('/home', methods = ['GET'])
def home(): return render_template('home.html', message  = 'Hello World')

@app.route('/db', methods = ['GET'])
def dataBase(): return render_template('db.html', dB = selectDataBase())

@app.route('/create', methods = ['GET', 'POST'])
def create(): 
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        age = request.form['age']
        insert = insertData(username, email, age)
        if insert == 1: return redirect(url_for('dataBase'))
        else: abort(403, 'Failed to send to database')

    return render_template('create.html')

