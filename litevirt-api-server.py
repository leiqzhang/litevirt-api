#!/usr/bin/env python

"""mimerender example for web.py. Run this server and then try:

$ curl -iH "Accept: application/html" localhost:8080/x
...
Content-Type: text/html
...
<html><body>Hello, x!</body></html>

$ curl -iH "Accept: application/xml" localhost:8080/x
...
Content-Type: application/xml
...
<message>Hello, x!</message>

$ curl -iH "Accept: application/json" localhost:8080/x
...
Content-Type: application/json
...
{"message": "Hello, x!"}

$ curl -iH "Accept: text/plain" localhost:8080/x
...
Content-Type: text/plain
...
Hello, x!

"""
import web
try:
    import simplejson as json
except ImportError:
    import json
import mimerender
import time
from gevent import monkey; monkey.patch_all()
from gevent.pywsgi import WSGIServer

mimerender = mimerender.WebPyMimeRender()

render_xml = lambda message: '<message>%s</message>'%message
render_json = lambda **args: json.dumps(args)
render_html = lambda message: '<html><body>%s</body></html>'%message
render_txt = lambda message: message

urls = (
    '/api/', 'index',
)


class index:
    @mimerender(
        default = 'html',
        html = render_html,
        xml = render_xml,
        json = render_json,
        txt = render_txt
    )

    def GET(self):
        #time.sleep(10)
        return {'message': 'Hello, world!'}


if __name__ == "__main__":
    #app = web.application(urls, globals())
    #app.run()
    application = web.application(urls, globals()).wsgifunc()
    server = WSGIServer(('', 8088), 
                        application)
    server.serve_forever()
