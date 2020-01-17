#!usr/bin/python3.7



class Car:
    def __init__(self, name):
        self.name = name

    def exclaim(self):
        print("I am a ", self.name)

class Yugo(Car):
    #instance method override
    def exclaim(self):
        print("I am a Yugo!")

    def need_a_push(self):
        print('A little help here?')

if __name__ == '__main__':
    car = Car('blackCar')
    print(car.name)
    car.exclaim()
    myYugo = Yugo('whiteYugo')
    print(myYugo.name)
    myYugo.exclaim()
    myYugo.need_a_push()