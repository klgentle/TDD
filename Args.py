from Command import Command
from Schema import Schema


class Args(object):

    def __init__(self, schema: str, command: str):
        self.command = Command(command)
        self.schema = Schema(schema)

    def get_value(self, name):
        return self.schema.get_value(name, self.command.get_value(name))