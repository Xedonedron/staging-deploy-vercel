from http.server import BaseHTTPRequestHandler
import json
from datetime import datetime

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # 1. Kirim HTTP status 200 OK
        self.send_response(200)
        
        # 2. Set header JSON dan CORS agar bisa dipanggil dari frontend
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        
        # 3. Data balasan dari Python
        response_data = {
            "status": "success",
            "message": "Halo! Python backend berhasil dieksekusi di Vercel! 🐍🚀",
            "server_time": datetime.now().strftime("%d %B %Y, %H:%M:%S UTC"),
            "environment": "Vercel Serverless Function",
            "python_runtime": "Standard Library (Zero Dependency)"
        }
        
        # 4. Kirim response
        self.wfile.write(json.dumps(response_data, ensure_ascii=False).encode('utf-8'))
        return
