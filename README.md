<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>Turtle Art & Login System — README</title>
  <style>
    :root{--bg:#0f1724;--card:#0b1220;--muted:#94a3b8;--accent:#fbbf24;--mono:Consolas,monaco,monospace}
    body{font-family:Inter,system-ui,Segoe UI,Roboto,"Helvetica Neue",Arial,sans-serif;background:linear-gradient(180deg,#04050b 0%,#071025 100%);color:#e6eef8;margin:0;padding:40px}
    .wrap{max-width:980px;margin:0 auto}
    header{display:flex;gap:16px;align-items:center}
    header .badge{background:var(--accent);color:#071025;padding:8px 12px;border-radius:10px;font-weight:700}
    h1{margin:6px 0 0;font-size:26px}
    p.lead{color:var(--muted);margin-top:6px}
    .grid{display:grid;grid-template-columns:1fr 320px;gap:24px;margin-top:28px}
    .card{background:linear-gradient(180deg,rgba(255,255,255,0.02),rgba(255,255,255,0.01));border:1px solid rgba(255,255,255,0.03);padding:20px;border-radius:12px;box-shadow:0 6px 30px rgba(2,6,23,0.6)}
    .card h2{margin-top:0}
    pre{background:#051226;color:#cfe9ff;padding:14px;border-radius:8px;overflow:auto;font-family:var(--mono);font-size:13px}
    code{background:rgba(255,255,255,0.02);padding:2px 6px;border-radius:6px}
    ul.meta{padding-left:18px;color:var(--muted)}
    .actions{display:flex;gap:8px;flex-wrap:wrap;margin-top:12px}
    a.btn{background:transparent;border:1px solid rgba(255,255,255,0.06);padding:8px 12px;border-radius:10px;color:var(--accent);text-decoration:none;font-weight:600}
    .right{position:sticky;top:24px}
    footer{margin-top:28px;color:var(--muted);font-size:13px;text-align:center}
    .note{background:rgba(255,255,255,0.02);border-left:4px solid rgba(255,191,36,0.18);padding:10px;margin:12px 0;border-radius:6px;color:var(--muted)}
    details{margin-top:8px}
  </style>
</head>
<body>
  <div class="wrap">
    <header>
      <div class="badge">Turtle & Login</div>
      <div>
        <h1>Turtle Art &amp; Login System — Combined README</h1>
        <p class="lead">Two small Python projects documented in a single friendly HTML README: a Turtle art script and a CLI login demo.</p>
      </div>
    </header>

    <div class="grid">
      <main class="card">
        <h2>📌 Overview</h2>
        <p>The repository contains two independent Python projects that live together for convenience:</p>
        <ol>
          <li><strong>Turtle Art Drawing Project</strong> — an intricate drawing made using <code>turtle</code>.</li>
          <li><strong>Login System Project</strong> — a command-line username/password demo with playful feedback messages and loading effects.</li>
        </ol>

        <section>
          <h3>🖼️ Turtle Art Drawing Project</h3>
          <p>This script uses multiple <code>turtle.Turtle()</code> objects to compose an elaborate scene. It demonstrates layered pen sizes, filled shapes, arcs and circles to form characters and decorative elements.</p>

          <h4>How to run</h4>
          <pre><code>python turtle_art.py</code></pre>

          <h4>Notes</h4>
          <ul class="meta">
            <li>Requires: Python (built-in <code>turtle</code> module).</li>
            <li>Run in a desktop environment (turtle opens a GUI window).</li>
            <li>Expect the drawing to take time due to its level of detail; you can speed it by setting turtle speed to a higher value (e.g. <code>turtle.speed(0)</code>).</li>
          </ul>

          <details>
            <summary><strong>Example filename</strong></summary>
            <pre><code>turtle_art.py</code></pre>
          </details>
        </section>

        <section style="margin-top:18px">
          <h3>🔐 Login System Project</h3>
          <p>A simple CLI authentication example that uses hard-coded credentials and prints creative messages depending on the authentication result.</p>

          <h4>How to run</h4>
          <pre><code>python login.py</code></pre>

          <h4>Credentials (example)</h4>
          <pre><code>username = 'tcm9798'
password = 'tcm123456'</code></pre>

          <h4>Behavior</h4>
          <ul class="meta">
            <li>Correct credentials -> prints a multi-stage loading sequence.</li>
            <li>Correct username, wrong password -> password-specific message.</li>
            <li>Wrong username, correct password -> username-specific message.</li>
            <li>Both wrong -> generic retry message.</li>
          </ul>

          <details>
            <summary><strong>Example filename</strong></summary>
            <pre><code>login.py</code></pre>
          </details>
        </section>

        <section style="margin-top:18px">
          <h3>📂 Suggested repository structure</h3>
          <pre><code>project/
├── turtle_art.py
├── login.py
└── README.html</code></pre>

          <h4>Requirements</h4>
          <ul class="meta">
            <li>Python 3.x</li>
            <li>No external libraries needed (uses built-ins: <code>turtle</code>, <code>time</code>).</li>
          </ul>
        </section>

        <section style="margin-top:18px">
          <h3>🛠️ Tips & Improvements</h3>
          <ul class="meta">
            <li>Refactor turtle drawing into functions for easier maintenance.</li>
            <li>Split the large turtle script into modular parts (face, hair, decorations).</li>
            <li>For the login script, consider replacing hard-coded credentials with a hashed credentials file for safety when practicing.</li>
            <li>Add command-line flags to run either project separately (e.g., <code>python -m project --turtle</code>).</li>
          </ul>
        </section>

      </main>

      <aside class="right card">
        <h2>Quick Actions</h2>
        <div class="actions">
          <a class="btn" href="#turtle">Jump to Turtle Art</a>
          <a class="btn" href="#login">Jump to Login System</a>
          <a class="btn" href="#download" onclick="downloadREADME()">Download README</a>
        </div>

        <div class="note">
          This HTML README is self-contained and printable. Use the download button to save a <code>README.html</code> copy locally.
        </div>

        <h3 style="margin-top:12px">Commands</h3>
        <pre><code>python turtle_art.py
python login.py</code></pre>

        <h3 style="margin-top:12px">License</h3>
        <p class="meta">MIT-style — feel free to copy, modify, and remix.</p>
      </aside>
    </div>

    <footer>
      Created for you — open the file in a browser to view. Want this split into two pages or exported to PDF? I can do that next.
    </footer>
  </div>

  <script>
    function downloadREADME(){
      const html = document.documentElement.outerHTML;
      const blob = new Blob([html], {type: 'text/html'});
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = 'README.html';
      document.body.appendChild(a);
      a.click();
      a.remove();
      URL.revokeObjectURL(url);
    }
  </script>
</body>
</html>
