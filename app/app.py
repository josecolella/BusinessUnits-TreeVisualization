# Copyright (c) 2017 Jose Colella

# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import print_function
from flask import (Flask, jsonify, render_template,
                   request, make_response)
from flask_uploads import (UploadSet, configure_uploads, UploadNotAllowed)
from flask_caching import Cache
import uuid
import ujson
import cyamlTree


application = Flask(__name__)
application.secret_key = str(uuid.uuid1())
application.config["UPLOADED_FILES_DEST"] = "/tmp/business_units"
application.config["DOWNLOADED_FILES_DEST"] = "/tmp/"
cache = Cache(application, config={"CACHE_TYPE": "redis"})


uploaded_files = UploadSet(name="files", extensions=("yml", ""))
configure_uploads(application, (uploaded_files,))


@application.route("/", methods=["GET"])
@cache.cached(timeout=60)
def index():
    return render_template("index.html")


@application.route("/upload", methods=["POST"])
def upload():
    response = None
    if request.method == "POST" and "file" in request.files:
        try:
            filename = uploaded_files.save(request.files.get("file"))
            yaml_dict = cyamlTree.businessunits_to_dict(uploaded_files.path(filename))
            output = cyamlTree.dict_to_d3tree(yaml_dict)
            response = render_template(
                "upload.html", tree=ujson.dumps(output))
        except UploadNotAllowed:
            message = ujson.dumps({
                "status": "Error: Upload Not Allowed",
                "description": "Only .yml files can be uploaded"
            })
            response = make_response(message, 400)
    return response


@application.route("/about", methods=["GET"])
@cache.cached(timeout=60)
def about():
    return jsonify({"version": 1.0,
                    "message": "Welcome to the API"})


if __name__ == "__main__":
    application.run(host="0.0.0.0")
