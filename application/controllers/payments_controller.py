from application.use_cases.payments import get

class PaymentsController:

    @classMethod
    def get_metrics(cls):

        return get.get_metrics()