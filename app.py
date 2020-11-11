from flask import Flask
import time
import os
app = Flask(__name__, static_folder="./build", static_url_path='/')


@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/api')
def get_current_time():
    res = os.system('python3 connection.py')
    return {'msg': res}

if __name__ == '__main__':
    app.run()