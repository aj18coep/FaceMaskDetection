class Animals:
     def __init__(self, legs, eyes, colour):
          self.legs=legs
          self.eyes=eyes
          self.colour=colour
class Dog(Animals):
     def __init__(self, legs, eyes, colour, voice):
          Animals.__init__(self, legs, eyes, colour)
          self.voice=voice
     def char(self):
          print("legs:",self.legs)
          print("eyes:",self.eyes)
          print("colur:",self.colour)
          print("voice:",self.voice)
print("Characteristics of Dog")
d=Dog(4,2,"brown","bark")
d.char()
class Cat(Animals):
     def __init__(self, legs, eyes, colour, voice):
          Animals.__init__(self, legs, eyes, colour)
          self.voice=voice
     def char(self):
          print("legs:",self.legs)
          print("eyes:",self.eyes)
          print("colour:",self.colour)
          print("voice:",self.voice)
print("Characteristics of Cat")
c=Cat(4,2, "white", "meow")
c.char()
class Horse(Animals):
     def __init__(self, legs, eyes, colour, voice):
          Animals.__init__(self, legs, eyes, colour)
          self.voice=voice
     def char(self):
          print("legs:",self.legs)
          print("eyes:",self.eyes)
          print("colour:",self.colour)
          print("voice:",self.voice)
print("Characteristics of horse")
h=Horse(4,2, "brown", "neigh")
h.char()
class Buffalo(Animals):
     def __init__(self, legs, eyes, colour, voice):
          Animals.__init__(self, legs, eyes, colour)
          self.voice=voice
     def char(self):
          print("legs:",self.legs)
          print("eyes:",self.eyes)
          print("colour:",self.colour)
          print("voice:", self.voice)
print("Characteristics of Buffalo")
b=Buffalo(4,2,"Black", "grunt")
b.char()
class Lion(Animals):
     def __init__(self, legs, eyes, colour, voice):
          Animals.__init__(self, legs, eyes, colour)
          self.voice=voice
     def char(self):
          print("legs:",self.legs)
          print("eyes:",self.eyes)
          print("colour:",self.colour)
          print("voice:",self.colour)
print("Characteristics of Lion")
l=Lion(4,2,"Golden","roar")
l.char()
# single inheritance
# Base class
class cow:
     def func1(self):
          print("mother")
 
# Derived class
class calf(cow):
     def func2(self):
          print("baby")
 
object = calf()
object.func1()
object.func2()


# multiple inheritance
# Base class1
class cow:
    mothername = ""
    def mother(self):
        print(self.mothername)
 
# Base class2
class bull:
    fathername = ""
    def father(self):
        print(self.fathername)
 
# Derived class
class calf(cow,bull):
    def parents(self):
        print("Father :", self.fathername)
        print("Mother :", self.mothername)
 
s1 = calf()
s1.fathername = "A"
s1.mothername = "B"
s1.parents()


# multilevel inheritance
# Base class
class Grandfatheranimal:
 def __init__(self, grandfathername):
        self.grandfathername = grandfathername
 
# Intermediate class
class Fatheranimal(Grandfatheranimal):
    def __init__(self, fathername, grandfathername):
        self.fathername = fathername
 
        # invoking constructor of Grandfather class
        Grandfatheranimal.__init__(self, grandfathername)
 
class Sonanimal(Fatheranimal):
    def __init__(self,sonname, fathername, grandfathername):
        self.sonname = sonname
 
        # invoking constructor of Father class
        Fatheranimal.__init__(self, fathername, grandfathername)
 
    def print_name(self):
        print('Grandfather name :', self.grandfathername)
        print("Father name :", self.fathername)
        print("Son name :", self.sonname)
 

s1 = Sonanimal('A', 'B', 'C')
print(s1.grandfathername)
s1.print_name()

# Hierarchical inheritance
# Base class
class Parent:
      def func1(self):
          print("This function is in parent class.")
 
# Derived class1
class Child1(Parent):
      def func2(self):
          print("This function is in child 1.")
 
# Derivied class2
class Child2(Parent):
      def func3(self):
          print("This function is in child 2.")
  
object1 = Child1()
object2 = Child2()
object1.func1()
object1.func2()
object2.func1()
object2.func3()

# hybrid inheritance
 
 
class Bull:
     def func1(self):
         print("Parent")
  
class Calf1(Bull):
     def func2(self):
         print("Child")
         print("moo")
  
class Calf2(Bull):
     def func3(self):
         print("Child")
         printf("moo")
  
class Calf3(Calf1, Bull):
     def func4(self):
         print("Child")
  
object = Calf3()
object.func1()
object.func2()



