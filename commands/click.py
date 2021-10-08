from commands.command import Command, CommandType
import requests

class CommandClick(Command):
    """
    Trigger a request on a link
    """

    def __init__(self, url: str) -> None:
        super().__init__(CommandType.CLICK)
        self.url = url

    def process(self) -> None:
        requests.get(self.url)

    def stop(self) -> None:
        pass