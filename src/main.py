from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello():
    return "Hello World! V1"

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080,debug=True)
