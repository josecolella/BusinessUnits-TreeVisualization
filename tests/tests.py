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

#!/usr/bin/env python

import unittest
import requests


class BusinessUnitEndPointTestCase(unittest.TestCase):

    def test_about_page_status_code(self):
        response = requests.get('http://localhost:5000/about')
        self.assertEqual(response.status_code, 200)

    def test_about_page_content_type(self):
        response = requests.get('http://localhost:5000/about')
        self.assertEqual(response.headers['Content-Type'], 'application/json')

    def test_index_page_status_code(self):
        response = requests.get('http://localhost:5000/')
        self.assertEqual(response.status_code, 200)

    def test_index_page_content_type(self):
        response = requests.get('http://localhost:5000/')
        self.assertEqual(response.headers['Content-Type'], 'text/html')


if __name__ == '__main__':
    unittest.main(verbosity=3)
