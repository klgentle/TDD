class Command(object):

    def __init__(self, command: str):
        # '-l true -p 8080 -d /usr/logs'
        command_list = command.split(' ')
        self.command_dict = {}
        for i in range(1, len(command_list)):
            name = command_list[i-1]
            value = command_list[i]
            # key starts withs '-', and is alpha may not be ok
            if value.startswith('-') and value[1].isalpha():
                value = None
            if name.startswith('-'):
                # key should not starts withs '-'
                self.command_dict[name[1:]] = value

    def get_value(self, name: str):
        return self.command_dict.get(name)

