from flask import Flask

app = Flask(__name__)

@app.route('/inicio')
def funcionPorDefinir():
    return 'hola mundo'