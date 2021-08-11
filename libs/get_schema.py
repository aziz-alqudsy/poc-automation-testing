import json

def get_schema_file(filename):
    # get schema file from json file
    with open(filename, 'r') as file_schema:
        schema = json.load(file_schema)
    return schema
