class Person():


    def __init__(self,name,tall):
        print('初始化')
        self.name = name
        self.tall = tall

if __name__ == '__main__':
   someOne = Person('Alan',170)
   anotherOne = Person("Jenny",160)
   print(someOne.name)