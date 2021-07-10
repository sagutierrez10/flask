from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def index():
    return render_template('index.html', times=3)  

@app.route('/play/<id>')
def repeat(id):
    return render_template('index.html', times= int(id))  

@app.route('/play/<id>/<string:color>')
def color(id, color):
    return render_template('index.html', times= int(id), color= color)  

if __name__=="__main__":
    app.run(debug=True)