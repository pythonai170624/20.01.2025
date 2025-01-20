

from FoodExpiredError import *
from datetime import datetime, timedelta

class FoodProduct:
    def __init__(self, name: str, price: float, category: str,
                 production_date: datetime, expiration_date: datetime):
        # 1
        # self.__name = name  # without setter -- not good
        # 2
        self.name = name # with setter -- better

        self.price = price
        self.category = category
        self.production_date = production_date
        self.__expiration_date = expiration_date

    # def get_name(self):
    #     return self.__name

    @property
    def name(self): # getter
        return 'Fruit name is: ' + self.__name.upper()

    @name.setter
    def name(self, value):  # setter
        if not isinstance(value, str):
            raise TypeError(f'setter for name must receive str and got type {type(value)} {value}')
        if len(value) < 3:
            raise Exception(f'setter for name must get str with len 3.value=  {value}')
        if len(set(value)) == 1:
            raise ValueError(f'setter for name must got repeating str. value={value}')
        self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        # type check -- float
        if not (0.1 <= value <= 100):
            raise ValueError(f"price must be between 0.1-100. value={value}")
        self.__price = value

    @property
    def category(self):
        return self.__category

    @category.setter
    def category(self, value):
        if value not in ['parve', 'meat', 'dairy']:
            raise ValueError(f"category must be 'parve', 'meat', 'dairy', value = {value}")
        self.__category = value

    @property
    def production_date(self):
        return self.__production_date

    @production_date.setter
    def production_date(self, value):
        if value >= datetime.now():
            raise ValueError(f"production day must be in the past. value={value}")
        self.__production_date = value

    @property
    def expiration_date(self):
        return self.__expiration_date

    @expiration_date.setter
    def expiration_date(self, value):
        if value <= datetime.now() + timedelta(days=7):
            raise ValueError(f"expiration day must one week in the future." +
                             f"we sell fresh only. value={value}")
        self.expiration_date = value

    @property
    def remaining(self):
        remain = (self.expiration_date - datetime.now()).days
        if remain < 0:
            raise FoodExpiredError(f"{self.name} has expired! expiration day is {self.expiration_date}")
        return (self.expiration_date - datetime.now()).days


banana = FoodProduct('banana', 1.0, 'parve',
                     production_date=datetime.now() - timedelta(days=10),
                     expiration_date=datetime.now() - timedelta(days=10))

try:
    print(banana.remaining)
except FoodExpiredError as e:
    print(e)

print(banana.name)
# banana.name = datetime.now()
# banana.name = 12
banana.name = 'abbbb'
#banana.price = 1
# print(banana.get_name)
print(banana.name)