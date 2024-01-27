from http.server import HTTPServer, BaseHTTPRequestHandler

class Serv(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        elif self.path =='/about':
             self.path ='/about.html'
        elif self.path =='/contact':
             self.path ='/contact.html'
        try:
            file_to_open = open(self.path[1:], encoding='utf-8').read()
            self.send_response(200)
        except:
            file_to_open = "Ez az oldal nem található"
            self.send_response(404)
        self.end_headers()
        self.wfile.write(bytes(file_to_open, 'utf-8'))

httpd = HTTPServer(('localhost', 8080), Serv)
httpd.serve_forever()