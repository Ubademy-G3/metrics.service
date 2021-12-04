from application.use_cases.users import get

class UsersController:

    @classmethod
    def get_metrics_by_id(cls, user_id):

        return get.get_metrics_by_id(user_id)

    
    @classmethod
    def get_metrics(cls):

        return get.get_metrics()
