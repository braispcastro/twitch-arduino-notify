import pyfirmata, time, json
from twitch import twitch

# Find board
board = pyfirmata.Arduino('/dev/tty.usbmodem14101')

# Twitch secrets
client_id = ''
client_secret = ''
with open('secret.json') as f:
    secret = json.load(f)
    client_id = secret['clientId']
    client_secret = secret['clientSecret']

twitch_client = twitch(client_id, client_secret)
access_token = twitch_client.authenticate()


while True:
    # Placeholder blink
    board.digital[13].write(1)
    time.sleep(1)
    board.digital[13].write(0)
    time.sleep(1)