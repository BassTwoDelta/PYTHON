from flask import Flask, render_template, request, redirect
app = Flask(__name__, static_url_path='/static')

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/users", methods=["POST"])
def create():
    print("Got Post Info")
    print(request.form)
    name_from_form = request.form['name']
    location_from_form = request.form['location']
    lang_from_form = request.form['favorite_lang']
    comment_from_form = request.form['comment']
    return render_template('result.html', result_name=name_from_form, result_location=location_from_form, result_fav_lang=lang_from_form, result_comment=comment_from_form)

if __name__ == "__main__":
    app.run(debug=True)