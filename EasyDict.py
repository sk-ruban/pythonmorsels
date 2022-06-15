class EasyDict:

    """Accepts a Dict and creates an instance which can work with key & attribute lookups"""

    # Use **kwargs for accepting optional key-word arguments (**)
    def __init__(self, input_dict = {}, **kwargs):
        # Store variables with self.__dict__.update()
        self.__dict__.update(input_dict)
        self.__dict__.update(kwargs)

    # Support key & index lookups
    def __getitem__(self, key):
        return self.__dict__[key]

    # Support key & attribute assignment
    def __setitem__(self, key, value):
        self.__dict__[key] = value

    # Testing for Equality
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def get(self, key, default=None):
        return getattr(self, key, default)


# Base Problem
person = EasyDict({'name': "Ruban", 'location': "Singapore"})
print(person.name)
print(person['location'])

# Bonus 1 - Key & Attribute Assignment
person.location = "Gran Canaria"
print(person['location'])

# Bonus 2 - Accept Keyword Arguments
person = EasyDict(name="Ruban", location="Singapore")
print(person.location)
print(person == EasyDict(name="Bob", location="Singapore"))
print(person == EasyDict(name="Ruban", location="Singapore"))
print(person.get('profession'))
print(person.get('profession', 'unknown'))