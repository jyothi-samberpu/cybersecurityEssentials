import http.server
import socket
import socketserver
import requests

# Proxy Server Configuration
LOG_FILE = "proxy_log.txt"

def get_available_port(start_port: int, max_tries: int = 50) -> int:
    """Finds an available TCP port starting from start_port."""
    port = start_port
    for _ in range(max_tries):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            try:
                sock.bind(("", port))
                return port
            except OSError:
                port += 1
    raise RuntimeError("No available port found.")

PROXY_PORT = get_available_port(8080)

class ProxyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    """Custom HTTP Proxy Handler that logs requests"""

    def do_GET(self):
        """Handle GET requests through the proxy"""
        self.log_request_details()
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Proxy Request Received.")

    def log_request_details(self):
        """Logs request details to a file"""
        client_ip = self.client_address[0]
        requested_url = self.path

        log_entry = f"Client IP: {client_ip} -> Request: {requested_url}\n"
        print(log_entry)  # Print to console
        with open(LOG_FILE, "a") as log_file:
            log_file.write(log_entry)

class ReusableTCPServer(socketserver.TCPServer):
    allow_reuse_address = True

# Start the Proxy Server
def start_proxy():
    """Starts an HTTP proxy server"""
    with ReusableTCPServer(("", PROXY_PORT), ProxyHTTPRequestHandler) as server:
        print(f"[*] Proxy Server Running on port {PROXY_PORT}")
        server.serve_forever()

if __name__ == "__main__":
    start_proxy()

PROXY = f"http://127.0.0.1:{PROXY_PORT}"  # Local proxy

proxies = {
    "http": PROXY,
    "https": PROXY,  # For HTTPS requests
}

target_url = "http://example.com"

try:
    response = requests.get(target_url, proxies=proxies)
    print(f"Response Status: {response.status_code}")
except Exception as e:
    print(f"Error: {e}")
