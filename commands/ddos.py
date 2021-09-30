from commands.command import Command, CommandType

class CommandDDoS(Command):
    def __init__(self, target_ip: str) -> None:
        super().__init__(CommandType.DDOS)
        self.target_ip = target_ip

    def process(self) -> None:
        pass