from flask import Flask, render_template, request, redirect
app = Flask(__name__)
# our index route will handle rendering our form
@app.route('/')
def index():
    return render_template("index.html")
if __name__ == "__main__":
    app.run(debug=True)

@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    # print(request.form)
    # name_from_form = request.form['name']
    # email_from_form = request.form['email']
    return render_template("show.html")
