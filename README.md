README

## Basic Usage
1. Create a bot using botfather and get API token
1. Save api token in a file named .env in the project directory
  * Env should contain `TELE_TOKEN=abcde` where abcde is your telegram bot api token
1. Add your bot to the public group you want it to send to
1. Navigate to your project directory
1. Create a python virtual environment
  * `python3 -m venv venv`
1. Step into virtual environment
  * `. ./venv/bin/activate`
  * if you use fish shell, it will be activate.fish instead of activate
1. Install requirements
  * `pip3 install -r requirements.txt`
1. Replace the channel names and shill template string with the values you actually want to use and update the bot run frequency variable (wait_minutes)
1. Run `python3 bot.py` in the terminal prompt (with environment activated), watch for intended responses
1. To stop the bot, press ctrl-c
