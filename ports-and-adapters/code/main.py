import os
from datetime import date
from adapters.csv_birthdays import CSVBirthdays
from adapters.in_memory_messages import InMemoryMessages
from adapters.slack_notifier import SlackNotifier

def send_birthday_greetings(notifier, birthdays, messages, today):
    for birthday in birthdays.get_birthdays(today):
        message = messages.get_message(birthday.name)
        notifier.notify(message)

def main():
    birthdays = CSVBirthdays("birthdays.csv")
    messages = InMemoryMessages()
    notifier = SlackNotifier(channel='bday_test', token=os.getenv('SLACK_TOKEN'))
    today = date.today()
    send_birthday_greetings(notifier, birthdays, messages, today)

if __name__ == '__main__':
    main()
