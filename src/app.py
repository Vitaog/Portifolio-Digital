from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contato')
def contatos():
    return render_template('contato.html')

@app.route('/sobremim')
def sobremim():
    return render_template('sobremim.html')
    
@app.route('/projeto')
def portfolio():
    return render_template('projeto.html')