from flask import Flask, render_template, request, redirect, session
app = Flask(__name__, static_url_path='/static')
app.secret_key="Titanic1912!"

@app.route('/')
def mainCount():
    if 'count' in session:
        session['count'] = session.get('count') + 1
    else:
        session['count'] = 1 
    return render_template("counter.html", counter=session['count'])

@app.route('/add_2')
def add_two():
    if 'count' in session: 
        session['count'] = session.get('count')+1
    return redirect("/")

@app.route('/destroy_session')
def destroySession():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)