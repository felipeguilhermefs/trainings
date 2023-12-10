from typing import List
from datetime import date

from domain.birthdays import Birthdays, Birthday

class CSVBirthdays(Birthdays):
    def __init__(self, filepath: str):
        self._filepath = filepath

    def get_birthdays(self, today: date) -> List[Birthday]:
        with open(self._filepath, 'r') as f:
            birthdays = []
            for row in f:
                name, month, day = row.strip().split(',')
                if int(month) == today.month and int(day) == today.day:
                    birthdays.append(Birthday(name, int(month), int(day)))
            return birthdays