from backend.modules import app
from flask import render_template

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/profile")
def index():
    return render_template("profile.html")

@app.route("/home")
def index():
    return render_template("home.html")


@app.route("/admin")
def index():
    return render_template("admin.html")

if __name__ == "__main__":
    app.run(debug=True)