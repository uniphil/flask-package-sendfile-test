import os
from flask import Flask, send_from_directory, send_file

app = Flask(__name__)

@app.route('/')
def hello_package():
    return send_from_directory('package_sendfrom_dir', 'sendme_package.txt')

@app.route('/from-up-one')
def hello_package2():
    return send_from_directory('package_app/package_sendfrom_dir', 'sendme_package.txt')

@app.route('/sendfile-nosafejoin')
def hello_package3():
    path = os.path.join('package_sendfrom_dir', 'sendme_package.txt')
    return send_file(path)
