from http.server import HTTPServer, SimpleHTTPRequestHandler


class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/data.json":
            with open("data.json", "r") as f:
                data = f.read()

            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(data.encode())
        else:
            super().do_GET()


server_address = ("", 8000)
httpd = HTTPServer(server_address, Handler)
print("Serving on http://localhost:8000")
httpd.serve_forever()
