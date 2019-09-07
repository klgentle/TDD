class Schema(object):

    def __init__(self, schema: str):
        # a = Schema("l:bool,p:int,d:str")
        schema_list = schema.split(",")
        self.schema_dict = {}
        for item in schema_list:
            name, str_type = item.split(":")
            self.schema_dict[name] = str_type

    def get_value(self, name: str, value):
        if self.schema_dict.get(name) == "bool":
            if value and value.upper() == "TRUE":
                return True
            else:
                return False
        elif self.schema_dict.get(name) == "int":
            if value:
                return int(value)
            else:
                return 8080
        else:
            return value
