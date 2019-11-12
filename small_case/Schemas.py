class Schemas(object):

    def __init__(self, schema_config: str):
        # schema_config = "d:str,l:bool,p:int"
        self.schema_dict = {}
        schemas = schema_config.split(',')
        for schema in schemas:
            name, type = schema.split(':')
            self.schema_dict[name] = type

    def get_value(self, name: str, value: str):
        str_type = self.schema_dict.get(name)
        if str_type == "bool":
            if value and value.upper() == "TRUE":
                return True
            else:
                return False
        elif str_type == "int":
            if value:
                return int(value)
            else:
                return 8080
        else:
            return value


if __name__ == "__main__":
    a = Schemas("l:bool")
    a.get_value("bool", "True")
