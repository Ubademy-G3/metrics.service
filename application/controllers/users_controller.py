from application.use_cases.users import get

class UsersController:

    @classmethod
    def get_metrics(cls):

        return get.get_metrics()