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


@handler.add(MessageEvent, message=TextMessageContent)
def handle_message(event):
    with ApiClient(configuration) as api_client:
        line_bot_api = MessagingApi(api_client)
        line_bot_api.reply_message_with_http_info(
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
    print("Content-Type: text/plain\r\n")
    main()
