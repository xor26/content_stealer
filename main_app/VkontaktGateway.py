import requests


class VkontaktGateway:
    def __init__(self):
        self.access_token = "6d7b41bc16f95212f94f93fb9d216dd21e33abf1cac6b179e16c1b5c5c75c1414883440d091edbb9e83f2"
        self.public_id = 180588672
        self.request_uri = "https://api.vk.com/method/{}"

    def send_post(self, post):
        url = self.request_uri.format("wall.post")
        requests.get(url=url, params={
            "access_token": self.access_token,
            "owner_id": -1 * self.public_id,  # lol
            "from_group": 1,
            "message": post.title + " " + post.content,
            "version": 5.5,
        })