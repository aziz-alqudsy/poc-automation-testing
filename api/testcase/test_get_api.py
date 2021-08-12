import requests
from jsonschema import validate
from libs.get_schema import get_schema_file

def test_get_api():
    # hit api success 200
    get_api_200 = requests.get("https://jsonplaceholder.cypress.io/posts")
    response_json = get_api_200.json()

    # verify status code from response
    assert get_api_200.status_code == 200
    # verify data type from response
    validate(instance=response_json, schema=get_schema_file("api/schema/schema_get_api_200.json"))
