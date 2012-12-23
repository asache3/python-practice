# coding: UTF-8

# クラスの作り方
class Person(object):
    def __init__(self, name):
        self.name = name
    def greet(self):
        print "My name is %s." % self.name

bob = Person("Bob")
print bob.name
bob.greet()

# 継承の使い方
class SuperPerson(Person):
    def shout(self):
        print "%s is super!" % self.name

tom = SuperPerson("Tom")
tom.shout()