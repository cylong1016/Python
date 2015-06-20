class Base:
    def __init__(self):
        self.data = []
	self.c = 0;
    def add(self, x):
        self.data.append(x)
    def addtwice(self, x):
        self.add(x)
        self.add(x)

# Child extends Base
class Child(Base):
    def plus(self,a,b):
	print self.c;
        return a+b

oChild =Child()
oChild.addtwice("str1")
print oChild.data
print oChild.plus(2,3)
oChild.x = 9
print oChild.xd
