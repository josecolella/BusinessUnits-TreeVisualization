# Business Units Tree Visualization 

![Travis Build Status](https://travis-ci.org/josecolella/BusinessUnits-TreeVisualization.svg?branch=dev)

A small web application to transform the **Business Units** export that is exported
from the Dynatrace Data Center RUM CAS to generate a tree visualization SVG for each
of the applications. Used for documentation purposes.

## Reason for creating this

This project was created to document the definitions of Business Units for
Dynatrace Data Center RUM. Sometimes clients want to be able to have a document
as to how Business Units (`Applications` -> `Transaction` -> `Tasks`) have been defined.
This is more so, when there are many Applications, are the client wants to have
an updated view of the applications.


## Usage

This application is simple to use. There are two steps to follow.

1. Upload the file exported by Central Analysis Server (usually called bussgroups)
    - **No files are saved in the backend**
2. Click on the application that you would like to visualize
3. Save the visualization of the application as SVG and PDF



![Tutorial on how to use platform](https://cl.ly/3e1U1k1D3o3O/Screen%20Recording%202017-08-05%20at%2010.15%20pm.gif)


## Demo

You can play around with the platform at the following link:

[http://dcrum-buv.duckdns.org/](http://dcrum-buv.duckdns.org/)

If you find any bugs please open an issue, and any feedback is appreciated.

## Deployment

The easiest way to deploy this is through docker or as a service using the docker-compose.yml

```sh
docker pull josecolella/flask-nginx-businessunits-vis
docker pull redis
docker run -d -p 6379:6379 redis
docker run -d -p 80:80 josecolella/flask-nginx-businessunits-vis
```

* Through docker-compose.yml

This will create two load-balances instances of the app and a redis cache instance

```sh
docker swarm init
docker stack deploy -c docker-compose.yml businessunits-prod
docker stack ps businessunits-prod
```

## Technologies

### Backend

- Python 3
- Flask
- Gunicorn
- Redis

### Frontend


Thanks to the following open-source projects which made this platform possible:

- [D3.js](https://github.com/d3/d3)
- [PDFKit.js](https://github.com/devongovett/pdfkit)
- [FileSaver.js](https://github.com/eligrey/FileSaver.js)
- [SVGtoPDF.js](https://github.com/alafr/SVG-to-PDFKit)

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
