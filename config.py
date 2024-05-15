import requests
import os

# Write out Discord configurations.
API_ENDPOINT='https://discord.com/api/v10'
TOKEN=os.environ.get('TOKEN')
CLIENT_ID=os.environ.get('CLIENT_ID')
CLIENT_SECRET=os.environ.get('CLIENT_SECRET')
REDIRECT_URI="https://discord-feedback-system.onrender.com/oauth/discord"
OAUTH_URL=os.environ.get('OAUTH_URL')

# Write out database configurations
host=os.environ.get('DB_HOST')
database="yafsdb"
user="mikey"
password=os.environ.get('DB_PASSWORD')

# Secret Key for sessions
SECRET_KEY = "SuperSecretKey123"

