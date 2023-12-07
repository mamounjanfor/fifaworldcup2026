from flask import Flask, render_template
import sqlite3
app = Flask(__name__)

world_cup_data = [
    {"year": 1930, "host": "Uruguay", "winner": "Uruguay"},
    {"year": 1934, "host": "Italy", "winner": "Italy"},
    {"year": 1938, "host": "France", "winner": "Italy"},
    {"year": 1950, "host": "Brazil", "winner": "Uruguay"},
    {"year": 1954, "host": "Switzerland", "winner": "West Germany"},
    {"year": 1958, "host": "Sweden", "winner": "Brazil"},
    {"year": 1962, "host": "Chile", "winner": "Brazil"},
    {"year": 1966, "host": "England", "winner": "England"},
    {"year": 1970, "host": "Mexico", "winner": "Brazil"},
    {"year": 1974, "host": "West Germany", "winner": "West Germany"},
    {"year": 1978, "host": "Argentina", "winner": "Argentina"},
    {"year": 1982, "host": "Spain", "winner": "Italy"},
    {"year": 1986, "host": "Mexico", "winner": "Argentina"},
    {"year": 1990, "host": "Italy", "winner": "West Germany"},
    {"year": 1994, "host": "United States", "winner": "Brazil"},
    {"year": 1998, "host": "France", "winner": "France"},
    {"year": 2002, "host": "South Korea/Japan", "winner": "Brazil"},
    {"year": 2006, "host": "Germany", "winner": "Italy"},
    {"year": 2010, "host": "South Africa", "winner": "Spain"},
    {"year": 2014, "host": "Brazil", "winner": "Germany"},
    {"year": 2018, "host": "Russia", "winner": "France"},
    {"year": 2022, "host": "Qatar", "winner": "Argentina"}
]




@app.route('/')
def home():
    print("Serving the home page...")  # This will print in the console when the route is accessed.
    return render_template('index.html')

@app.route('/stadiums')  # Add this route for the Stadiums page
def stadiums():
    print("Serving the stadiums page...")
    return render_template('stadiums.html')

@app.route('/history')  # Add this route for the History page
def history():
    print("Serving the history page...")
    return render_template('history.html', world_cup_data=world_cup_data)

@app.route('/states')  # Add this route for the History page
def states():
    print("Serving the states page...")

    # Connect to the SQLite database
    conn = sqlite3.connect('UsaWorldcup2026.db')
    cursor = conn.cursor()

    # Fetch all records from the stadiums table
    cursor.execute("SELECT * FROM stadiums")
    stadiums_data = cursor.fetchall()

    # Close the connection to the database
    conn.close()

    # Pass the fetched data to the template
    return render_template('states.html', stadiums_data=stadiums_data)

if __name__ == '__main__':
    print("Starting Flask server...")  # This will print in the console when the Flask app starts.
    app.run(debug=True)





