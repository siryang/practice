import time
import BaseHTTPServer
import os

HOST_NAME = '127.0.0.1' # !!!REMEMBER TO CHANGE THIS!!!
PORT_NUMBER = 80 # Maybe set this to 9000.


class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_HEAD(s):
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
    def do_GET(s):
        """Respond to a GET request."""
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
        s.wfile.write("<html><head><title>Title goes here.</title></head>")
        s.wfile.write("<body><p>This is a test.</p>")
        # If someone went to "http://something.somewhere.net/foo/bar/",
        # then s.path equals "/foo/bar/".
        s.wfile.write("<p>Current path: %s</p>" % os.getcwd())
        s.wfile.write("<p>Base path: %s</p>" % os.path.basename("."))
        accessPath = os.path.join(os.getcwd(), os.path.basename(s.path))
        s.wfile.write("<p>You accessed path: %s</p>" % accessPath)
        if os.path.isfile(accessPath):
            fp = open(accessPath)
            map(lambda x: s.wfile.write("<p>%s</p>" % x) , fp.readlines())
            fp.close()
        else:
            s.wfile.write("<p>not files</p>")
        s.wfile.write("</body></html>")

def main():
    server_class = BaseHTTPServer.HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
    print time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER)

if __name__ == '__main__':
   main()
