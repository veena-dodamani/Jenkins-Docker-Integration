from http.server import BaseHTTPRequestHandler, HTTPServer
import socket

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            db_status = "Connected"
            try:
                with socket.create_connection(("db", 3306), timeout=3):
                    pass
            except OSError:
                db_status = "Not Connected"

            response = f"Backend: Connected\nDatabase: {db_status}\n"
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(response.encode())
        else:
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Backend container is running successfully!")

server = HTTPServer(("0.0.0.0", 5000), Handler)
print("Backend running on port 5000")
server.serve_forever()
