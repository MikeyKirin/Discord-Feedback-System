from config import *
from flask import Flask,render_template,request, redirect, session
from datetime import datetime
from zenora import APIClient
import psycopg2

# We've loaded all of our modules. Additionally we've put all of our passwords and other sensitive data
# into config.py then imported it for security. 

# Create our instance and label our templates folder.
app = Flask(__name__,template_folder = 'templates')

# Set the secret key for sessions.
app.secret_key = SECRET_KEY

# Get token and client_secret.
client = APIClient(TOKEN, client_secret=CLIENT_SECRET)

# current date and time.
now = datetime.now()

# Connect to our database.
def db_connect():
    conn = psycopg2.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD)
    return conn

# Display the index page where you login.
@app.route ('/')
def index():
     return render_template("index.html")

# Redirect /login to Discord login.
@app.route('/login')
def login():
    return redirect(OAUTH_URL)

# User login via the Discord API, gather and store data in a session
@app.route('/oauth/discord')
def auth():
    code = request.args['code']
    access_token = client.oauth.get_access_token(code, REDIRECT_URI).access_token
    bearer_client = APIClient(access_token, bearer=True)
    current_user = bearer_client.users.get_current_user()

    id = str(current_user.id)
    username = str(current_user.username)

    session['id'] = id
    session['username'] = username
    session['token'] = access_token
    return redirect('/home')

# Once logged in, go to the home area.
@app.route ('/home')
def home():
    return render_template("home.html")    

# Display the Admin panel.
@app.route ('/admin')
def admin():
    return render_template("admin.html")

# Fill out the code to collect data and put it in the database from the feedback form
@app.route ('/feedback', methods = ["GET","POST"])
def feedback():
    if request.method == "POST":
        username = session.get('username')
        userid = session.get('id')
        public = request.form.get("public")
        contact = request.form.get("contact")
        feedback_desc = request.form.get("feedback_desc")
        email = request.form.get("email")
        timestamp = datetime.now()

        conn = db_connect()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO users (id, userid, username, contact, email, feedback_desc, created_at, is_public) VALUES (DEFAULT,%s,%s,%s,%s,%s,%s,%s)",
            (userid,username,contact,email,feedback_desc,timestamp,public)
            )
        conn.commit()

        return render_template("success.html")
    return render_template("feedback.html")

# Show all of the submitted feedback data.
@app.route ('/queries')
def queries():
        conn = db_connect()
        cur = conn.cursor()
        cur.execute(
            "SELECT * FROM users"
        )
        data = cur.fetchall()
        return render_template('queries.html', data=data)

# Let users search for a specific user, email or keyword
@app.route ('/search')
def search():
        return render_template('search.html')

if __name__=="__main__":
    app.run(debug=True)
