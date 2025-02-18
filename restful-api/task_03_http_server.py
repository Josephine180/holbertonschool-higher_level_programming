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
        if self.path == '/favicon.ico':
            self.send_response(204)
            self.end_headers()
            return
        elif self.path == "/":
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
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
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b"OK")
        elif self.path == '/info':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = {
                'version': '1.0',
                'description': 'A simple API built with http.server'
            }
            self.wfile.write(json.dumps(response).encode('utf-8'))
        else:
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            error_message = {"error": "Endpoint not found"}
            self.wfile.write(json.dumps(error_message).encode('utf-8'))


def run():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, SimpleAPIHandler)
    print("Serveur démarré sur http://localhost:8000")
    httpd.serve_forever()


if __name__ == '__main__':
    run()