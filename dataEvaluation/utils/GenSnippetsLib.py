import json
import os
import re

import numpy as np
from PIL import Image, ImageDraw, ImageFont
from pygments import highlight
from pygments.formatters import BBCodeFormatter
from pygments.lexers import JavaLexer
from pygments.styles import get_style_by_name


def parse_bbcode_list(bbcode, logging=False):
    result = []
    pattern = "\[[^\[\]]*?\]"
    idx = 0
    base_color = (0, 0, 0, 255)
    color = base_color
    bold = False
    italic = False
    aoi_default = "None"
    aoi_name = [aoi_default]
    while idx < len(bbcode):
        data = re.search(pattern, bbcode[idx:])
        meta = False

        if data is not None and data.start(0) == 0:
            value = data.group(0).strip("[").strip("]")

            if "/AOI" in value:
                meta = True
                aoi_name.pop()
                if logging:
                    print(f"after deletion {aoi_name}")
            elif "AOI" in value:
                meta = True
                aoi_name.append(value[4:])
                if logging:
                    print(f"after insertion {aoi_name}")

            if "/aoi" in value:
                meta = True
                aoi_name.pop()
            elif "aoi" in value:
                meta = True
                aoi_name.append(value[4:])

            if "/color" in value:
                meta = True
                color = base_color
            elif "color" in value:
                meta = True
                color = tuple(int(value[i: i + 2], 16) for i in (7, 9, 11))
                color = (color[0], color[1], color[2], 255)

            if meta == True:
                idx += data.end(0)

        if meta == False:
            result.append({"letter": bbcode[idx], "color": color, "bold": bold, "italic": italic, "AOI": [value for value in aoi_name]})
            idx += 1
    if len(aoi_name) != 1:
        raise Exception("AOI not closed - " + aoi_name[0])
    return result


def set_font(data, regular, bold, italic, bolditalic):
    new_result = []
    for entry in data:
        if entry["bold"] == True and entry["italic"] == True:
            entry["font"] = bolditalic

        if entry["bold"] == True and entry["italic"] == False:
            entry["font"] = bold

        if entry["bold"] == False and entry["italic"] == True:
            entry["font"] = italic

        if entry["bold"] == False and entry["italic"] == False:
            entry["font"] = regular

        new_result.append(entry)

    return new_result


def create_image(source_json, font_path="\\fonts\\ttf\\", lexer=JavaLexer, logging=False):
    data = {}
    with open(source_json) as f:
        data = json.load(f)

    code = ""
    for line in data["source-code"]:
        code += line + "\n"

    background_color = (data["background-color"][0], data["background-color"][1], data["background-color"][2])
    width_margin = data["width-margin"]
    height_margin = data["height-margin"]
    spacing = data["spacing"]

    regular = ImageFont.truetype(os.getcwd() + font_path + data["font-normal"], data["font-size"], encoding="unic")
    bold = ImageFont.truetype(os.getcwd() + font_path + data["font-bold"], data["font-size"], encoding="unic")
    italic = ImageFont.truetype(os.getcwd() + font_path + data["font-italic"], data["font-size"], encoding="unic")
    bolditalic = ImageFont.truetype(
        os.getcwd() + font_path + data["font-bold-italic"], data["font-size"], encoding="unic"
    )

    code = highlight(code, lexer(), BBCodeFormatter(line_numbers=False, style=get_style_by_name("vs")))
    code = parse_bbcode_list(code, logging)
    code = set_font(code, regular, bold, italic, bolditalic)

    source_code = []
    tmp_source_code = ""
    for tmp_data in code:
        if tmp_data["letter"] == "\n":
            source_code.append(tmp_source_code)
            tmp_source_code = ""
        else:
            tmp_source_code += tmp_data["letter"]

    img = Image.new("RGBA", (1, 1), color="white")
    draw = ImageDraw.Draw(img)
    max_length = max([draw.textsize(txt, regular)[0] for txt in source_code]) + 2 * width_margin
    max_height = (
            sum([draw.textsize("placeholder", regular)[1] + spacing for txt in data["source-code"]]) + 2 * height_margin
    )

    img = Image.new("RGBA", (max_length, max_height), color=background_color)
    draw = ImageDraw.Draw(img)

    width_current = width_margin
    height_current = height_margin
    result = []
    for letter in code:
        if letter["letter"] == "\n":
            width_current = width_margin
            height_current = height_current + draw.textsize("placeholder", regular)[1] + spacing
            letter["BoundingBox"] = (0, 0, 0, 0)
        else:
            letter["BoundingBox"] = draw.textbbox(
                (width_current, height_current), letter["letter"], font=letter["font"]
            )
            draw.text((width_current, height_current), letter["letter"], letter["color"], font=letter["font"])
            width_current += draw.textsize(letter["letter"], regular)[0]

        result.append(letter)
    return img, result


def create_background(width, height, color):
    r = np.full([height, width], color[0], np.uint8)
    g = np.full([height, width], color[1], np.uint8)
    b = np.full([height, width], color[2], np.uint8)
    a = np.full([height, width], color[3], np.uint8)
    background = np.dstack((r, g, b, a))
    return background


def place_image_on(background, image, x_percent, y_percent):
    width_back = background.shape[1]
    height_back = background.shape[0]
    image_width_half = int(image.shape[1] / 2)
    image_height_half = int(image.shape[0] / 2)
    image_width = int(image.shape[1])
    image_height = int(image.shape[0])
    image_width_start = int(width_back * x_percent) - image_width_half
    image_height_start = int(height_back * y_percent) - image_height_half

    image_width_end = image_width_start + image_width
    image_height_end = image_height_start + image_height
    background[image_height_start:image_height_end, image_width_start:image_width_end, :] = image

    return background
