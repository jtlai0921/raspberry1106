class Person():
    def __init__(self,name='robert',tall=100):
        self.name = name
        self.tall = tall


class Car():
    def __init__(self,name):
        self.name = name

    def exclaim(self):
        print("I'm a Car")

class Yugo(Car):
    def __init__(self,name,weight):
        super().__init__(name)
        self.weight = weight

    def exclaim(self): #override method
        print("I'm a Yugo")



if __name__ == '__main__':
   give_me_a_car = Car('happyCar')
   give_me_a_car.exclaim()
   print('carName=', give_me_a_car.name)

   give_me_a_yugo = Yugo('Happy Yugo',59)
   give_me_a_yugo.exclaim()
   print('yugoName=',give_me_a_yugo.name)