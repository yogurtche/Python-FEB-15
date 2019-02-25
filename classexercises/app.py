from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        return "Bye, World"
    return "Hello World!"

@app.route('/hello/<word>')
def hello_word(word):
    return 'Hello, {}'

@app.route('/hello_v2', methods=['POST'])
def hello_word_v2():
    data=request.get_json()
    word=data['word']
    return 'Hello, {}'.format(word)