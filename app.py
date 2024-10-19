from flask import Flask
from datetime import datetime
import os
import getpass
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    try:
        name = "S Veerendar"
        username = getpass.getuser()
        server_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S IST')

        top_output = subprocess.check_output(['ps', 'aux']).decode('utf-8')

        html_content = f"""
        <p><strong>Name:</strong> {name}</p>
        <p><strong>Username:</strong> {username}</p>
        <p><strong>Server Time (IST):</strong> {server_time}</p>
        <p><strong>Top Output :</strong></p>
        <pre>{top_output}</pre>
        """
        return html_content

    except Exception as e:
        return f"<h1>Internal Server Error</h1><p>{str(e)}</p>", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
