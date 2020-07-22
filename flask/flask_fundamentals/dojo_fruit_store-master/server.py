from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    strawberry = request.form['strawberry']
    raspberry = request.form['raspberry']
    apple = request.form['apple']
    blackberry = request.form['blackberry']
    first_name= request.form['first_name']
    last_name = request.form['last_name']
    student_id = request.form['student_id']
    totalCount= (int(strawberry) + int(raspberry) + int(apple) + int(blackberry))
    if student_id != '':
        print(f'Charging { first_name }, with student ID number:{student_id}, for { totalCount } fruits')
    else: 
        print(f"Charging { first_name } for {totalCount} fruits")
    return render_template("checkout.html", strawberry_amnt=int(strawberry), raspberry_amnt=int(raspberry), apple_amnt=int(apple), blackberry_amnt=int(blackberry), firstName=first_name, lastName=last_name, studentID=student_id, total=totalCount)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    