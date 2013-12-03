from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/')
def hello_module():
    return send_from_directory('module_sendfrom_dir', 'sendme_module.txt')

app.run(debug=True)
