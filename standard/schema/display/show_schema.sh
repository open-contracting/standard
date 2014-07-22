#!/usr/bin/env python
import SimpleHTTPServer
import SocketServer

PORT = 8001

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
httpd = SocketServer.TCPServer(("", PORT), Handler)
print "--------------"
print "Open your web browser to http://localhost:8001"
print "--------------\n\n\n"
httpd.serve_forever()
