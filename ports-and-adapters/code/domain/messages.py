from abc import ABC
from abc import abstractmethod
from dataclasses import dataclass

@dataclass
class Message:
    body: str

class Messages(ABC):
    @abstractmethod
    def get_message(self, name: str) -> Message:
        pass