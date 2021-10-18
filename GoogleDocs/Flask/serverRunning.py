from http.server import HTTPServer, SimpleHTTPRequestHandler

httpd = HTTPServer( ('127.0.0.1', 8080), SimpleHTTPRequestHandler )
print( '서버시작' )
httpd.serve_forever()
print( '서버종료' )
