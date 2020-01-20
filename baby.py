# subclass or derived class
from parent import Parent
class Baby(Parent):
    def __init__(self, eyeColor, hairColor, toes):
        super().__init__(eyeColor, hairColor, toes)
        self.name = ""
        self.gender = ""
    def about_me(self):
        print("I am a baby")