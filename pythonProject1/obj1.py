class Person():
    def __init__(self,name='robert',tall=100):
        self.name = name
        self.tall = tall




if __name__ == '__main__':
   noOne = Person()
   someOne = Person(name = "alen")
   anotherOne = Person(name='jenny',tall = 170)
   print(someOne.name)
   print(someOne.tall)
   print(anotherOne.name)
   print(anotherOne.tall)