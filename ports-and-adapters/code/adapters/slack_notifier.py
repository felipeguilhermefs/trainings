from slack_sdk import WebClient

from domain.messages import Message
from domain.notifier import Notifier


class SlackNotifier(Notifier):
    def __init__(self, channel: str, token: str):
        self._channel = channel
        self._client = WebClient(token=token)

    def notify(self, message: Message):
        self._client.chat_postMessage(channel=self._channel, text=message.body)