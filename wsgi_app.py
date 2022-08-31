#-*- coding: utf-8 -*-
def wsgi_app(environ, start_response):
    import sys
    output = sys.version.encode('utf8')
    status = '200 OK'
    headers = [('Content-type', 'text/plain'),
               ('Content-Length', str(len(output)))]
    start_response(status, headers)
    yield output

# mod_wsgi need the *application* variable to serve our small app
application = wsgi_app
