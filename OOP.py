class Person:
  def __init__(self):
    pass

  def myfunc(self):
    print("Hello my name is ")

p1 = Person()
p1.myfunc()

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()
