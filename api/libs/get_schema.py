import json

class GetSchema():
    def __init__(self):
        pass

    def get_schema_file(filename):
        with open(filename, 'r') as file_schema:
            schema = json.load(file_schema)
        return schema
