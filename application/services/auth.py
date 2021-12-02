import os
from dotenv import load_dotenv
from exceptions.auth_error import ApiKeyError

load_dotenv()

class AuthService:
    
    def __init__(self):

        self.api_key = os.getenv('API_KEY')


    def check_api_key(self, api_key):

        if api_key == self.api_key:
            return True
        raise ApiKeyError()


auth_service = AuthService()