import requests
from jsonschema import validate
from libs.get_schema import get_schema_file

def test_post_api():
    # request data
    request_data = {}
    request_data['title'] = 'recommendation'
    request_data['body'] = 'motorcycle'
    request_data['userId'] = 12

    # hit api created 201
    post_api_201 = requests.post("https://jsonplaceholder.cypress.io/posts", data=request_data)
    response_json = post_api_201.json()

    # verify status code and value from response
    assert post_api_201.status_code == 201
    assert response_json['title'] == request_data['title']
    assert response_json['body'] == request_data['body']
    assert int(response_json['userId']) == request_data['userId']
    # verify data type from response
    validate(instance=response_json, schema=get_schema_file("api/schema/schema_post_api_201.json"))
