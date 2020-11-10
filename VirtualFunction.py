from abc import ABCMeta, abstractmethod
class Shape:
    __metaclass__=ABCMeta
    def __init__(self, Shapetype):
        self.Shapetype=Shapetype
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
class Rectangle(Shape):
    def __init__(self, length, breadth):
        Shape.__init__(self,'Rectangle')
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth
    def perimeter(self):
        return 2*(self.length+self.breadth)
class Circle(Shape):
    pi=3.14
    def __init__(self, radius):
        Shape.__init__(self, 'Circle')
        self.radius=radius
    def area(self):
        return round(Circle.pi * (self.radius**2), 2)
    def perimeter(self):
        return round(2*Circle.pi*self.radius, 2)
class Square(Shape):
    def __init__(self, side):
        Shape.__init__(self, 'Square')
        self.side=side
    def area(self):
        return self.side*self.side
    def perimeter(self):
        return 4*self.side
class Triangle(Shape):
    def __init__(self, base, height, side):
        Shape.__init__(self, 'Triangle')
        self.base=base
        self.height=height
        self.side=side
    def area(self):
        return 0.5*self.base*self.height
    def perimeter(self):
        return self.base+self.height+self.side
class Ellipse(Shape):
    pi=3.14
    def __init__(self, majoraxis, minoraxis):
        Shape.__init__(self, 'Circle')
        self.majoraxis=majoraxis
        self.minoraxis=minoraxis
    def area(self):
        return pi*self.majoraxis*self.minoraxis
    def perimeter(self):
        return 45
a=Rectangle(2,3)
b=Circle(2)
c=Square(7)
d=Triangle(2,3,4)
e=Ellipse(2,3)






        
