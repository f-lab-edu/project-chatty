from fastapi.logger import logger
from slack_sdk import WebClient

from core.config import settings


class SlackClient:
    def __init__(self):
        self.client: WebClient = WebClient(settings.SLACK_BOT_TOKEN)

    def post_message(self, channel: str, text: str):
        try:
            self.client.chat_postMessage(channel=channel, text=text)
        except Exception as e:
            logger.error(e)


def get_slack_client() -> SlackClient:
    slack_client = SlackClient()
    return slack_client
