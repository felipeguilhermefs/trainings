import os
from datetime import date
from adapters.csv_birthdays import CSVBirthdays
from adapters.in_memory_messages import InMemoryMessages
from adapters.slack_notifier import SlackNotifier

from domain.greeter import Greeter

birthdays = CSVBirthdays("birthdays.csv")
messages = InMemoryMessages()
notifier = SlackNotifier(channel='bday_test', token=os.getenv('SLACK_TOKEN'))
greeter = Greeter(notifier, birthdays, messages)

def handler(event, context):
    greeter.greet(date.today())
    return {"StatusCode": 200}
