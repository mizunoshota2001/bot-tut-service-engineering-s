#!.venv/bin/python3
import os
import sys

# line-bot-sdk
from linebot.v3.messaging import (
    Configuration,
    ApiClient,
    MessagingApi,
    ReplyMessageRequest,
    TextMessage
)
from linebot.v3.webhooks import (
    MessageEvent,
    TextMessageContent
)
from linebot.v3 import WebhookHandler

# custom module
from config import CONFIG


# LINE BOT SDKの初期化
configuration = Configuration(access_token=CONFIG["channel_access_token"])
handler = WebhookHandler(CONFIG["channel_secret"])
api_instance = MessagingApi(ApiClient(configuration))


@handler.add(MessageEvent, message=TextMessageContent)
def handle_message(event):
    api_instance.reply_message_with_http_info(
        ReplyMessageRequest(
            reply_token=event.reply_token,
            messages=[TextMessage(text=event.message.text)]
        )
    )


def main():
    body: str = sys.stdin.read(int(os.environ.get('CONTENT_LENGTH', 0)))
    signature: str = os.getenv('HTTP_X_LINE_SIGNATURE', '')
    handler.handle(body, signature)


if __name__ == "__main__":
    print("Access-Control-Allow-Headers: Origin, Content-Type\r\nAccess-Control-Allow-Origin: *\r\nAccess-Control-Allow-Methods: GET, POST, PATCH, PUT, DELETE, OPTIONS\r\nContent-Type: application/json\r\n")
    main()
