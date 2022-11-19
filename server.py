from flask import Flask, render_template, redirect, request
from users import User
app = Flask(__name__)

@app.route('/')
def all_user():
    users = User.get_all()
    return render_template('read.html', users = users)

@app.route('/new_user')
def new_user():
    return render_template('create.html')

@app.route('/create_user', methods = ['POST'])
def create_user():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }
    User.create_user(data)
    return redirect('/')



if __name__ == "__main__":
    app.run(debug=True)