from Schemas import Schemas
from Command import Command


class Args:

    def __init__(self, schema: str, command: str):
        self.schema = Schemas(schema)
        self.command = Command(command)

    def get_value(self, name: str):
        return self.schema.get_value(name, self.command.get_value(name))


if __name__ == "__main__":
    a = ParseSchema()
    a.parse()
