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
        if self.path == "/":
            self.send_text_response("Hello, this is a simple API!")
        elif self.path == "/data":
            data = {"name": "John", "age": 30, "city": "New York"}
            self.send_json_response(data)
        elif self.path == "/status":
            self.send_text_response("OK")
        elif self.path == '/info':
            info = {"version": "1.0", "description": "A simple API built with http.server"}
            self.send_json_response(info)
        else:
            error_message = {"error": "Endpoint not found"}
            self.send_json_response(error_message, status=404)
     def send_text_response(self, message, status=200):
        """
        Envoie une réponse en texte brut.

        :param message: Texte de la réponse.
        :param status: Code HTTP (200 par défaut).
        """
        self.send_response(status)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write(message.encode("utf-8"))

    def send_json_response(self, data, status=200):
        """
        Envoie une réponse JSON.

        :param data: Dictionnaire à envoyer sous forme de JSON.
        :param status: Code HTTP (200 par défaut).
        """
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode("utf-8"))

def run():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, SimpleAPIHandler)
    print("Serveur démarré sur http://localhost:8000")
    httpd.serve_forever()


if __name__ == '__main__':
    run()