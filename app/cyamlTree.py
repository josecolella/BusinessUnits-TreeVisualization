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

from __future__ import print_function
import yaml
import typing
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader


def profile(func):
    def check_profile(*args):
        import cProfile
        import pstats
        import io
        pr = cProfile.Profile()
        pr.enable()
        func(*args)
        pr.disable()
        s = io.StringIO()
        sortby = 'tottime'
        ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
        ps.print_stats()
        return s.getvalue()
    return check_profile


def businessunits_to_dict(yaml_file: str) -> dict:
    """
    TODO: Document
    """
    with open(yaml_file) as f:
        yaml_output = yaml.load(f.read(), Loader=Loader)
    return yaml_output


def dict_to_d3tree(yaml_dict: dict) -> dict:
    """
    TODO: Document
    """

    def sanitizeNameValue(x): return x.get('name') != "All other"

    def sanitizeTransactionValue(x): return x.get(
        'transactions') not in (None, "All Other")

    applications = [
        {"name": application['name'],
         "children": [{
             "name": transaction['name'],
             "children":
             [{"name": step['name']}
                 for step in transaction['steps'] if sanitizeNameValue(step)]
         } for transaction in application.get('transactions')]}
        for application in yaml_dict if sanitizeNameValue(application) and sanitizeTransactionValue(application)]

    return applications
