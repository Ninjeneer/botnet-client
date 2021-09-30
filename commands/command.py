from abc import ABC, abstractmethod
import uuid
from enum import Enum

class CommandType(Enum):
    DDOS = 0,
    RCE = 1

class Command(ABC):
    def __init__(self, type: CommandType) -> None:
        self.id = uuid.uuid4()
        self.type = CommandType

    @abstractmethod
    def process():
        pass
    