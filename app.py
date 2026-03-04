from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///visits.db'
db = SQLAlchemy(app)

class Visit(db.Model):
    id = db.Column(db.Integer, primary_key=True)

with app.app_context():
    db.create_all()

@app.route("/")
def home():
    new_visit = Visit()
    db.session.add(new_visit)
    db.session.commit()
    count = Visit.query.count()
    return render_template("index.html", name="Ali", count=count)

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)