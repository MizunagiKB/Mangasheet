# -*- coding: utf-8 -*-
import math

# A4           210 x 297
# B5           182 x 257
DPI = 300


# ------------------------------------------------------------------- class(s)
class CPaper(object):
    def __init__(self, mm_w, mm_h, dpi=None):
        self.mm_w = mm_w
        self.mm_h = mm_h
        self.dpi = None

    def in_size(self):
        return mm_to_in(self.mm_w), mm_to_in(self.self.mm_h)

    def mm_size(self):
        return self.mm_w, self.mm_h

    def px_size(self):
        return mm_to_px(self.mm_w), mm_to_px(self.mm_h)


# ---------------------------------------------------------------- function(s)
def mm_to_in(mm_size, DPI=DPI):
    in_size = float(mm_size / 25.4)

    return in_size

def mm_to_px(mm_size, DPI=DPI):
    px_size = float(mm_size * DPI) / 25.4
    px_size = int(math.floor(px_size + 1)) & ~1

    return px_size

def A4PaperV(dpi):
    return CPaper(210, 297, dpi)
def A4PaperH(dpi):
    return CPaper(297, 210, dpi)

def B5PaperV(dpi):
    return CPaper(182, 257, dpi)
def B5PaperH(dpi):
    return CPaper(257, 182, dpi)


# [EOF]
