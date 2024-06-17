import http.server
import socketserver
import pyqrcode
import png
import os
import socket
import webbrowser

# Assign Port Number and User Name
PORT = 8000
USER_NAME = "YourName"

# Obtain the IP Address of the PC
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

# Convert the IP Address into a QR Code
url = f"http://{IPAddr}:{PORT}"
qr = pyqrcode.create(url)
qr.png("qrcode.png", scale=8)

# Create an HTTP Request Handler to Handle File Sharing
class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

# Display the QR Code in a Web Browser
webbrowser.open("qrcode.png")

# Implement File Sharing Functionality by Serving Files Over HTTP
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at port {PORT}")
    print(f"Access the shared files at: {url}")
    httpd.serve_forever()
