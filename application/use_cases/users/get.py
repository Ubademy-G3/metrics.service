import os
import requests
import json
from dotenv import load_dotenv
load_dotenv()
import logging

logger = logging.getLogger(__name__)

USERS_SERVICE_API_KEY = os.getenv('USERS_SERVICE_API_KEY')
USERS_SERVICE_URL = "https://staging-users-service-v2.herokuapp.com/users"


header_users = {"authorization": USERS_SERVICE_API_KEY}

def get_metrics_by_id(user_id):

    logger.info("Get metrics of user %s", user_id)
    logger.debug("Making request to users service")
    response = requests.get(USERS_SERVICE_URL+"/"+user_id,
                            headers = header_users)

    response_json = response.json()
    logger.debug("Response: %s", str(response_json))
    result = {
        "user_id": user_id,
        "metrics": {
            "register_with_email": (response_json['registerType'] == "not-google"),
            "register_with_app": (response_json['registerType'] == "google"),
            "login_with_email": (response_json['registerType'] == "not-google"),
            "login_with_app": (response_json['registerType'] == "google"),
            "times_pw_changed": response_json['passwordChanged']
        }
    }
    return result


def get_metrics():

    logger.info("Get users metrics")
    logger.debug("Making request to users service")
    response_all_users = requests.get(USERS_SERVICE_URL,
                            headers = header_users)
    response_json = response_all_users.json()
    logger.debug("Response: %s", str(response_json))
    
    reg_mail = 0
    reg_app = 0
    log_mail = 0
    log_app = 0
    pw_changes = 0
    for user in response_json:
        reg_mail += (1 if user['registerType'] == "not-google" else 0)
        reg_app += (1 if user['registerType'] == "google" else 0)
        log_mail += (1 if user['registerType'] == "not-google" else 0)
        log_app += (1 if user['registerType'] == "google" else 0)
        pw_changes += user['passwordChanged']

    result = {
        "users_amount": len(response_json),
        "metrics":{
            "registered_with_mail": reg_mail,
            "registered_with_app": reg_app,
            "logged_with_mail": log_mail,
            "logged_with_app": log_app,
            "times_pw_changed": pw_changes
        }
    }
    return result
