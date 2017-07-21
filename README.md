# Business Units Tree Visualization

A small web application to transform the **BusinessUnits.yml** that is exported
from the Dynatrace Data Center RUM CAS to generate a tree visualization SVG for each
of the applications. Used for documentation purposes.

## Reason for creating this

This project was created to document the definitions of Business Units for
Dynatrace Data Center RUM. Sometimes clients want to be able to have a document
as to how Business Units (`Applications` -> `Transaction` -> `Tasks`) have been defined.
This is more so, when there are many Applications, are the client wants to have
an updated view of the applications.


## How to use

This application is simple to use. There are two steps to follow.

1. Upload the BusinessUnits.yml
2. Save the SVG for the applications that you would like

## Dependencies

```sh
pip install -r requirements.txt
```



## License

MIT License

    Copyright (c) 2017 Jose Colella

    Permission is hereby granted, free of charge, to any person obtaining a
    copy of this software and associated documentation files (the "Software"),
    to deal in the Software without restriction, including without limitation
    the rights to use, copy, modify, merge, publish, distribute, sublicense,
    and/or sell copies of the Software, and to permit persons to whom the
    Software is furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in
    all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
    FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
    DEALINGS IN THE SOFTWARE.
