from flask import Flask
from PIL import Image, ImageFont, ImageDraw


app = Flask(__name__)

@app.route('/')
def hello_world():
    return text_to_dot_map("Python PIL")


def text_to_dot_map(textToDisplay):
    font = ImageFont.truetype('arialbd.ttf', 15)
    size = font.getsize(textToDisplay)  # calc the size of text in pixels
    image = Image.new('1', size, 1)  # create a b/w image
    draw = ImageDraw.Draw(image)
    draw.text((0, 0), textToDisplay, font=font)  # render the text to the bitmap

    stringoutput = ""
    for row in range(size[1]):
        for column in range(size[0]):
            stringoutput += map_bit_to_char(image, column, row)

        stringoutput += "<br>"

    return stringoutput


def map_bit_to_char(im, col, row):
    if im.getpixel((col, row)):
        return '&nbsp;&nbsp;'
    else:
        return '#'


if __name__ == '__main__':
    app.run()
