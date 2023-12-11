import os
from datetime import date
from fastapi import FastAPI
from adapters.csv_birthdays import CSVBirthdays
from adapters.in_memory_messages import InMemoryMessages
from adapters.slack_notifier import SlackNotifier

from domain.greeter import Greeter

birthdays = CSVBirthdays("birthdays.csv")
messages = InMemoryMessages()
notifier = SlackNotifier(channel='bday_test', token=os.getenv('SLACK_TOKEN'))
greeter = Greeter(notifier, birthdays, messages)

app = FastAPI()

@app.get("/greet")
def greet():
    greeter.greet(date.today())
    return {"Result": "Noice"}