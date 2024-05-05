import json
import urllib.request


class Reply():
    def __init__(self, api_send_reply_messages: str, channel_access_token: str, reply_token: str):
        self.messages = []
        self.api_send_reply_messages = api_send_reply_messages
        self.channel_access_token = channel_access_token
        self.reply_token = reply_token

    def add(self, message: dict):
        self.messages.append(message)

    def send(self):
        headers = {
            'Content-Type': 'application/json; charset=UTF-8',
            'Authorization': f'Bearer {self.api_send_reply_messages}'
        }
        data = {
            'replyToken': self.reply_token,
            'messages': self.messages
        }
        data = json.dumps(data).encode('utf-8')
        url = self.api_send_reply_messages
        req = urllib.request.Request(url, data, headers)
        urllib.request.urlopen(req)
