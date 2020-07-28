def ToUserData(j):
    return UserData(j)


def ToStreamData(j):
    return StreamData(j)


def ToGameData(j):
    return GameData(j)


def ToChannelData(user, name, description, avatar, game, start_time, title, isOnline, viewer_count):
    return ChannelData(user, name, description, avatar, game, start_time, title, isOnline, viewer_count)


class UserData(object):
    def __init__(self, json):
        self.id = json["id"]
        self.login = json["login"]
        self.display_name = json["display_name"]
        self.type = json["type"]
        self.broadcaster_type = json["broadcaster_type"]
        self.description = json["description"]
        self.profile_image_url = json["profile_image_url"]
        self.offline_image_url = json["offline_image_url"]
        self.view_count = json["view_count"]


class StreamData(object):
    def __init__(self, json):
        self.id = json["id"]
        self.user_id = json["user_id"]
        self.user_name = json["user_name"]
        self.game_id = json["game_id"]
        self.type = json["type"]
        self.title = json["title"]
        self.viewer_count = json["viewer_count"]
        self.started_at = json["started_at"]
        self.language = json["language"]
        self.thumbnail_url = json["thumbnail_url"]
        self.tag_ids = json["tag_ids"]


class GameData(object):
    def __init__(self, json):
        self.id = json["id"]
        self.box_art_url = json["box_art_url"]
        self.name = json["name"]


class ChannelData(object):
    def __init__(self, user, name, description, avatar, game, start_time, title, isOnline, viewer_count):
        self.user = user
        self.displayName = name
        self.description = description
        self.avatar = avatar
        self.game = game
        self.start_time = start_time
        self.title = title
        self.isOnline = isOnline
        self.viewer_count = viewer_count