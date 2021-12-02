import os
import requests
import json
from dotenv import load_dotenv
load_dotenv()

COURSES_SERVICE_API_KEY = os.getenv('COURSES_SERVICE_API_KEY')
COURSES_SERVICE_URL = os.getenv('COURSES_SERVICE_URL')

EXAMS_SERVICE_API_KEY = os.getenv('EXAMS_SERVICE_API_KEY')
EXAMS_SERVICE_URL = os.getenv('EXAMS_SERVICE_URL')

header_courses = {"apikey": COURSES_SERVICE_API_KEY}
header_exams = {"apikey": EXAMS_SERVICE_API_KEY}

def get_metrics_by_id(course_id):

    response_courses = requests.get(COURSES_SERVICE_URL+course_id+"/metrics/",
                            headers = header_courses)

    response_exams = requests.get(EXAMS_SERVICE_URL+course_id,
                                    headers = header_exams)
    
    courses_json = response_courses.json()
    exams_json = response_exams.json()
    courses_json['metrics']['exams_amount'] = exams_json['amount']
    courses_json['metrics']['average_score'] = exams_json['average_score']
    courses_json['metrics']['approval_rate'] = exams_json['approval_rate']
    courses_json['metrics']['graded_exams'] = exams_json['amount_graded']
    courses_json['metrics']['passed_exams'] = exams_json['approval_rate'] * exams_json['amount']
    
    return courses_json


def get_metrics():

    response_courses = requests.get(COURSES_SERVICE_URL,
                                    headers = header_courses)
    courses_json = response_courses.json()
    result_list = []
    for course in courses_json['courses']:
        c_id = course['id']
        course_metrics = get_metrics_by_id(c_id)
        result_list.append(course_metrics)
    
    return result_list
    
