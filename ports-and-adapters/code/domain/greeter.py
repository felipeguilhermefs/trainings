from datetime import date

from domain.birthdays import Birthdays
from domain.messages import Messages
from domain.notifier import Notifier

class Greeter:
    def __init__(self, notifier: Notifier, birthdays: Birthdays, messages: Messages):
        self._notifier = notifier
        self._birthdays = birthdays
        self._messages = messages

    def greet(self, today: date):
        for birthday in self._birthdays.get_birthdays(today):
            message = self._messages.get_message(birthday.name)
            self._notifier.notify(message)