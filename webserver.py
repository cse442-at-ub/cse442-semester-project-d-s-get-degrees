from backend.modules import app
from flask import render_template, Flask, send_from_directory

app=Flask(__name__)

@app.route("/css/<path:path>", methods=['GET', 'POST'])
def route_css(path):
    return send_from_directory("frontend/css", path)

@app.route("/images/<path:path>", methods=['GET', 'POST'])
def route_image(path):
    return send_from_directory("frontend/images", path)

@app.route("/<path:path>", methods=['GET', 'POST'])
def route_html(path):
    return send_from_directory("frontend", path)

@app.route("/", methods=['GET', 'POST'])
def route_index():
    return send_from_directory("frontend", "index.html")

app.run (port = 8080)

if __name__ == "__main__":
    app.run(debug=True)
