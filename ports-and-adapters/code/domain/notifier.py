from abc import ABC
from abc import abstractmethod

from domain.messages import Message

class Notifier(ABC):
    @abstractmethod
    def notify(self, message: Message):
        pass