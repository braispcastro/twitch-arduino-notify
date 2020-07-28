import pyfirmata, time, json
from twitch import twitch


def get_twitch_user_id(access_token, username):
    user_data = twitch_client.get_users(access_token, username)[0]
    return user_data['id']




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
user_id = get_twitch_user_id(access_token, 'frankylift')


while True:
    # Placeholder blink
    board.digital[13].write(1)
    time.sleep(1)
    board.digital[13].write(0)
    time.sleep(1)
