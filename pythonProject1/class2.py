#!usr/bin/python3.7



class Car:
    def exclaim(self):
        print("I am a Car!")

class Yugo(Car):
    #instance method override
    def exclaim(self):
        print("I am a Yugo!")

if __name__ == '__main__':
    car = Car()
    car.exclaim()
    myYugo = Yugo()
    myYugo.exclaim()