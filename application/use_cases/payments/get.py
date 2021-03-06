import os
import requests
import json
from dotenv import load_dotenv
load_dotenv()
import logging

logger = logging.getLogger(__name__)

PAYMENTS_SERVICE_API_KEY = os.getenv('PAYMENTS_SERVICE_API_KEY')
PAYMENTS_SERVICE_URL = "https://staging-payments-service-app.herokuapp.com/deposit"

header_payments = {"authorization": PAYMENTS_SERVICE_API_KEY}

def get_metrics():

    logger.info("Get payments metrics")
    logger.debug("Making request to payments service")
    response = requests.get(PAYMENTS_SERVICE_URL,
                            headers = header_payments)
    response_json = response.json()
    logger.debug("Response: %s", str(response_json))

    result = {}
    for payment in response_json:
        date = payment['created_at'].split('T')[0]
        money = float(payment["amount_sent"])
        if not date in result:
            result[date] = {
                "amount_transactions": 1,
                "total_money_sent": money
            }
        else:
            result[date]["amount_transactions"] += 1
            result[date]["total_money_sent"] += money
    return result