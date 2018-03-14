from PIL import Image, ImageFont, ImageDraw

# 1 - Arial - ariblk.ttf
# 2 - Impact - impact.ttf
# 3 - Bauhaus - BAUHS93.TTF
font_map = {'1': 'ariblk.ttf',
            '2': 'impact.ttf',
            '3': 'GILSANUB.TTF',
            }


def text_to_dot_map(texttoconvert, font, font_size):
    font = ImageFont.truetype(font_map[font], int(font_size))
    size = font.getsize(texttoconvert)  # calc the size of text in pixels
    image = Image.new('1', size, 1)  # create a b/w image
    draw = ImageDraw.Draw(image)
    draw.text((0, 0), texttoconvert, font=font)  # render the text to the bitmap

    stringoutput = ''
    for row in range(size[1]):
        line = []
        for column in range(size[0]):
            line += [map_bit_to_char(image, column, row)]

        if len(set(line)) == 1:
            continue

        stringoutput += ''.join(line) + '<br>'

    return stringoutput


def map_bit_to_char(im, col, row):
    if im.getpixel((col, row)):
        return '&nbsp;'
    else:
        return '#'
