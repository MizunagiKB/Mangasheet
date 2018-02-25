# -*- coding: utf -*-
import sys
import argparse

import PIL.Image
import PIL.ImageDraw

import paper_calc


COLOR_WHITE = (255, 255, 255)
COLOR_LBLUE = ( 63,  63, 255)
DPI = 300
# A4           210 x 297
# B5           182 x 257
# B5 baseframe 150 x 220


def gen_namebase(dpi, div_size):

    o_a4v = paper_calc.A4PaperH(dpi)
    px_w, px_h = o_a4v.px_size()

    px_mm_10 = paper_calc.mm_to_px(10)
    px_mm_03 = paper_calc.mm_to_px(3)
    px_mm_01 = paper_calc.mm_to_px(1)

    px_mm = (px_mm_10 * 2) + (px_mm_03 * (div_size - 1))

    name_h = ((px_h - px_mm) / div_size)
    name_w = name_h * 182.0 / 257.0

    px_w_space = (px_w - ((px_mm_10 * 2) + (name_w * div_size * 2) + (px_mm_03 * div_size))) / (div_size >> 1)

    print("px_w", px_w)
    print("px_mm_03", px_mm_03)
    print("px_mm_10", px_mm_10)
    print("name_w", name_w)
    print("px_w_space", px_w_space)

    o_image = PIL.Image.new("RGB", o_a4v.px_size(), COLOR_WHITE)
    o_draw = PIL.ImageDraw.Draw(o_image)

    for x in range(div_size * 2):
        for y in range(div_size):

            render_x = px_mm_10 + (name_w * x) + (px_mm_01 * x)
            render_y = px_mm_10 + (name_h * y) + (px_mm_03 * y)

            render_x += (px_w_space * (x >> 1))

            render_w = render_x + name_w
            render_h = render_y + name_h

            o_draw.rectangle(
                (
                    (render_x, render_y), (render_w, render_h)
                ),
                outline=COLOR_LBLUE,
                fill=None
            )

    return o_image


def main():

    parser = argparse.ArgumentParser(description="Name sheet generator")

    parser.add_argument(
        "-o", "--out", type=str, required=True,
        help="Output filename")
    parser.add_argument(
        "-m", "--margin", type=int, required=False, default=3,
        help="Margin")
    parser.add_argument(
        "-d", "--dpi", type=int, required=False, default=DPI,
        help="Image resolution")

    o_argv = parser.parse_args()

    o_image = gen_namebase(4, o_argv.dpi, o_argv.margin)
    o_image.save(o_argv.out)


if __name__ == "__main__":
    main()



# [EOF]
