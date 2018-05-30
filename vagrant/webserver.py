from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

class WebServerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            if self.path.endswith("/hello"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                output = ""
                output += "<html><body>Hello World!</body></html>"

                self.wfile.write(output)
                
                print("test")
                return
        except IOError:
            self.send_error(404, "File Not Found: {}".format(self.path))


def main():
    try:
        port = 8080
        server = HTTPServer(('',port), WebServerHandler)
        print("BaseHTTPServer is running on port {}".format(port))
        server.serve_forever()

    except KeyboardInterrupt:
        print("Servers working interrupter using ^C - stopping web server")
        server.socket.close()


if __name__ == "__main__":
    main()