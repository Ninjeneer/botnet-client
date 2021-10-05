from abc import ABC, abstractmethod
import uuid
from enum import Enum

class CommandType:
    DDoS = 'ddos'
    RCE = 'rce'

class Command(ABC):
    def __init__(self, type: str) -> None:
        self.id = uuid.uuid4()
        self.type = str

    @abstractmethod
    def process() -> None:
        pass

    @abstractmethod
    def stop() -> None:
        pass
    