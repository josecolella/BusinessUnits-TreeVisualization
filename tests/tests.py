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
# -*- coding: utf-8 -*-

import unittest
import sys
import os
sys.path.insert(0, os.path.abspath('../app'))
from app import application


class EndPointTestCase(unittest.TestCase):

    def setUp(self):
        self.application = application
        self.application.testing = True

    def test_about_page_status_code(self):
        with self.application.test_client() as client:
            response = client.get('/about')
            self.assertEqual(response.status_code, 200)

    def test_about_page_content_type(self):
        with self.application.test_client() as client:
            response = client.get('/about')
            self.assertEqual(response.headers['Content-Type'],
                             'application/json')

    def test_about_page_incorrect_http_method_response(self):
        with self.application.test_client() as client:
            response = client.post('/about')
            self.assertEqual(response.status_code, 405)

    def test_index_page_status_code(self):
        with self.application.test_client() as client:
            response = client.get('/')
            self.assertEqual(response.status_code, 200)

    def test_index_page_content_type(self):
        with self.application.test_client() as client:
            response = client.get('/')
            self.assertIn('text/html', response.headers['Content-Type'])

    def test_index_page_incorrect_http_method_response(self):
        with self.application.test_client() as client:
            response = client.post('/')
            self.assertEqual(response.status_code, 405)
