class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        if self.weight > 29:
            print(self.name, 'says "WOOF WOOf"')
        else:
            print(self.name, 'says "woof woof"')

    def human_years(self):
        print(self.name, 'is ',self.age * 7, 'years old in human years')

    def __str__(self):
        return "I'm a dog named " + self.name

def print_dog(dog):
        print(dog.name + "'s", 'age is', dog.age, 'and weight is', dog.weight)

class ServiceDog(Dog):
    def __init__(self, name, age, weight, handler):
        Dog.__init__(self, name, age, weight)
        self.handler = handler
        self.is_working = False

    def walk(self):
        print(self.name, 'is helping its handler', self.handler, 'walk')

    def bark(self):
        if self.is_working:
            print(self.name, 'says, "I can\'t bark, I\'m working"')
        else:
            Dog.bark(self)

class SeeingEyeDog(ServiceDog):
    def __init__(self, name, age, weight, handler):
        ServiceDog.__init__(self, name, age, handler)

    def listen(self):    
        print(self.name, 'is helping its handler', self.handler, 'listen')

class Frisbee:
    def __init__(self, color):
        self.color = color

    def __str__(self):
        return "I'm a " + self.color +' frisbee'

class FrisbeeDog(Dog):
    def __init__(self, name, age, weight):
        Dog.__init__(self, name, age, weight)
        self.frisbee = None

    def bark(self):
        if self.frisbee != None:
            print(self.name, 'says, "I can\'t bark, I have a frisbee in my mouth."')
        else:
            Dog.bark(self)

    def catch(self, frisbee):
        self.frisbee = frisbee
        print(self.name, 'caught a', frisbee.color, 'frisbee')

    def give(self):
        if self.frisbee != None:
            frisbee = self.frisbee
            self.frisbee = None
            print(self.name, 'gives back', frisbee.color, 'frisbee')
            return frisbee
        else:
            print(self.name, "doesn't have a frisbee")


    def __str__(self):
        msg = "I'm a dog named " + self.name
        if self.frisbee != None:
            msg = msg + ' and I have a frisbee'
        return msg

### Below lines are test code. ###
codie = Dog('Codie', 12, 38)
jackson = Dog('Jackson', 9, 12)
codie.human_years()
jackson.human_years()
print_dog(jackson)

rody = ServiceDog('Rody', 8, 38, 'Joseph')
print("This dog's name is", rody.name)
print("This dog's handler is", rody.handler)
print_dog(rody)
rody.bark()
rody.walk()
rody.human_years()

mystery_dog = ServiceDog('Mystery', 5, 13, 'Helen')

if isinstance(mystery_dog, ServiceDog):
    print("Yup, it's a ServiceDog")
else:
    print('That is no ServiceDog')

if isinstance(mystery_dog, Dog): 
    print("Yup, it's a Dog")
else:
    print('That is no Dog')

if isinstance(mystery_dog, SeeingEyeDog): 
    print("Yup, it's a SeeingEyeDog")
else:
    print('That is no SeeingEyeDog')

print(codie)
print(jackson)
print(rody)
print(mystery_dog)

rody.bark()
rody.is_working = True
rody.bark()

mystery_dog.bark()
mystery_dog.is_working = True
mystery_dog.bark()

popawi = FrisbeeDog('Popawi', 5, 26)
red_frisbee = Frisbee('red')

print(popawi)
popawi.bark()
popawi.catch(red_frisbee)

popawi.bark()
print(popawi)
popawi.give()
popawi.bark()
