from flask import Flask, request, render_template
import os
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/diagnostic')
def diagnostic():
    return render_template('diagnostic.html')

@app.route('/api/ping', methods=['POST'])
def ping():
    target = request.form.get('target', '')
    
    if not target:
        return "Target cannot be empty!", 400

    try:
        command = f"ping -c 3 -n {target}"
        process = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        return render_template('diagnostic.html', output=process.stdout, target=target)
    except Exception as e:
        return render_template('diagnostic.html', output=f"Unexpected Error: {str(e)}", target=target)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
