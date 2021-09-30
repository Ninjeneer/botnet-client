from commands.command import Command, CommandType

class CommandRCE(Command):
    def __init__(self, payload: str) -> None:
        super().__init__(CommandType.RCE)
        self.payload = payload

    def process(self) -> None:
        pass