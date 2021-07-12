from flask import Flask, url_for, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'hello'

@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect("/")

@app.route('/')
def home():
    if "count" in session:
        session["count"] += 1
    else:
        session["count"] = 1
    return render_template("index.html", times= session["count"])

@app.route('/plus')
def plus():
    session["count"] += 1
    return redirect('/')



if __name__ == "__main__":
    app.run(debug=True)  




