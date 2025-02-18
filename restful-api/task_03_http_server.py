#!/usr/bin/python3
import http.server
import json
from http import HTTPServer, BaseHTTPRequestHandler


PORT = 8080
Handler = http.server.BaseHTTPRequestHandler

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
                    self.send_response(HTTPStatus.OK)
                    self.send_header("Content-type", "text/plain")
                    self.end_headers()
                    self.wfile.write(b"Hello, this is a simple API!")

                elif self.path == "/data":
                    self.send_response(HTTPStatus.OK)
                    self.send_header("Content-type", "application/json")
                    self.end_headers()
                    
                    # Données JSON à envoyer
                    data = {"name": "John", "age": 30, "city": "New York"}
                    self.wfile.write(json.dumps(data).encode("utf-8"))

                elif self.path == "/status":
                    self.send_response(HTTPStatus.OK)
                    self.send_header("Content-type", "text/plain")
                    self.end_headers()
                    self.wfile.write(b"OK")

                else:
                    self.send_response(HTTPStatus.NOT_FOUND)
                    self.send_header("Content-type", "text/plain")
                    self.end_headers()
                    self.wfile.write(b"404 Not Found: The requested resource does not exist.")

        if __name__ == "__main__":
            # Lancer le serveur sur le port 8000
            server_address = ("", 8000)
            httpd = http.server.HTTPServer(server_address, SimpleHTTPRequestHandler)
            print("Serveur en cours d'exécution sur le port 8000...")
            httpd.serve_forever()
