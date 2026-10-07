from http.server import BaseHTTPRequestHandler
from datetime import datetime

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # 1. Set Header sebagai HTML
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()

        # 2. Server time & metadata dari Python
        server_time = datetime.now().strftime("%d %B %Y, %H:%M:%S UTC")

        # 3. Template HTML dengan Rich Modern Aesthetics (Glassmorphism, Dark UI, Animations)
        html_content = f"""<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Python Web App | Deployed on Vercel</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        :root {{
            --bg-primary: #0a0e17;
            --bg-secondary: #121826;
            --card-bg: rgba(26, 34, 52, 0.7);
            --card-border: rgba(255, 255, 255, 0.08);
            --text-main: #f8fafc;
            --text-muted: #94a3b8;
            --accent-python: #38bdf8;
            --accent-gold: #facc15;
            --accent-glow: rgba(56, 189, 248, 0.25);
            --gradient-accent: linear-gradient(135deg, #38bdf8 0%, #818cf8 50%, #c084fc 100%);
        }}

        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: 'Plus Jakarta Sans', sans-serif;
            background-color: var(--bg-primary);
            color: var(--text-main);
            min-height: 100vh;
            overflow-x: hidden;
            display: flex;
            flex-direction: column;
            background-image: 
                radial-gradient(circle at 15% 15%, rgba(56, 189, 248, 0.12) 0%, transparent 40%),
                radial-gradient(circle at 85% 85%, rgba(192, 132, 252, 0.12) 0%, transparent 40%);
        }}

        /* Navbar */
        nav {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 1.5rem 8%;
            background: rgba(10, 14, 23, 0.85);
            backdrop-filter: blur(16px);
            border-bottom: 1px solid var(--card-border);
            position: sticky;
            top: 0;
            z-index: 100;
        }}

        .logo {{
            font-family: 'Outfit', sans-serif;
            font-weight: 800;
            font-size: 1.4rem;
            display: flex;
            align-items: center;
            gap: 10px;
            color: #fff;
            text-decoration: none;
        }}

        .logo span {{
            background: var(--gradient-accent);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}

        .nav-badge {{
            display: inline-flex;
            align-items: center;
            gap: 8px;
            padding: 6px 14px;
            background: rgba(34, 197, 94, 0.12);
            border: 1px solid rgba(34, 197, 94, 0.3);
            border-radius: 9999px;
            font-size: 0.85rem;
            color: #4ade80;
            font-weight: 600;
        }}

        .status-dot {{
            width: 8px;
            height: 8px;
            background-color: #22c55e;
            border-radius: 50%;
            box-shadow: 0 0 10px #22c55e;
            animation: pulse 2s infinite;
        }}

        @keyframes pulse {{
            0%, 100% {{ transform: scale(1); opacity: 1; }}
            50% {{ transform: scale(1.4); opacity: 0.6; }}
        }}

        /* Hero Section */
        main {{
            flex: 1;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            padding: 4rem 8%;
            text-align: center;
        }}

        .hero-pill {{
            display: inline-flex;
            align-items: center;
            gap: 8px;
            padding: 6px 18px;
            background: rgba(56, 189, 248, 0.1);
            border: 1px solid rgba(56, 189, 248, 0.25);
            border-radius: 9999px;
            font-size: 0.9rem;
            color: var(--accent-python);
            margin-bottom: 1.5rem;
            font-weight: 500;
        }}

        h1 {{
            font-family: 'Outfit', sans-serif;
            font-size: clamp(2.4rem, 5vw, 3.8rem);
            font-weight: 800;
            line-height: 1.15;
            max-width: 800px;
            margin-bottom: 1.25rem;
            letter-spacing: -0.02em;
        }}

        h1 .highlight {{
            background: var(--gradient-accent);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}

        p.hero-desc {{
            font-size: 1.15rem;
            color: var(--text-muted);
            max-width: 600px;
            line-height: 1.7;
            margin-bottom: 2.5rem;
        }}

        /* Feature Cards Grid */
        .cards-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 1.5rem;
            width: 100%;
            max-width: 1000px;
            margin-top: 1.5rem;
        }}

        .card {{
            background: var(--card-bg);
            border: 1px solid var(--card-border);
            border-radius: 16px;
            padding: 2rem 1.5rem;
            text-align: left;
            backdrop-filter: blur(12px);
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            position: relative;
            overflow: hidden;
        }}

        .card::before {{
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 2px;
            background: var(--gradient-accent);
            opacity: 0;
            transition: opacity 0.3s ease;
        }}

        .card:hover {{
            transform: translateY(-6px);
            border-color: rgba(56, 189, 248, 0.3);
            box-shadow: 0 16px 32px rgba(0, 0, 0, 0.4), 0 0 20px var(--accent-glow);
        }}

        .card:hover::before {{
            opacity: 1;
        }}

        .card-icon {{
            font-size: 2rem;
            margin-bottom: 1rem;
            display: inline-block;
        }}

        .card h3 {{
            font-family: 'Outfit', sans-serif;
            font-size: 1.25rem;
            font-weight: 700;
            margin-bottom: 0.5rem;
            color: #fff;
        }}

        .card p {{
            font-size: 0.95rem;
            color: var(--text-muted);
            line-height: 1.6;
        }}

        /* Interactive Action Box */
        .interactive-box {{
            margin-top: 3rem;
            background: linear-gradient(135deg, rgba(30, 41, 59, 0.8) 0%, rgba(15, 23, 42, 0.9) 100%);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 20px;
            padding: 2rem;
            max-width: 650px;
            width: 100%;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.5);
        }}

        .code-preview {{
            background: #050811;
            border-radius: 10px;
            padding: 1rem 1.25rem;
            text-align: left;
            font-family: 'Courier New', Courier, monospace;
            font-size: 0.9rem;
            color: #38bdf8;
            margin-top: 1rem;
            border: 1px solid rgba(255, 255, 255, 0.05);
            overflow-x: auto;
        }}

        /* Footer */
        footer {{
            text-align: center;
            padding: 2rem 8%;
            border-top: 1px solid var(--card-border);
            color: var(--text-muted);
            font-size: 0.9rem;
        }}

        .cta-btn {{
            display: inline-block;
            margin-top: 1rem;
            padding: 12px 28px;
            background: var(--gradient-accent);
            color: #0b0f19;
            font-weight: 700;
            border-radius: 12px;
            text-decoration: none;
            transition: transform 0.2s, box-shadow 0.2s;
        }}

        .cta-btn:hover {{
            transform: scale(1.04);
            box-shadow: 0 10px 20px rgba(56, 189, 248, 0.4);
        }}
    </style>
</head>
<body>

    <!-- Header / Navbar -->
    <nav>
        <a href="/" class="logo">
            <span>🐍 PythonApp</span>
        </a>
        <div class="nav-badge">
            <span class="status-dot"></span>
            Serverless Live
        </div>
    </nav>

    <!-- Main Hero -->
    <main>
        <div class="hero-pill">
            ⚡ Powered by Python & Vercel
        </div>
        <h1>Website Keren Ini Dijalankan Langsung oleh <span class="highlight">Python</span></h1>
        <p class="hero-desc">
            Bukan cuma JSON, file Python Anda sekarang me-render halaman web visual modern secara langsung dari serverless backend.
        </p>

        <!-- Feature Grid -->
        <div class="cards-grid">
            <div class="card">
                <div class="card-icon">⚡</div>
                <h3>Super Ringan & Cepat</h3>
                <p>Menggunakan standard library bawaan Python tanpa ketergantungan library luar, membuat cold start hampir instan.</p>
            </div>
            <div class="card">
                <div class="card-icon">☁️</div>
                <h3>Serverless di Vercel</h3>
                <p>Otomatis scaling secara dinamis dari nol request hingga jutaan request tanpa perlu manage server fisik.</p>
            </div>
            <div class="card">
                <div class="card-icon">⏱️</div>
                <h3>Server-Side Rendered</h3>
                <p>Waktu server saat halaman ini di-render: <br><strong style="color:#facc15;">{server_time}</strong></p>
            </div>
        </div>

        <!-- Interactive Info Box -->
        <div class="interactive-box">
            <h3 style="font-family:'Outfit'; font-size:1.3rem; margin-bottom:0.5rem;">🔥 Full Python Controller</h3>
            <p style="color:var(--text-muted); font-size:0.95rem;">File Python <code>api/index.py</code> yang Anda minta menangani request HTTP dan langsung menyajikan tampilan HTML interaktif ini ke browser.</p>
            
            <div class="code-preview">
                # Rendered by Python handler<br>
                status: 200 OK<br>
                content-type: text/html<br>
                engine: Python 3.x on Vercel
            </div>

            <a href="/api" class="cta-btn" id="refreshBtn">Reload Website 🚀</a>
        </div>
    </main>

    <!-- Footer -->
    <footer>
        <p>&copy; 2026 Nixon Daniel • Deployed on Vercel with Python</p>
    </footer>

</body>
</html>"""

        # 4. Kirim HTML ke client
        self.wfile.write(html_content.encode('utf-8'))
        return
