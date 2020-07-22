from flask import Flask, render_template
app = Flask(__name__, static_url_path='/static')

@app.route("/")
def makeCheckerboard():
    return render_template("index.html", x_times=8, y_times=8)

@app.route("/<int:y>")
def inputCheckerboard(y):
    return render_template("index.html", y_times=int(y), x_times=4)

@app.route("/<int:y>/<int:x>")
def xyInput(y,x):
    return render_template("index.html", y_times=int(y), x_times=int(x))

if __name__=="__main__":
    app.run(debug=True)