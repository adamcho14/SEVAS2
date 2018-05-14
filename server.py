import http.server  # https://docs.python.org/3/library/http.server.html
import cgitb
import ssl  # https://docs.python.org/3.0/library/ssl.html

# https://cit.uniba.sk/wiki/doku.php?id=public/jas/cosign
# https://www.piware.de/2011/01/creating-an-https-server-in-python/

cgitb.enable()

address = ""
port = 8000

handler = http.server.CGIHTTPRequestHandler
handler.cgi_directories = ["/", "/administration"]
autServer = http.server.HTTPServer((address, port), handler)
#autServer.socket = ssl.wrap_socket(autServer.socket, None, None, True)
print("Serving at port", port)
print("Access voting by typing this to your browser: localhost:" + str(port) + "/index.py")
print("If you want to access paper voting management, type: localhost:" + str(port) + "/administration/login.py")
autServer.serve_forever()

