# A simple HTTP service built directly against the low-level(底层) WSGI spec.
from pprint import pformat
from wsgiref.simple_server import make_server


def app(environ, start_reponse):
    headers = {'Content-Type': 'text/plain; charset=utf-8'}
    start_reponse('200 OK', list(headers.items()))
    yield 'Here is the WSGI environment:\r\n\r\n'.encode('utf-8')
    yield pformat(environ).encode('utf-8')


if __name__ == '__main__':
    httpd = make_server('', 8000, app)
    host, port = httpd.socket.getsockname()
    print('Serving on', host, 'port', port)
    httpd.serve_forever()

