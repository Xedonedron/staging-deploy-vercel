from http.server import BaseHTTPRequestHandler
import json

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # 1. Kirim HTTP status 200 OK
        self.send_response(200)
        
        # 2. Header response (JSON)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
        # 3. Data response
        response_data = {
            "status": "success",
            "message": "Halo! Python berhasil jalan di Vercel! 🐍🚀",
            "author": "Nixon Daniel",
            "runtime": "Python Serverless Function (No extra packages needed)"
        }
        
        # 4. Kirim response ke browser/client
        self.wfile.write(json.dumps(response_data, ensure_ascii=False).encode('utf-8'))
        return
