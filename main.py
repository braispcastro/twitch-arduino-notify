import pyfirmata, json, time, twitchdata
from twitch import twitch
from datetime import datetime


def get_twitch_user_id(username):
    user_data = twitch_client.get_users(access_token, [username])[0]
    return user_data['id']


def get_streams_online(user_id):
    follows_list = twitch_client.get_follows(access_token, user_id)
    users_id = []
    for item in follows_list:
        users_id.append(item['to_id'])
    online_list = twitch_client.get_streams(access_token, users_id)
    result = []
    for channel in online_list:
        stream = twitchdata.ToStreamData(channel)
        if stream.type == 'live':
            result.append(stream)
    return [r.user_name for r in result]


# Find board
# board = pyfirmata.Arduino('/dev/tty.usbmodem14101')

# Twitch secrets
client_id = ''
client_secret = ''
twitch_username = ''
with open('secret.json') as f:
    secret = json.load(f)
    client_id = secret['clientId']
    client_secret = secret['clientSecret']
    twitch_username = secret['twitchUsername']

twitch_client = twitch(client_id, client_secret)
access_token = twitch_client.authenticate()
user_id = get_twitch_user_id(twitch_username)
streams = get_streams_online(user_id)


print('Starting loop...')
while True:
    # Wait 60 seconds
    time.sleep(60)
    aux_streams = get_streams_online(user_id)
    new_online = set(aux_streams).difference(streams)
    streams = aux_streams
    str_now = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    if len(new_online) > 0:
        print(f"[{str_now}] {new_online}")
    else:
        print(f"[{str_now}] None")