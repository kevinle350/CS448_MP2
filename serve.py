from flask import Flask, request
import subprocess
import socket

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def serve():
    if request.method == 'POST':
        subprocess.Popen(['python', 'stress_cpu.py'])
        return 'CPU stress script started', 200
    else:
        hostname = socket.gethostname()    
        IPAddr = socket.gethostbyname(hostname)    
        return IPAddr

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=5000)
