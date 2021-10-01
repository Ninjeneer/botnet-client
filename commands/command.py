from abc import ABC, abstractmethod
import uuid
from enum import Enum

class CommandType:
    DDoS = 'ddos'
    RCE = 'rce'

class Command(ABC):
    def __init__(self, type: CommandType) -> None:
        self.id = uuid.uuid4()
        self.type = CommandType

    @abstractmethod
    def process() -> None:
        pass

    @abstractmethod
    def stop() -> None:
        pass
    