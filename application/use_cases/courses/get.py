import os
import requests
import json
from dotenv import load_dotenv
load_dotenv()

COURSES_SERVICE_API_KEY = os.getenv('COURSES_SERVICE_API_KEY')
COURSES_SERVICE_URL = "https://staging-courses-service-app.herokuapp.com/courses/"

EXAMS_SERVICE_API_KEY = os.getenv('EXAMS_SERVICE_API_KEY')
EXAMS_SERVICE_URL = "https://staging-exams-service.herokuapp.com/exams/solutions/course/"

header_courses = {"apikey": COURSES_SERVICE_API_KEY}
header_exams = {"apikey": EXAMS_SERVICE_API_KEY}

def get_metrics_by_id(course_id):

    
    response_courses = requests.get(COURSES_SERVICE_URL+course_id,
                            headers = header_courses)

    response_exams = requests.get(EXAMS_SERVICE_URL+course_id,
                                    headers = header_exams)
    
    courses_json = response_courses.json()['metrics']
    exams_json = response_exams.json()
    courses_json['exams_amount'] = exams_json['amount']
    courses_json['average_score'] = exams_json['average_score']
    courses_json['approval_rate'] = exams_json['approval_rate']
    courses_json['graded_exams'] = exams_json['amount_graded']
    courses_json['passed_exams'] = exams_json['approval_rate'] * exams_json['amount']
    
    return {
        "course_id": course_id,
        "metrics": courses_json
    }    


def get_metrics():

    response_courses = requests.get(COURSES_SERVICE_URL,
                                    headers = header_courses)
    courses_json = response_courses.json()
    dicc = {"total_users": 0,
            "users_approved": 0,
            "users_currently_studying": 0,
            "exams_amount": 0,
            "average_score": 0,
            "approval_rate": 0,
            "graded_exams": 0,
            "passed_exams": 0
        }

    for course in courses_json['courses']:
    
        response_exams = requests.get(EXAMS_SERVICE_URL+course['id'],
                                    headers = header_exams)
        exams_json = response_exams.json()
        dicc['total_users'] += course['metrics']['total_users']
        dicc['users_approved'] += course['metrics']['users_approved']
        dicc['users_currently_studying'] += course['metrics']['users_currently_studying']
        dicc['exams_amount'] += exams_json['amount']
        dicc['average_score'] += exams_json['average_score']
        dicc['approval_rate'] += exams_json['approval_rate']
        dicc['graded_exams'] += exams_json['amount_graded']
        dicc['passed_exams'] += exams_json['approval_rate'] * exams_json['amount']
    
    return {
        "courses_amount": courses_json['amount'],
        "metrics": dicc
    }

    
