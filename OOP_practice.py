# OOP practice

# Write a class describing some animal or any other being/entity by your choice (see more examples below).

# Instances of that class should have at least 2 attributes - for example in case of animal - name, hungry, color, etc..
# The class also should declare at least 3 methods. Sample methods for animal:
# hello() – it should print some nice words describing object (animal) name and it's color/type etc.
# trick() – kind of sound or any other output – for example for sound it should print something randomly chosen sound - like a "bark" or "gav- gav" for dog etc.
# feed() – the object should have from the beginning boolean "hunger" attribute equals to True (it is hungry). After performing feed() object should thank you and became non-hungry. Second time you try to feed him it should refuse. After 3 "sound" action it should became hungry again and refuse to play tricks.
# Note: Please treat above as just the example and develop your own class modelling anything you want. Another good options to try out:

# 🌳Plant, 👶🏼 Tamagochi, 🤖Robot, 👾 Alien - similar to 🐵 Animal
# ⚔️ Player for some RRG game (name, class, health, strength, dexterity, methods - fight, heal/rest, power-up, etc.)
# 👨‍🎓 Student (name, group, age, methods: learn, party)
# 📱 Phone (name/model, manufacturer, ram, cpu, methods: charge, sms, power_on, power_off, etc.)
# 📗 Book (name, author, length, genre, methods: read(), time_to_read(), etc)
# There is no test for this task. Let your imagination be your limit for this one!

import random

class Animal:
    "Sample class - feel free to rename, add any attrs/methods you like"
    
    def __init__(self, name, kind, color):
        self.name = name
        self.kind = kind
        self.color = color
        self.hungry = True
        self.trick_count = 0
    
    def hello(self):
        return f"Hello, I am {self.name}, a {self.color} {self.kind}."
    
    def trick(self):
        sounds = ["Bark", "Meow", "Roar", "Chirp", "Squeak"]
        sound = random.choice(sounds)
        return f"{self.name} says: {sound}!"
    
    def feed(self):
        if self.hungry:
            self.hungry = False
            return f"{self.name} says: Thank you for feeding me!"
        else:
            return f"{self.name} is not hungry right now."
    
    def play(self):
        if self.trick_count >= 3:
            self.hungry = True
            self.trick_count = 0
            return f"{self.name} says: I'm hungry now. Time to eat!"
        else:
            self.trick_count += 1
            return f"{self.name} performs a trick."

zhuchka = Animal("Zhuchka", "dog", "brown")
print(zhuchka.hello())
print(zhuchka.trick())
print(zhuchka.feed())