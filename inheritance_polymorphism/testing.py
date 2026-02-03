#class Animal:
#    def __init__(self, name):
 #       self.name = name

#    def sound(self):
#        return f'{self.name} makes a sound!'

#class Dog(Animal):
#    bark = 'woof! woof!! woof!!!'

#    def sound(self):
#        base = super().sound()
#        return f"{base}, then {self.name} barks {self.bark}"

#jack = Dog('Jack')
#print(jack.sound())

class Walker:
    def walk(self):
        return 'I can walk on land'

class Swimmer:
    def swim(self):
        return 'I can swim in water'

class Amphibian(Walker, Swimmer):
    def __init__(self, name):
        self.name = name

    def introduce(self):
        return f"I'm {self.name} the frog. {self.walk()} and {self.swim()}"

frog = Amphibian('Freddy')
print(frog.introduce())


class Twitter:
    def __init__(self, content):
        self.content = content
    def post(self):
        return f"Tweet: '{self.content}' (280 chars max)"

class Instagram:
    def __init__(self, content):
        self.content = content

    def post(self):
        return f"Instagram post: '{self.content}' + filters"

class LinkedIn:
    def __init__(self, content):
        self.content = content

    def post(self):
        return f"LinkedIn Post: '{self.content}' (Professional Mode)"

def start(social_media):
    print(social_media.post())

#Creates instances
tweet = Twitter('I just learned Python polymorphism!')
photo = Instagram('Sunset vibes')
article = LinkedIn("Why OOP matters in 2026")


#polymorph calls
start(tweet)
start(photo)
start(article)

class Animal:
    def speak(self):
        return 'Some generic sound'

class Cat(Animal):
    def speak(self):
        return 'A cat meow'

class Dog(Animal):
    def speak(self):
        return 'A dog barks woof woof'

class Monkey(Animal):
    def speak(self):
        return 'A monkey ooh ooh aah aah ooh ooh aah aah'

print(Cat().speak()) # A cat meow
print(Dog().speak()) # A dog barks woof woof
print(Monkey().speak()) # A monkey ooh ooh aah aah ooh ooh aah aah
print(Animal().speak()) # Some generic sound
