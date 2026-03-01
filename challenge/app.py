from flask import Flask, request, render_template
import os
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/ping', methods=['POST'])
def ping():
    target = request.form.get('target', '')
    
    # Simple check for empty target
    if not target:
        return "Target cannot be empty!", 400

    # Vulnerability: user-supplied 'target' is directly passed into shell command
    # I'll use a slightly more 'professional' looking subprocess.check_output 
    # to mask the simplicity of the vulnerability.
    try:
        # We only want to ping 3 times to prevent hanging
        command = f"ping -c 3 {target}"
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, text=True)
        return render_template('index.html', output=output, target=target)
    except subprocess.CalledProcessError as e:
        return render_template('index.html', output=f"Error: {e.output}", target=target)
    except Exception as e:
        return render_template('index.html', output=f"Unexpected Error: {str(e)}", target=target)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
