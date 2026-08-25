#!/usr/bin/env python3
"""Run local HTTP server for Google Timeline visualization."""

import http.server
import socketserver
import os
import sys

DIR = os.path.dirname(os.path.abspath(__file__))
PORT = 1300

os.chdir(DIR)

Handler = http.server.SimpleHTTPRequestHandler

try:
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Server running at http://localhost:{PORT}")
        print("Buka di browser, tekan Ctrl+C untuk berhenti.")
        httpd.serve_forever()
except KeyboardInterrupt:
    print("\nServer stopped.")
except OSError as e:
    print(f"Error: {e}")
    print(f"Coba port lain: python3 {sys.argv[0]} 8080")
    sys.exit(1)
