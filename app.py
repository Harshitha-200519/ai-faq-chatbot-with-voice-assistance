from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

faqs = {
    "what is ai": "AI means Artificial Intelligence.",
    "what is python": "Python is a programming language.",
    "what is flask": "Flask is a Python web framework."
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_msg = request.json['message'].lower()

    response = "Sorry, I don't know that."

    for key in faqs:
        if key in user_msg:
            response = faqs[key]

    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)