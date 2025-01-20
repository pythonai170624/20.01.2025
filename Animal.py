
class Animal:
    def __init__(self, name):
        # encapsulation __ getter setter
        self.name = name

    def say_my_name(self):
        print(self.name)

    def speak(self):
        pass

# Dog is Animal
class Dog(Animal):

     def speak(self):
        return 'haw haw'

# dog is labrador
class Labrador(Dog):
    def __init__(self, iq: float):
        self.__iq = iq

    @iq.setter
    def iq(self):
        pass

# cat is dog -- wrong!
class Cat(Dog):
    pass

dog = Animal('dog')
cat = Animal('cat')
bird = Animal('bird')
elephant = Animal('elephant', 2.5)

labreador1 = Labrador()