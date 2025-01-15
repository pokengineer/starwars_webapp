# Assignment
Using the StarWars API (https://swapi.tech/) create a simple full-stack web application to support the following end-user functionality:

- An authenticated user should be able to view a list of Starships in a `<table>`
- Using a `<select>`, an authenticated user should be able to choose a Starship `manufacturer` from a list
- When a Starship `manufacturer` is selected the `<table>` should display only the Starships for the selected `manufacturer`
- If no `manufacturer` is selected the `<table>` should display all Starships

# Notes and Technical Requirements:
- You are free to use any language and framework you’d like (.net code, node js, Micronaut, Flask, ruby on rails, etc).
- The solution should require Authentication.  We do not have any specific requirements for the approach and the solution does not need to account for inviting or signing up users, static user credentials are fine.
- The solution will not be evaluated on visual style, so you do not need to spend time styling unless you want to (browser defaults are fine).
- The solution does not need to be deployed anywhere, localhost is fine.
- If the solution uses an API it should respond with JSON data
- Client libraries exist for the StarWars API. We request that you do not use these libraries library to interact with the StarWars API
- Open-source packages other than the StarWars client libraries can be used but are not required to complete this assignment.

# Solution Overview
## 1. Data Extraction
Due to the Star Wars API's rate limit (5 calls every 15 minutes), data is extracted using a script and saved locally in a CSV file for faster processing and offline use.

## 2. Web Application
The web application is developed using Flask, chosen for its simplicity and lightweight nature. It includes the following key features:

### Login: 
- Static user credentials (user: user, password: 1234) to access the application.
### Homepage:
- Displays a table with all Starship data initially.
- Includes a dropdown for Starship manufacturers to filter the data.
- When a manufacturer is selected, the table is dynamically updated to display only matching results.
- Refresh Button: A button allows authenticated users to refresh the data by fetching the latest information from the Star Wars API and updating the local CSV.
- Logout Button: Logs the user out, clearing their session.

# How to Run the Application
### Clone the repository:
```
git clone https://github.com/pokengineer/starwars_webapp
cd starwars_webapp
```
### Install dependencies:
Make sure you have Python installed. Then install the required packages:
```
pip install -r requirements.txt 
```

### Create the PostgreSQL database
```
cd database
docker-compose up -d
```

### Prepare the data:
Run the script to fetch and save Starship data into the database and perform an exploratory analysis

### Run the application:
```
python app.py  
```

Access the application in your browser at http://localhost:5000.
