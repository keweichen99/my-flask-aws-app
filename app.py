from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Flask is running on AWS!"

if __name__ == "__main__":
    # 注意：在云服务器上必须监听 0.0.0.0
    app.run(host='0.0.0.0', port=5000)
