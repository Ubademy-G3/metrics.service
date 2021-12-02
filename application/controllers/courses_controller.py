from application.use_cases.courses import get

class CoursesController:

    @classmethod
    def get_metrics_by_id(cls, course_id):

        return get.get_metrics_by_id(course_id)


    @classmethod
    def get_metrics(cls):

        return get.get_metrics()