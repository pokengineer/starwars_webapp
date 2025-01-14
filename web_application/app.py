from flask import Flask, render_template, request, redirect, url_for, session
import pandas as pd
import requests
from ratelimiter import RateLimiter
import re

app = Flask(__name__)
app.secret_key = "secretkey"  # Used for session management

# Static credentials
USERNAME = "user"
PASSWORD = "1234"

@RateLimiter(max_calls=400, period=3600)
def request_get( url ):
    return requests.get(url)


@app.route('/')
def index():
    if "logged_in" in session and session["logged_in"]:
        return redirect(url_for('homepage'))
    return redirect(url_for('login'))



@app.route('/login', methods=['GET', 'POST'])
def login():
    # Static credentials are used, but this method could be replaced with a real login
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
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
            # Load data, using read_csv.
            # on a real app here is where we would connect with a database
            df = pd.read_csv('data/starships.csv')

            # get list of possible manufacturers
            manufacturers = sorted(df['manufacturer'].unique())

            selected_manufacturer = request.form.get('manufacturer', '')
            if selected_manufacturer:
                # Filter rows matching the manufacturer using regex
                pattern = re.compile(selected_manufacturer, re.IGNORECASE)
                filtered_df = df[df['manufacturer'].str.contains(pattern)]
            else:
                # show complete df by default
                filtered_df = df

            table_data = filtered_df.to_html(index=False, classes='table table-striped')
        except FileNotFoundError:
            manufacturers = []
            table_data = "<p>Error: CSV file not found.</p>"
        
        return render_template('homepage.html', table=table_data, manufacturers=manufacturers, selected_manufacturer=selected_manufacturer)
    return redirect(url_for('login'))

@app.route('/refresh_data', methods=['POST'])
def refresh_data():
    try:
        url = "https://www.swapi.tech/api/starships/"
        starships = []
        while url:
            r = request_get( url )
            response = r.json()
            starships.extend(response['results'])
            url = response['next']
        starship_details = []
        for s in starships:
            r = request_get( s['url'] )
            response = r.json()
            starship_details.append(response['result']['properties'])
        df = pd.DataFrame(starship_details)
        df.to_csv('data/starships.csv', index=False)
        return redirect(url_for('homepage'))
    except Exception as e:
            return f"Error refreshing CSV: {str(e)}", 500


@app.route('/logout')
def logout():
    session.clear()  # Clear session data
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)


@RateLimiter(max_calls=400, period=3600)
def request_get( url ):
    return requests.get(url)