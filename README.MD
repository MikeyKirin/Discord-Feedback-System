# Yet Another Feedback System
The purpose of Yet Another Feedback System (YAFS) is to provide a way for people to collect feedback about their Discord server. 
This code includes a Discord bot as well as a feedback web interace. 

## Prerequisites
For this project you'll need the following installed using pip:
> psycopg2, postgres, libpq-dev, flask, zenora, datetime, discord, and discord-ext-bot

** If you have an issue with psycopg2, you must reinstall libpq-dev which may require sudo: `sudo apt-get install --reinstall libpq-dev`

## Installation
1. Start by installing the prerequisites above into the main project directory.
   1. Once installed, configure your postgres credentials and add them to the config.py document.
   2. Now setup your database using the `database.sql` file included in this project.
      1. You can either use a GUI to import this file, or run `psql -h hostname -U username -f {SQL script file name}` in your terminal.
2. Go back to your terminal and type `flask run` to start the webserver.
3. Click the link in the terminal to go to the website. It should be `http://127.0.0.1:5000`
4. If you are also running this in your Discord Server, follow the instructions below.
   1. Invite the YAFS Discord Bot to your server using [THIS LINK](https://discord.com/oauth2/authorize?client_id=1232533338162462720&response_type=code&redirect_uri=http%3A%2F%2Flocalhost%3A5000%2Foauth%2Fdiscord&scope=identify+guilds+email).
   2. Once invited, type `%run main.py` in your terminal to start the bot.
   3. Head to your Discord server and type `/feedback` in any channel the bot has access. This will bring up an embed with a link to access the website.

## Developer Installation
1. If you're a developer looking to launch the bot yourself for development or testing, follow the instructions below.
   1. You'll need to get your own bot and API info from the [Discord Developer Portal](https://discord.com/developers/applications)
   2. Once finished, you will then create your own YAFS Bot Link to invite your bot to your Discord. It is located in the "Bot" tab of the Developer Portal.
   3. Once you have your API setup, you will have to add your CLIENT ID, CLIENT_SECRET, TOKEN and new OAUTH_URL to config.py
   4. You will also need to add your own credentials to the database configurations in config.py as well.
   5. After all that is completed, you can navigate to the project directory and type `%run main.py` to start your bot.
2. Once the bot is online, you can let your community call it and find the Feedback link with the `/feedback` in any channel the bot has access to.

## Usage
There are two main categories on the website: Submit Feedback and Admin Panel

1. Feedback
   1. This will be where a user can submit feedback of your Discord and request to be contacted.
   2. A user will submit their email and feedback, and check off if they want to be contacted or have the feedback made public.
   3. Once they hit submit, the information will be sent to the database for later review.

2. Admin Panel
   1. This is where you can view all the feedback submitted.
   2. There's a Queries tab on the left hand side once you access the Admin Panel. This tab will bring up all the information submitted through the feedback system.

## Contact
Michael Kirkpatrick - [GitHub](LINK) - mikeykirin101@gmail.com

Project Link: