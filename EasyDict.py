class EasyDict:

    """Accepts a Dict and creates an instance which can work with key & attribute lookups"""

    def __init__(self, input_dict={}):
        self.__dict__.update(input_dict)

    # Support key lookups
    def __getitem__(self, index):
        return self.__dict__[index]

    # Support key & attribute assignment
    def __setitem__(self, key, value):
        self.__dict__[key] = value


person = EasyDict({'name': "Trey Hunner", 'location': "San Diego"})
print(person.name)
print(person['location'])
person.location = "Portland"
print(person['location'])
