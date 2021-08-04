from flask import Flask, request
app = Flask(__name__)

@app.route('/')

def index():
    return 'Hello World'

# GET, POST, PUT, PATCH, DELETE
@app.route('/post/<int:post_id>', methods = ['GET', 'POST'])
def lala(post_id):
    # return 'The post id is ' + str(post_id)
    if request.method == 'GET': return f'The post id is {post_id}'
    else: return f'This is another method and not GET'

@app.route('/form', methods = ['POST'])
def form():
    form = request.form
    key1 = request.form['key1']
    ret = f'Form: {form}\nKey1: {key1}'
    print(ret)
    return ret
