from fastapi import APIRouter, Header, Query, Depends
from application.controllers.courses_controller import *
from application.controllers.users_controller import *
from application.controllers.payments_controller import *
from application.services.auth import auth_service
from typing import Optional

router = APIRouter()

#Courses
@router.get('/courses/{course_id}', response_model = dict, status_code = 200)
async def get_courses_metrics_by_id(course_id: str,
                                apikey: str = Header(None)
                            ):

    auth_service.check_api_key(apikey)
    return CoursesController.get_metrics_by_id(course_id)

@router.get('/courses/', status_code = 200)
async def get_all_courses_metrics(apikey: str = Header(None),
                                category: Optional[int] = None,
                                subscription: Optional[str] = None
                                ):

    auth_service.check_api_key(apikey)
    return CoursesController.get_metrics(category, subscription)


#Users
@router.get('/users/{user_id}', response_model = dict, status_code = 200)
async def get_user_metrics_by_id(user_id: str,
                                apikey: str = Header(None)
                                ):

    auth_service.check_api_key(apikey)
    return UsersController.get_metrics_by_id(user_id)


@router.get('/users/', response_model = dict, status_code = 200)
async def get_users_metrics(apikey: str = Header(None)):

    auth_service.check_api_key(apikey)
    return UsersController.get_metrics()


#Payments
@router.get('/payments/', status_code = 200)
async def get_payments_metrics(apikey: str = Header(None)):

    auth_service.check_api_key(apikey)
    return PaymentsController.get_metrics()