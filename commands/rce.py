from commands.command import Command, CommandType
import os


class CommandRCE(Command):
    """
    Remote Code Execution command
    Creates a python file, execute it, then delete it
    """

    def __init__(self, payload: str) -> None:
        super().__init__(CommandType.RCE)
        self.payload = payload

    def process(self) -> None:
        with open("code.py", "w+") as file:
            file.write(self.payload)

        os.system('python3 ./code.py')
        os.remove("code.py")

    def stop(self):
        pass
