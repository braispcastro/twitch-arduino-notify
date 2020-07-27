import urllib.parse, requests, json

class twitch:

    def __init__(self, client_id, client_secret):
        self.base_url = "https://api.twitch.tv/helix/"
        self.oauth_url = "https://id.twitch.tv/oauth2/"
        self.client_id = client_id
        self.client_secret = client_secret

    def authenticate(self):
        url = urllib.parse.urljoin(self.oauth_url, "token")
        headers = {
            "Content-Type": "application/json",
            "Client-ID": self.client_id
        }
        params = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "grant_type": "client_credentials"
        }

        response = requests.post(url, headers=headers, params=params)

        if response.status_code != 200:
            return None

        return json.loads(response.text)["access_token"]

    def get_users(self, access_token, users):
        url = urllib.parse.urljoin(self.baseUrl, "users")
        headers = {
            "Content-Type": "application/json",
            "Client-ID": self.client_id,
            "Authorization": f"Bearer {access_token}"
        }
        url = url + "?"
        for user in users:
            url = url + f"login={user}&"

        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            return None

        return json.loads(response.text)["data"]

    def get_streams(self, access_token, users):
        url = urllib.parse.urljoin(self.baseUrl, "streams")
        headers = {
            "Content-Type": "application/json",
            "Client-ID": self.client_id,
            "Authorization": f"Bearer {access_token}"
        }
        url = url + "?"
        for user in users:
            url = url + f"user_id={user}&"

        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            return None

        return json.loads(response.text)["data"]

    def get_games(self, access_token, games):
        url = urllib.parse.urljoin(self.baseUrl, "games")
        headers = {
            "Content-Type": "application/json",
            "Client-ID": self.client_id,
            "Authorization": f"Bearer {access_token}"
        }
        url = url + "?"
        for game in games:
            url = url + f"id={game}&"

        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            return None

        return json.loads(response.text)["data"]