import requests
from behave import given, when, then

api_url = None
api_key = None
response = None


@given('the endpoint "{endpoint}"')
def step_given_endpoint(context, endpoint):
    global api_url
    api_url = endpoint


@given('the API key "{key}"')
def step_given_api_key(context, key):
    global api_key
    api_key = key


@when('I get information for "{code}"')
def step_get_information(context, code):
    global response
    response = requests.get(api_url.format(code=code), params={"access_key": api_key})


@then('the response should have status code {status_code:d}')
def step_response_status_code(context, status_code):
    assert response.status_code == status_code


@then('the response should have the country name "{country_name}"')
def step_response_country_name(context, country_name):
    json_response = response.json()
    assert json_response["name"] == country_name


@when('I create a new country with name "{name}", alpha2_code "{alpha2}" and alpha3_code "{alpha3}"')
def step_create_country(context, name, alpha2, alpha3):
    global response
    payload = {"name": name, "alpha2Code": alpha2, "alpha3Code": alpha3}
    response = requests.post(api_url, params={"access_key": api_key}, json=payload)
