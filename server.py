from http.server import BaseHTTPRequestHandler, HTTPServer


class DemoAppServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        routes = {
            "/": "demo-app is working",
            "/healthz": "healthy"
        }
        content = routes[self.path]
        self.wfile.write(bytes(content, "utf-8"))


if __name__ == "__main__":
    host_name = "0.0.0.0"
    server_port = 80
    web_server = HTTPServer((host_name, server_port), DemoAppServer)
    print(f"Server started at http://{host_name}:{server_port}")
    web_server.serve_forever()
