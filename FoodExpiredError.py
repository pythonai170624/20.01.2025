
class FoodExpiredError(Exception):
    def __init__(self, message):
        #### whatever I want
        super().__init__(message)