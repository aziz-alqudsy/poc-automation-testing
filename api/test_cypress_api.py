import requests
from jsonschema import validate
from api.libs.get_schema import GetSchema

def test_get_api():
    # hit api success 200
    get_api_200 = requests.get("https://jsonplaceholder.cypress.io/posts")
    response_json = get_api_200.json()

    # verify status code from response
    assert get_api_200.status_code == 200
    # verify data type from response
    validate(instance=response_json, schema=GetSchema.get_schema_file("api/schema/schema_get_api_200.json"))

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
    validate(instance=response_json, schema=GetSchema.get_schema_file("api/schema/schema_post_api_201.json"))
