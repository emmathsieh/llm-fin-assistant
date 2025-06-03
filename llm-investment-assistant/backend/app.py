from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    question = data.get("question", "")
    # Later: use LLM here
    return jsonify({"answer": f"Your question was: {question}"})

if __name__ == "__main__":
    app.run(port=5000)