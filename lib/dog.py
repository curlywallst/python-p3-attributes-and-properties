#!/usr/bin/env python3

class Dog:
    breeds = ["Pug", "Mutt"]
    def get_name(self):
        print("name")
        return self._name

    def set_name(self, name):
        if type(name) == str and len(name) > 0 and len(name) < 26:
            self._name = name
        else:
            print("Name must be string between 1 and 25 characters.")

    name = property(get_name, set_name)

    def get_breed(self):
        return self._breed

    def set_breed(self, breed):
        if breed in Dog.breeds:
            self._breed = breed
        else:
            print("Breed must be in list of approved breeds.")

    breed = property(get_breed, set_breed)