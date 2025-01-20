from OrderNotExistError import *

class Humus:
    def __init__(self, pita):
        print('creating new humus')
        self.pita = pita

    def __str__(self):
        return f"Large plate of humus with {self.pita} pitot"

    def __repr__(self):
        return f"Large plate of humus with {self.pita} pitot"

class Cake:
    def __init__(self):
        print('creating new cake')

    def __str__(self):
        return f"Large cake"

    def __repr__(self):
        return f"Large cake"

class Restaurant:
    def __init__(self, pita):
        self.pita = pita

    def order_from_waitress(self, order):
        result = self.checker(order)
        return result

    def checker(self, order):
        try:
            result = self.cook(order)
            return result
        except OrderNotExistError as e:
            # write to log file ... write e to file ...
            return Cake(), 0

    def owner(self):
        try:
            self.cook('Fillet minioun')
        except:
            pass
            # raise ...
        finally:
            print('always happends')


    def cook(self, order):
        # 1 cook knows what to do ...
        # try:
        #     if order == 'humus':
        #         self.pita -= 1
        #         humus = Humus(1)
        #         return humus, 35
        #     else:
        #         # 1 no error
        #         #print(f"there is no {order}, you will eat humus!")
        #         #humus = Humus(1)
        #         #return humus, 35 // 4
        #         # 2
        #         raise OrderNotExistError(f"order not exist value={order}")
        # except OrderNotExistError as e:
        #     # write to log file ... write e to file ...
        #     print(f'there is no {order}')
        #     humus = Humus(1)
        #     return humus, 35 // 4

        # 2 cook does NOT know what to do
        if order == 'humus':
            self.pita -= 1
            humus = Humus(1)
            return humus, 35
        else:
            try:
            # 1 no error
            #print(f"there is no {order}, you will eat humus!")
            #humus = Humus(1)
            #return humus, 35 // 4
            # 2
                raise OrderNotExistError(f"order not exist value={order}")
            finally:
                print('something bad is going to happen...')



eliyahu = Restaurant(pita=2)
result = eliyahu.order_from_waitress('humus')
result = eliyahu.order_from_waitress('steak')
print(result)

# try-except
# main -> waitress -> checker -> cook


