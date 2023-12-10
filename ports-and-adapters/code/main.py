import os
import random
from slack_sdk import WebClient 
from datetime import date
from adapters.csv_birthdays import CSVBirthdays

def send_birthday_greetings(slack_client, birthdays, today):
    for birthday in birthdays.get_birthdays(today):
        greeting = choose_random_greeting()
        slack_message = replace_placeholders(greeting, birthday.name)
        slack_client.chat_postMessage(channel='bday_test', text=slack_message)

def choose_random_greeting():
    greetings = [
        'Happy birthday to the amazing [name]!',
        '[name], you are the sunshine of our team! Wishing you a wonderful birthday!',
        'Sending you warm birthday wishes, [name]! May this year be filled with joy and success!'
    ]
    return random.choice(greetings)

def replace_placeholders(message, name):
    return message.replace('[name]', name)

def main():
    birthdays = CSVBirthdays("birthdays.csv")
    slack_token = os.getenv('SLACK_TOKEN')
    slack_client = WebClient(token=slack_token)
    today = date.today()
    send_birthday_greetings(slack_client, birthdays, today)

if __name__ == '__main__':
    main()
