import requests

# Write out Discord configurations.
API_ENDPOINT = 'https://discord.com/api/v10'
TOKEN="MTIzMjUzMzMzODE2MjQ2MjcyMA.GVKCLI.vJiti4BhQAMlcKsK3xmK_jPbIXXDjzMNGtDpUs"
CLIENT_ID="1232533338162462720"
CLIENT_SECRET="UisDlzr3M2mhtNqkVZ3maz5l4qgCc3i8"
REDIRECT_URI="http://localhost:5000/oauth/discord"
OAUTH_URL="https://discord.com/oauth2/authorize?client_id=1232533338162462720&response_type=code&redirect_uri=http%3A%2F%2Flocalhost%3A5000%2Foauth%2Fdiscord&scope=identify+guilds+email"

# Write out database configurations
host="localhost"
database="yafsDB"
user="postgres"
password="Mikey6972"

# Secret Key for sessions
SECRET_KEY = "MikeysSuperSecretKey123"

