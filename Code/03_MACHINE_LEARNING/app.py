from flask import Flask

app = Flask(__name__)

@app.route('/ml')
def ml_home():
    return "Welcome to the Machine Learning App!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
