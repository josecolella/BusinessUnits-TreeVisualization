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

from flask import Flask
from flask import (jsonify, render_template, request, redirect, url_for, flash)
from flask_uploads import (UploadSet, configure_uploads)
import cyamlTree
import ujson

app = Flask(__name__)
app.secret_key = 'e2ea4d4fed55c18e397c4f22350e160009b88302b2404232e3e4fa50cafb7950'
app.config['UPLOADED_FILES_DEST'] = '/tmp/business_units'
UPLOADED_FILES_DEST = '/tmp/business_units'
uploaded_files = UploadSet(name='files', extensions=('yml',))
configure_uploads(app, (uploaded_files,))


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST' and 'file' in request.files:
        filename = uploaded_files.save(request.files.get('file'))
        yaml_dict = cyamlTree.businessunits_to_dict(
            uploaded_files.path(filename))
        output = cyamlTree.dict_to_d3tree(yaml_dict)
    return render_template('upload.html', tree=ujson.dumps(output[0]))


@app.route('/about', methods=['GET'])
def about():
    return jsonify({'version': 1.0,
                    'message': 'Welcome to the API'})


if __name__ == '__main__':
    app.run(host='0.0.0.0')
