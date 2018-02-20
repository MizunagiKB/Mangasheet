# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# ------------------------------------------------------------------ import(s)
import sys
import math
import argparse

import PIL.Image
import PIL.ImageDraw
import PIL.ImageFont


# ------------------------------------------------------------------- param(s)
COLOR_WHITE = (255, 255, 255)
COLOR_LBLUE = ( 63,  63, 255)
DPI = 300
# A4           210 x 297
# B5           182 x 257
# B5 baseframe 150 x 220


# ------------------------------------------------------------------- class(s)
# ---------------------------------------------------------------- function(s)
def mm_to_px(w_mm, h_mm, DPI=DPI):

    w_px = float(w_mm * DPI) / 25.4
    w_px = int(math.floor(w_px + 1)) & ~1
    h_px = float(h_mm * DPI) / 25.4
    h_px = int(math.floor(h_px + 1)) & ~1

    return w_px, h_px


def draw_center_rect(o_image, w_mm, h_mm, dpi=DPI, width=1, fill=COLOR_WHITE):

    paper_w, paper_h = o_image.size

    w, h = mm_to_px(w_mm, h_mm, dpi)

    o_draw = PIL.ImageDraw.Draw(o_image)

    if width == 1:
        range_st = 0
        range_sz = 1
    else:
        range_st = -1
        range_sz = 2

    for width_y in range(range_st, range_sz):
        for width_x in range(range_st, range_sz):
            x = ( paper_w - w) >> 1
            x += width_x
            y = ( paper_h - h) >> 1
            y += width_y
            o_draw.rectangle(
                ((x, y),
                (x + w, y + h)),
                outline=COLOR_LBLUE,
                fill=fill
            )


def gen_comicbase(dpi, margin, comment="", Jmarks=False):

    A4_paper_w, A4_paper_h = mm_to_px(210.0, 297.0, dpi)
    B5_paper_w, B5_paper_h = mm_to_px(182.0, 257.0, dpi)
    B5margin_w, B5margin_h = mm_to_px((182.0 - 2.0), (257.0 + 2.0) + (margin << 1), dpi)

    o_image = PIL.Image.new("RGB", (A4_paper_w, A4_paper_h), COLOR_WHITE)

    if Jmarks is True:
        draw_center_rect(o_image, 999, 257, dpi, 1)
        draw_center_rect(o_image, 182, 999, dpi, 1)

        o_draw = PIL.ImageDraw.Draw(o_image)
        o_draw.line(
            (
                A4_paper_w >> 1, 0, A4_paper_w >> 1, A4_paper_h
            ),
            fill=COLOR_LBLUE, width=1
            )
        o_draw.line(
            (
                0, A4_paper_h >> 1, A4_paper_w, A4_paper_h >> 1
            ),
            fill=COLOR_LBLUE, width=1
            )

    draw_center_rect(
        o_image,
        182 + (margin << 1),
        257 + (margin << 1),
        dpi, 1
        )

    draw_center_rect(
        o_image,
        182 + (margin << 1),
        257 + (margin << 1),
        dpi, 3, None
        )

    draw_center_rect(o_image, 182, 257, dpi)
    draw_center_rect(o_image, 150, 220, dpi)


    if len(comment.strip()) > 0:

        fontsize = int((dpi / 300.0) * 24)

        render_text = comment.strip()[0:200]
        fnt = PIL.ImageFont.truetype("res/NotoSansCJKjp-Regular.otf", fontsize)

        txt_x = ((A4_paper_w - B5margin_w) >> 1)
        txt_y = B5margin_h + ((A4_paper_h - B5margin_h) >> 1)
        o_draw = PIL.ImageDraw.Draw(o_image)
        o_draw.text(
            (txt_x, txt_y),
            render_text, font=fnt, fill=COLOR_LBLUE)

    return o_image


def main():

    parser = argparse.ArgumentParser(description="Comic base generator")

    parser.add_argument(
        "-o", "--out", type=str, required=True,
        help="Output filename")
    parser.add_argument(
        "-m", "--margin", type=int, required=False, default=3,
        help="Margin")
    parser.add_argument(
        "-d", "--dpi", type=int, required=False, default=DPI,
        help="Output filename")

    o_argv = parser.parse_args()

    o_image = gen_comicbase(o_argv.dpi, o_argv.margin)
    o_image.save(o_argv.out)

if __name__ == "__main__":
    main()

# [EOF]
