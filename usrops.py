''' Twilio user operations '''
from authy.api import AuthyApiClient

def new_user(email, phone_number, country_code, api_key):
    authy_api = AuthyApiClient(api_key)
    # verify(email, phone_number, country_code)
    user = authy_api.users.create(email, phone_number, country_code)
