from PIL import Image, ImageFont, ImageDraw
import itertools, os

font_map = {}


def generate_font_paths(app):
    global font_map
    font_map = {'1': 'ariblk.ttf',
                '2': os.path.join(app.root_path, 'python', 'block.ttf'),
                '3': 'GILSANUB.TTF',
                '4': os.path.join(app.root_path, 'python', 'blockline.ttf'),
                }


def text_to_dot_map(text, font, font_size):
    font = ImageFont.truetype(font_map[font], int(font_size))
    size = font.getsize(text)  # calc the size of text in pixels
    image = Image.new('1', size, 1)  # create a b/w image
    draw = ImageDraw.Draw(image)
    draw.text((0, 0), text, font=font)  # render the text to the bitmap

    output = []
    for row in range(size[1]):
        line = []
        for column in range(size[0]):
            line += [not image.getpixel((column, row))]

        if len(set(line)) == 1:
            continue

        output += [line]

    return output


def count_free_slots(dot_map):
    sum = 0
    for row in range(len(dot_map)):
        for column in range(len(dot_map[0])):
            sum += 1 if dot_map[row][column] else 0

    return sum


def text_to_fancy(text, font, font_size):
    dot_map = text_to_dot_map(text, font, font_size)

    output = ''
    for row in range(len(dot_map)):
        for column in range(len(dot_map[0])):
            output += '#' if dot_map[row][column] else '&nbsp;'

        output += '<br>'

    return output + '<br>'


def wrap_text_in_text(inner, outer, font, font_size):
    dot_map = text_to_dot_map(outer, font, font_size)
    inner = list(itertools.chain.from_iterable([[x, " "] for x in inner.split(" ")]))

    out = ""
    current_word = 0
    for i in range(len(dot_map)):
        length = 0
        for j in range(len(dot_map[0])):
            length += 1

            if not dot_map[i][j]:
                out += "&nbsp;" * length
                length = 0

            if length == len(inner[current_word]):
                out += inner[current_word]
                current_word += 1
                length = 0

                if len(inner) == current_word:
                    print(dot_map)
                    return out
        out += "<br>"

    return out
