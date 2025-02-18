#!/usr/bin/env python3
"""
Module `task_03_http_server`

Ce module implémente une API HTTP simple à
l'aide du module `http.server` de la bibliothèque standard de Python.

Fonctionnalités :
- `/`        : Retourne un message de bienvenue.
- `/data`    : Retourne un objet JSON contenant des informations fictives.
- `/status`  : Retourne "OK" pour vérifier l'état du serveur.
- `/info`    : Retourne des informations sur l'API.
- Autres routes : Retourne une erreur `404 Not Found`.

"""

import http.server
import json
import BaseHTTPRequestHandler

class SimpleAPI(BaseHTTPRequestHandler):
    def do_GET(self):
        """Gère les requêtes GET et route vers le bon endpoint."""
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.end_headers()
        if content:
            self.wfile.write(content.encode('utf-8'))
        
        if self.path == "/":
            self._send_response(HTTPStatus.OK, "Hello, this is a simple API!")
        
        elif self.path == "favicon.ico":
            self._send_response(HTTPStatus.NO_CONTENT)

        elif self.path == "/data":
            data = {"name": "John", "age": 30, "city": "New York"}
            self._send_response(HTTPStatus.OK, json.dumps(data), content_type="application/json")

        elif self.path == "/status":
            self._send_response(HTTPStatus.OK, "OK")

        elif self.path == "/info":
            info = {"version": "1.0", "description": "A simple API built with http.server"}
            self._send_response(HTTPStatus.OK, json.dumps(info), content_type="application/json")

        else:
            self._send_response(HTTPStatus.NOT_FOUND, "404 Not Found")

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8000):
    """Démarre le serveur HTTP sur le port spécifié."""
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print(f"Server running on port {port}...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
