from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Used for session management

# Static credentials
USERNAME = "user"
PASSWORD = "1234"

@app.route('/')
def index():
    # If user is already logged in, redirect to homepage
    if "logged_in" in session and session["logged_in"]:
        return redirect(url_for('homepage'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Validate credentials
        if username == USERNAME and password == PASSWORD:
            session['logged_in'] = True
            return redirect(url_for('homepage'))
        else:
            return render_template('login.html', error="Invalid username or password")
    return render_template('login.html')

@app.route('/homepage')
def homepage():
    # Check if user is logged in
    if "logged_in" in session and session["logged_in"]:
        return render_template('homepage.html')
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.clear()  # Clear session data
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)