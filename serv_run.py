# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# ------------------------------------------------------------------ import(s)
import sys
import os
import io
import bottle

import mangasheet


# ------------------------------------------------------------------- param(s)
# ------------------------------------------------------------------- class(s)
# ---------------------------------------------------------------- function(s)
@bottle.route("/mangasheet.png")
def res_image():

    jmark = False
    if bottle.request.query.jmark in ("on", True, 1):
        jmark = True

    o_image = mangasheet.gen_comicbase(
        int(bottle.request.query.dpi),
        int(bottle.request.query.margin),
        bottle.request.query.comment,
        jmark
        )

    image_writer = io.BytesIO()
    o_image.save(image_writer, format="png")

    res = bottle.HTTPResponse(status=200, body=image_writer.getvalue())
    res.set_header("Content-Type", "image/png")

    return res

@bottle.route("/")
@bottle.route("/index")
@bottle.route("/index.html")
def web_index():
    return(bottle.template("templates/index.html", dict()))


def main():

    #bottle.run(host="localhost", port=8000, debug=True, reloader=True)
    os.chdir(os.path.dirname(__file__))
    application = bottle.default_app()


if __name__ == "__main__":
    main()

# [EOF]
