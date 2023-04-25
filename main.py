from flask import Flask, render_template

from front import *

app = Flask(__name__)

@app.route('/')
def index():
    '''
    Displays the index page accessible at '/'
    '''
    return render_template('index.html')

@app.route('/new_cca')
def new_cca():
    return render_template('cca.html')

if __name__ == '__main__':
    app.run('0.0.0.0')

