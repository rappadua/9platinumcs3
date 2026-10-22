#the first step is to make the parent class named "Animal"
class Animal:
  def __init__(self, name):
    self.name = name
  #make the general eat method to be overriden by the child classes
  def eat(self):
    print(f"{self.name} is eating.")
  #make the general make_sound method to be overriden by the child classes
  def make_sound(self):
    print(f"{self.name} is sleeping.")

#make the child class named "Liomn"
class Lion(Animal):
  #make it overriding make_sound() for Lion
  def make_sound(self):
    print(f"{self.name} roars loudly!")
  #then make it overriding eat() for Lion as well
  def eat(self):
    print(f"{self.name} eats fresh meat.")

#make the child class named "Elephant"
class Elephant(Animal):
  #make it overriding make_sound() for Elephant
  def make_sound(self):
    print(f"{self.name} trumpets!")
  #overriding eat() for Elephant
  def eat(self):
    print(f"{self.name} grass and fruits.")

#lastly, make the child class "Monkey"
class Monkey(Animal):
  #it is supposed to be overriding make_sound() for Monkey
  def make_sound(self):
    print(f"{self.name} chatters!")
  #and then overriding eat() for Monkey againn
  def eat(self):
    print(f"{self.name} bananas.")
#next, create an object for each child class by inputing their own respective names like simba, dumbo, and george (all from different cartoons hehe)
lion = Lion("Simba")
elephant = Elephant("Dumbo")
monkey = Monkey("George")

#next step is to store all animals in a list
animals = [lion, elephant, monkey]
#lastly, we nthen use a loop to finally execute the overriden methods for each animal object
for animal in animals:
  animal.make_sound()
  animal.eat()
  print("_____")
