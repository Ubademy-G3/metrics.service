import os
import requests
import json
from dotenv import load_dotenv
load_dotenv()

import logging

logger = logging.getLogger(__name__)

COURSES_SERVICE_API_KEY = os.getenv('COURSES_SERVICE_API_KEY')
COURSES_SERVICE_URL = "https://staging-courses-service-app-v2.herokuapp.com/courses/"

EXAMS_SERVICE_API_KEY = os.getenv('EXAMS_SERVICE_API_KEY')
EXAMS_SERVICE_URL = "https://staging-exams-service.herokuapp.com/exams/solutions/course/"

header_courses = {"apikey": COURSES_SERVICE_API_KEY}
header_exams = {"apikey": EXAMS_SERVICE_API_KEY}

def get_metrics_by_id(course_id):

    logger.info("Get metrics of course %s", course_id)
    logger.debug("Making request to courses service")
    response_courses = requests.get(COURSES_SERVICE_URL+course_id,
                            headers = header_courses)
    courses_json = response_courses.json()
    logger.debug("Response: %s", str(courses_json))

    logger.debug("Making request to exams service")
    response_exams = requests.get(EXAMS_SERVICE_URL+course_id,
                                    headers = header_exams)    
    exams_json = response_exams.json()
    logger.debug("Response: %s", str(exams_json))

    courses_json['metrics']['exams_amount'] = exams_json['amount']
    courses_json['metrics']['average_score'] = exams_json['average_score']
    courses_json['metrics']['approval_rate'] = exams_json['approval_rate']
    courses_json['metrics']['graded_exams'] = exams_json['amount_graded']
    courses_json['metrics']['passed_exams'] = exams_json['approval_rate'] * exams_json['amount']

    return {
        "course_id": course_id,
        "metrics": courses_json
    }    


def get_metrics(category, subscription):

    logger.info("Get courses metrics")
    if category is None and subscription is None:
        logger.debug("Making request to courses service")
        response_courses = requests.get(COURSES_SERVICE_URL,
                                    headers = header_courses)
    if category is not None and subscription is None:
        logger.debug("Making request to courses service with filter category %s", str(category))
        response_courses = requests.get(COURSES_SERVICE_URL+"?category[]="+str(category),
                                    headers = header_courses)
    if category is not None and subscription is not None:
        logger.debug("Making request to courses service with filters category %s and subscription_type %s",
                    str(category),subscription)
        response_courses = requests.get(COURSES_SERVICE_URL+"?category[]="+str(category)+
                                    "&subscription_type[]="+subscription,
                                    headers = header_courses)
    if category is None and subscription is not None:
        logger.debug("Making request to courses service with filter subscription_type %s", subscription)
        response_courses = requests.get(COURSES_SERVICE_URL+"?subscription_type[]="+subscription,
                                    headers = header_courses)
                                    
    courses_json = response_courses.json()
    logger.debug("Response: %s", str(courses_json))
    dicc = {"total_users": 0,
            "users_approved": 0,
            "users_currently_studying": 0,
            "exams_amount": 0,
            "average_score": 0,
            "approval_rate": 0,
            "graded_exams": 0,
            "passed_exams": 0
        }
    logger.debug("Making request to exams service...")
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

    
