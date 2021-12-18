from decouple import config
import requests
import urllib.parse
import time

# This works only for public groups, not channels and not private groups
TELE_TOKEN = config('TELE_TOKEN')
groups = [
    '@frenbotfarm1',
    '@frenbotfarm2'
]

wait_minutes = 60              # send message every hour
wait_time = wait_minutes * 60  # convert seconds to minutes

msg = urllib.parse.quote(
    """
    Fren shill template goes here

    can use unicode with utf-16 code

    \U0001f604 \U0001f604 \U0001f604
    \U0001F680 \U0001F680 \U0001F680
    shill shill shill
    """)

while True:
    for group in groups:
        url = ('https://api.telegram.org/bot' +
               TELE_TOKEN + '/sendMessage?chat_id='
               + group + '&text=' + msg)

        response = requests.get(url)
        print(group + '\n')
        print(url + '\n')
        print(response.content)
        print('\n---------\n')

    time.sleep(wait_time)
