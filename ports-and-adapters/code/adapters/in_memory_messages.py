import random

from domain.messages import Messages, Message

class InMemoryMessages(Messages):
    def __init__(self):
        self._messages = [
            'Happy birthday to the amazing [name]!',
            '[name], you are the sunshine of our team! Wishing you a wonderful birthday!',
            'Sending you warm birthday wishes, [name]! May this year be filled with joy and success!'
        ]

    def get_message(self, name: str) -> Message:
        message = random.choice(self._messages)
        return Message(message.replace('[name]', name))