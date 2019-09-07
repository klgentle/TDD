class Command(object):

    def __init__(self, command: str):
        # a = Command("-l true -d usr/local")
        self.command = command
        self.command_dict = {}
        command_list = command.split(' ')
        for i in range(1, len(command_list)):
            name = command_list[i-1]
            value = command_list[i]
            if name.startswith('-'):
                if value.startswith('-') and value[1].isalpha():
                    value = None
                self.command_dict[name[1:]] = value
            else:
                continue

    def get_value(self, name: str):
        # return "true"
        return self.command_dict.get(name)
