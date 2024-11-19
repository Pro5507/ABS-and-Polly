
class animal():
    def move(self):
        pass
class humen(animal):
    def move(self):
        print("I can walk and run")
class snake(animal):
    def move(self):
        print("I can crawl")
class dog(animal):
    def move(self):
        print("I can bark")
o1= humen()
o1.move()
o2= snake()
o2.move()
o3= dog()
o3.move()