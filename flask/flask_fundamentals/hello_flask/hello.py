from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__) # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def index():
    return render_template("index.html", phrase="hello", times=5)

@app.route('/dojo') # prints Dojo 
def dojo():
    return "Dojo"

@app.route('/say/<word>') # prints Hi and then whatever word is entered
def word(word):
    print(word)
    return "Hi "+ word +"!"

@app.route('/repeat/<int:num>/<word>') #repeats the word int:num amount of times
def repeat(num,word):
    print(word)
    return word * num

@app.route('/success')
def success():
    return "success"

@app.route('/hello/<name>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
def hello(name):
    print(name)
    return "Hello, " + name

@app.route('/users/<username>/<id>') # for a route '/users/____/____', two parameters in the url get passed as username and id
def show_user_profile(username, id):
    print(username)
    print(id)
    return "username: " + username + ", id: " + id

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
