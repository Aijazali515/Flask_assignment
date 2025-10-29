from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    message = ''
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username and password:
            message = f"Welcome, {username}!"
        else:
            message = "Error: Both fields are required!"
    return render_template('login.html', message=message)

@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        return render_template('feedback.html', name=name, email=email, message=message, submitted=True)
    return render_template('feedback.html', submitted=False)

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        return "Form submitted using POST method"
    else:
        return "Form opened using GET method"

if __name__ == '__main__':
    app.run(debug=True)