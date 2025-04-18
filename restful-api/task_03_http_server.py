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
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
class SimpleAPIHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Ignorer la requête du favicon pour éviter une erreur 404
        if self.path == "/":
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
        elif self.path == "/data":
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode('utf-8'))
        elif self.path == "/status":
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')  # Correction ici
            self.end_headers()
            self.wfile.write(b"OK")
        elif self.path == "/info":
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            self.wfile.write(json.dumps(response).encode('utf-8'))
        else:
            self.send_response(404)
            self.send_header('Content-type', 'texte/html')
            self.end_headers()
            self.wfile.write(b"Endpoint not found")
            
def run(server_class=HTTPServer, handler_class=SimpleAPIHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Début d'API sur le port {port}")
    httpd.serve_forever()
if __name__ == '__main__':
    run()