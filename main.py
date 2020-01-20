# inheritance

# Class based inheritance lets you specify that one type will contain all of the properties and methods that are defined in another type, without having to duplicate the code in the two source code files.

# the parent class is called super class or base class and the child class is called subclass or derived class.

# Overriding methods
# To override a method in the base class, sub class needs to define a method of same signature. (i.e same method name and same number of parameters as method in base class).

from baby import Baby
from cat import Cat

human_baby = Baby("green", "brown", "weird")

cat_baby = Cat("Grey", "brown", "normal")

human_baby.about_me()

cat_baby.about_me()