from flask import Flask, render_template, request, redirect, session
app = Flask(__name__, static_url_path='/static')
app.secret_key="Titanic1912!"

@app.route('/', methods=['GET','POST'])
def index():
    import random
    session['randomInt'] = random.randint(1,100) 
    print(session['randomInt'])
    return render_template('index.html')

@app.route("/num_check", methods=['POST'])
def numberCheck():

    if int(request.form['numberGuess']) < session['randomInt']:
        return render_template('index2.html')

    if int(request.form['numberGuess']) > session['randomInt']:
        return render_template('index3.html')

    else:
        return render_template('index4.html')
        
if __name__ == "__main__":
    app.run(debug=True)