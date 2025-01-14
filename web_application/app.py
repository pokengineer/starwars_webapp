from flask import Flask, render_template, request, redirect, url_for, session
import pandas as pd
import re

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

@app.route('/homepage', methods=['GET', 'POST'])
def homepage():
    # Check if user is logged in
    if "logged_in" in session and session["logged_in"]:
        try:
            # Load CSV data
            df = pd.read_csv('data/starships.csv')
            manufacturers = sorted(df['manufacturer'].unique())

            selected_manufacturer = request.form.get('manufacturer', '')
            if selected_manufacturer:
                # Filter rows matching the manufacturer using regex
                pattern = re.compile(selected_manufacturer, re.IGNORECASE)
                filtered_df = df[df['manufacturer'].str.contains(pattern)]
            else:
                filtered_df = df

            table_data = filtered_df.to_html(index=False, classes='table table-striped')
        except FileNotFoundError:
            manufacturers = []
            table_data = "<p>Error: CSV file not found.</p>"
        
        return render_template('homepage.html', table=table_data, manufacturers=manufacturers, selected_manufacturer=selected_manufacturer)
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.clear()  # Clear session data
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)