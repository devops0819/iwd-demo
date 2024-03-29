from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def hello_world():
    status_code = random.choice([200, 200, 200, 404, 500])
    return 'Hello, World!', status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

