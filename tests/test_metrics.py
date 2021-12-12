import json
import os
from tests.conftest import test_app
from unittest import TestCase, mock
#from application.use_cases.courses.get import (get_metrics, get_metrics_by_id)
#from application.use_cases.payments.get import get_metrics
#from application.use_cases.users.get import (get_metrics, get_metrics_by_id)

header = {"apikey": os.getenv('API_KEY')}


class CoursesMetricsTest(TestCase):

    @mock.patch("application.use_cases.courses.get.get_metrics")
    def test_courses_without_apikey(self, mock_get):

        mock_get.return_value.status_code = 401
        response = test_app.get("/metrics/courses/")
        response_json = response.json()

        assert response.status_code == 401
        assert response_json["message"] == "Error with API Key"


    @mock.patch("application.use_cases.courses.get.get_metrics")
    def test_courses_metrics(self, mock_get):

        mock_get.return_value.status_code = 200
        mock_get.return_value = {
            "courses_amount": 2,
            "metrics": {
                "total_users": 12,
                "users_approved": 3,
                "users_currently_studying": 9,
                "exams_amount": 3,
                "average_score": 0,
                "approval_rate": 1,
                "graded_exams": 3,
                "passed_exams": 3
            }
        }
        response = test_app.get("/metrics/courses/", headers = header)
        response_json = response.json()
      
        assert response.status_code == 200
        assert response_json == {
            "courses_amount": 2,
            "metrics": {
                "total_users": 12,
                "users_approved": 3,
                "users_currently_studying": 9,
                "exams_amount": 3,
                "average_score": 0,
                "approval_rate": 1,
                "graded_exams": 3,
                "passed_exams": 3
            }
        }
       

    @mock.patch("application.use_cases.courses.get.get_metrics_by_id")
    def test_course_metrics_by_id(self, mock_get):

        course_id = "278f684b-69e2-4ad2-9d23-b64f971cf874"
        mock_get.return_value.status_code = 200
        mock_get.return_value = {
            "course_id": course_id,
            "metrics": {
                "total_users": 5,
                "users_approved": 0,
                "users_currently_studying": 5,
                "exams_amount": 0,
                "average_score": 0,
                "approval_rate": 0,
                "graded_exams": 0,
                "passed_exams": 0
            }
        }
        response = test_app.get("/metrics/courses/"+course_id, headers = header)
        response_json = response.json()
        
        assert response.status_code == 200
        assert response_json == {
            "course_id": course_id,
            "metrics": {
                "total_users": 5,
                "users_approved": 0,
                "users_currently_studying": 5,
                "exams_amount": 0,
                "average_score": 0,
                "approval_rate": 0,
                "graded_exams": 0,
                "passed_exams": 0
            }
        }


    @mock.patch("application.use_cases.courses.get.get_metrics_by_id")
    def test_course_metrics_inexistent(self, mock_get):

        course_id = "278f685b-69e2-4ad2-9d23-b64f971cf871"
        mock_get.return_value.status_code = 200
        
        response = test_app.get("/metrics/courses/"+course_id, headers = header)
        response_json = response.json()
        
        assert response.status_code == 200
        assert response_json == {}        


    @mock.patch("application.use_cases.courses.get.get_metrics")
    def test_courses_metrics_filtered_both(self, mock_get):

        mock_get.return_value.status_code = 200
        mock_get.return_value = {
            "courses_amount": 2,
            "metrics": {
                "total_users": 12,
                "users_approved": 3,
                "users_currently_studying": 9,
                "exams_amount": 3,
                "average_score": 0,
                "approval_rate": 1,
                "graded_exams": 3,
                "passed_exams": 3
            }
        }
        response = test_app.get("/metrics/courses/?category[]=1&subscription_type[]=free",
                                headers = header)
        response_json = response.json()
        
        assert response.status_code == 200
        assert response_json == {
            "courses_amount": 2,
            "metrics": {
                "total_users": 12,
                "users_approved": 3,
                "users_currently_studying": 9,
                "exams_amount": 3,
                "average_score": 0,
                "approval_rate": 1,
                "graded_exams": 3,
                "passed_exams": 3
            }
        }

    
    @mock.patch("application.use_cases.courses.get.get_metrics")
    def test_courses_metrics_filtered_cat(self, mock_get):

        mock_get.return_value.status_code = 200
        mock_get.return_value = {
            "courses_amount": 2,
            "metrics": {
                "total_users": 12,
                "users_approved": 3,
                "users_currently_studying": 9,
                "exams_amount": 3,
                "average_score": 0,
                "approval_rate": 1,
                "graded_exams": 3,
                "passed_exams": 3
            }
        }
        response = test_app.get("/metrics/courses/?category[]=1",
                                headers = header)
        response_json = response.json()
        
        assert response.status_code == 200
        assert response_json == {
            "courses_amount": 2,
            "metrics": {
                "total_users": 12,
                "users_approved": 3,
                "users_currently_studying": 9,
                "exams_amount": 3,
                "average_score": 0,
                "approval_rate": 1,
                "graded_exams": 3,
                "passed_exams": 3
            }
        }


    @mock.patch("application.use_cases.courses.get.get_metrics")
    def test_courses_metrics_filtered_subs(self, mock_get):

        mock_get.return_value.status_code = 200
        mock_get.return_value = {
            "courses_amount": 2,
            "metrics": {
                "total_users": 12,
                "users_approved": 3,
                "users_currently_studying": 9,
                "exams_amount": 3,
                "average_score": 0,
                "approval_rate": 1,
                "graded_exams": 3,
                "passed_exams": 3
            }
        }
        response = test_app.get("/metrics/courses/?subscription_type[]=free",
                                headers = header)
        response_json = response.json()
        
        assert response.status_code == 200
        assert response_json == {
            "courses_amount": 2,
            "metrics": {
                "total_users": 12,
                "users_approved": 3,
                "users_currently_studying": 9,
                "exams_amount": 3,
                "average_score": 0,
                "approval_rate": 1,
                "graded_exams": 3,
                "passed_exams": 3
            }
        }

    
    @mock.patch("application.use_cases.users.get.get_metrics")
    def test_users_metrics(self, mock_get):

        
        mock_get.return_value.status_code = 200
        mock_get.return_value = {
            "users_amount": 5,
            "metrics": {
                "registered_with_mail": 3,
                "registered_with_app": 2,
                "logged_with_mail": 4,
                "logged_with_app": 1,
                "times_pw_changed": 3
            }
        }
        response = test_app.get("/metrics/users/", headers = header)
        response_json = response.json()
        
        assert response.status_code == 200
        assert response_json == {
            "users_amount": 5,
            "metrics": {
                "registered_with_mail": 3,
                "registered_with_app": 2,
                "logged_with_mail": 4,
                "logged_with_app": 1,
                "times_pw_changed": 3
            }
        }


    @mock.patch("application.use_cases.users.get.get_metrics")
    def test_users_without_apikey(self, mock_get):

        mock_get.return_value.status_code = 401
        response = test_app.get("/metrics/users/")
        response_json = response.json()

        assert response.status_code == 401
        assert response_json["message"] == "Error with API Key"


    @mock.patch("application.use_cases.users.get.get_metrics_by_id")
    def test_user_metrics_by_id(self, mock_get):

        user_id = "4a2d3fc7-5afe-489b-bdd8-20b600854a91"
        mock_get.return_value.status_code = 200
        mock_get.return_value = {
            "user_id": user_id,
            "metrics": {
               "registered_with_mail": False,
                "registered_with_app": False,
                "logged_with_mail": False,
                "logged_with_app": False,
                "times_pw_changed": 0
            }
        }
        response = test_app.get("/metrics/users/"+user_id, headers = header)
        response_json = response.json()
  
        assert response.status_code == 200
        assert response_json == {
            "user_id": user_id,
            "metrics": {
               "registered_with_mail": False,
                "registered_with_app": False,
                "logged_with_mail": False,
                "logged_with_app": False,
                "times_pw_changed": 0
            }
        }
    

    @mock.patch("application.use_cases.payments.get.get_metrics")
    def test_payments_metrics(self, mock_get):

        mock_get.return_value.status_code = 200
        mock_get.return_value = {
            "2021-11-28": {
                "amount_transactions": 2,
                "total_money_sent": 0.04301
            }
        }
        response = test_app.get("/metrics/payments/", headers = header)
        response_json = response.json()
        
        assert response.status_code == 200
        assert response_json == {
            "2021-11-28": {
                "amount_transactions": 2,
                "total_money_sent": 0.04301
            }
        }


    @mock.patch("application.use_cases.payments.get.get_metrics")
    def test_payments_without_apikey(self, mock_get):

        mock_get.return_value.status_code = 401
        response = test_app.get("/metrics/payments/")
        response_json = response.json()

        assert response.status_code == 401
        assert response_json["message"] == "Error with API Key"


    