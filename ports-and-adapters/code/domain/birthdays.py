from abc import ABC
from abc import abstractmethod
from dataclasses import dataclass
from datetime import date
from typing import List

@dataclass
class Birthday:
    name: str
    month: int
    day: int

class Birthdays(ABC):
    @abstractmethod
    def get_birthdays(self, today: date) -> List[Birthday]:
        pass