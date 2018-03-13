from flask import Flask, render_template
from python.dotmapgenerator import *


app = Flask(__name__)
app.config['DEBUG'] = True
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/app.html')
def application():
    return render_template('app.html')


@app.route('/<text>')
def index_with_text(text):
    return text_to_dot_map(text)


if __name__ == '__main__':
    app.run()
