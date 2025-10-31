import http.server
from logging import Handler
import socketserver
import re

class HttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        regex = regex = r".((css)|(js)|(png)|(svg)|(json))(\/)?$"
        
        if re.match(regex, self.path, re.MULTILINE) != None:
            pass
        elif re.search(".svg", self.path) != None:
            pass
        elif re.search(".png", self.path) != None:
            pass
        elif re.search(".js", self.path) != None:
            pass
        elif re.search(".css", self.path) != None:
            pass
        elif re.search(".ttf", self.path) != None:
            pass
        else:
            self.path = 'index.html'

        self.path = 'src/' + self.path
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

handler = HttpRequestHandler

PORT = 8000
my_server = socketserver.TCPServer(("", PORT), handler)

print("Epita-Map server running and serving on 127.0.0.1 port " + str(PORT) + " (http://127.0.0.1:" + str(PORT) + ")")
my_server.serve_forever()