import os
from slack_sdk import WebClient 
from datetime import date
from adapters.csv_birthdays import CSVBirthdays
from adapters.in_memory_messages import InMemoryMessages

def send_birthday_greetings(slack_client, birthdays, messages, today):
    for birthday in birthdays.get_birthdays(today):
        slack_message = messages.get_message(birthday.name)
        slack_client.chat_postMessage(channel='bday_test', text=slack_message.body)

def main():
    birthdays = CSVBirthdays("birthdays.csv")
    messages = InMemoryMessages()
    slack_token = os.getenv('SLACK_TOKEN')
    slack_client = WebClient(token=slack_token)
    today = date.today()
    send_birthday_greetings(slack_client, birthdays, messages, today)

if __name__ == '__main__':
    main()
