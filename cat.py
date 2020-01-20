from baby import Baby
from type import Type
class Cat(Baby, Type):
    def __init__(self, eyeColor, hairColor, toes):
        Baby.__init__(self, eyeColor, hairColor, toes)
        self.type = "cat"
    def about_me(self):
        print("I am a cat baby!")