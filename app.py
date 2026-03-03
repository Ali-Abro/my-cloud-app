from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from my cloud app!"

@app.route("/about")
def about():
    return "This is Ali's first cloud deployment."

if __name__ == "__main__":
    app.run(debug=True)