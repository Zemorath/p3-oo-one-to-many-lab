class Pet:

    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]

    all = []
    
    def __init__(self, name, pet_type, owner=''):
        self.name = name
        if pet_type in self.PET_TYPES:
            self.pet_type = pet_type
        else:
            raise Exception
        self.owner = owner
        self.all.append(self)

class Owner:
    
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception
        else:
            pet.owner = self
    
    def get_sorted_pets(self):
        list = []
        for pet in Pet.all:
            if pet.owner == self:
                list.append(pet)
            else:
                raise Exception
        return sorted(list, key=lambda pet: pet.name)
        # return [pet for pet in Pet.all if pet.owner == self].sort()
       