from flask import Flask, render_template, request
from python.dotmapgenerator import *


app = Flask(__name__)
app.config['DEBUG'] = True
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/app.html')
def process():
    error = lambda: render_template('process.html', generated_text="ERROR")

    if len(request.args) != 0:
        maintext = request.args.get("text[main]")
        if not maintext:
            return error()

        font = request.args.get("options[font]")
        if not font:
            return error()

        text = text_to_dot_map(maintext, font)
        return render_template('process.html', generated_text=text)

    else:
        return render_template('app.html')


if __name__ == '__main__':
    app.run()
