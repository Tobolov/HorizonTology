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
        inner = request.args.get("text[main]")
        if not inner:
            return error()

        outer = request.args.get("text[wrapper]")
        if not outer:
            return error()

        font = request.args.get("options[font]")
        if not font:
            return error()

        size = request.args.get("options[size]")
        if not size:
            return error()

        text = wrap_text_in_text(inner, outer, font, size)
        return render_template('process.html', generated_text=text)

    else:
        return render_template('app.html')


if __name__ == '__main__':
    generate_font_paths(app)
    app.run()
