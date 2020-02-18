from backend.modules import app,render_template,redirect,url_for

@app.route("/logout")
def logout():
    # logout_user()
    return redirect(url_for('home'))

@app.route("/register")
def index():
    return render_template("register.html")

@app.route("/login")
def index():
    return render_template("login.html")