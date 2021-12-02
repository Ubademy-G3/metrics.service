import os
import requests
import json
from dotenv import load_dotenv
load_dotenv()

COURSES_SERVICE_API_KEY = os.getenv('COURSES_SERVICE_API_KEY')
COURSES_SERVICE_URL = os.getenv('COURSES_SERVICE_URL')

header = {"apikey": COURSES_SERVICE_API_KEY}

def get_metrics_by_id(course_id):

    response = requests.get(COURSES_SERVICE_URL+course_id+"/metrics/",
                            headers = header)
    return response.json()


def get_metrics():

    response_courses = requests.get(COURSES_SERVICE_URL,
                                    headers = header)
    courses_json = response_courses.json()
    result_list = []
    for course in courses_json['courses']:
        c_id = course['id']

        course_metrics = get_metrics_by_id(c_id)
        result_list.append(course_metrics)
    
    return result_list
    
