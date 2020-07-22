from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def addPlay():
    return "Please add play after the forward slash to continue"

@app.route('/play')
def boxes():
    return render_template("index.html")

@app.route('/play/<int:num>')
def num_boxes(num):
    return render_template("index2.html", times=num)

@app.route('/play/<int:num>/<color>')
def color_box(num,color): 
    return render_template("index3.html", boxes=num, colorVar=color)


if __name__=="__main__":
    app.run(debug=True)