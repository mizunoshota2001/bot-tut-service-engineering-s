#!/usr/local/bin/python3
import sys
import json

# custom module
import loglib
from linelib import Reply

SAMPLE_MESSAGE: dict = {'type': 'text', 'text': "Hello, wold!!"}
API_SEND_REPLY_MESSAGES: str = "https://api.line.me/v2/bot/message/reply"
CHANNEL_ACCESS_TOKEN: str = ""
logger = loglib.get(__name__)


def main():
    body: dict = json.load(sys.stdin)
    event: dict = body["events"][0]
    rtoken: str = event['replyToken']
    etype: str = event["type"]
    reply = Reply(API_SEND_REPLY_MESSAGES, CHANNEL_ACCESS_TOKEN, rtoken)

    if etype == "message":
        text: str = event["message"]["text"]
        reply.add(SAMPLE_MESSAGE)

    reply.send()


if __name__ == "__main__":
    print("Content-Type: text/plain\r\n")
    try:
        main()
    except Exception as e:
        logger.exception(str(e))
