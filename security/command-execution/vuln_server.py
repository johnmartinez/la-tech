from http.server import BaseHTTPRequestHandler, HTTPServer
import subprocess
import urllib.parse

HOST = 'localhost'
PORT = 8080

class VulnerableServer(BaseHTTPRequestHandler):
    def do_GET(self):
        # Parse user input from the query string
        parsed_path = urllib.parse.urlparse(self.path)
        query_params = urllib.parse.parse_qs(parsed_path.query)
        command = query_params.get("cmd", [""])[0]  # Get the "cmd" parameter

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        try:
            # Simulate a command injection vulnerability
            result = subprocess.check_output(command, shell=True, text=True)
            self.wfile.write(f"<h1>Command Output:</h1><pre>{result}</pre>".encode())
        except Exception as e:
            self.wfile.write(f"<h1>Error:</h1><pre>{e}</pre>".encode())

        return

if __name__ == "__main__":
    print(f"Starting vulnerable server at http://{HOST}:{PORT}")
    server = HTTPServer((HOST, PORT), VulnerableServer)
    server.serve_forever()
