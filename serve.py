#!/usr/bin/env python3
"""Simple HTTP server for the Snippeter web frontend."""

import http.server
import socketserver
import webbrowser
from pathlib import Path

PORT = 8000

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add CORS headers
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        super().end_headers()

def serve():
    """Start the HTTP server and open the browser."""
    # Change to the script directory
    script_dir = Path(__file__).parent

    with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
        url = f"http://localhost:{PORT}/index.html"
        print(f"Server running at {url}")
        print(f"Press Ctrl+C to stop the server")
        print(f"\nServing {len(list(script_dir.glob('*.html')))} HTML file(s)")
        print(f"Snippets data: snippets.json")

        # Open browser
        try:
            webbrowser.open(url)
        except Exception as e:
            print(f"Could not open browser: {e}")
            print(f"Please navigate to {url} manually")

        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\nServer stopped.")

if __name__ == "__main__":
    serve()
