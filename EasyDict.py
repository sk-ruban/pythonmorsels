class EasyDict:

    """Accepts a Dict and creates an instance which can work with key & attribute lookups"""

    # Use **kwargs for accepting optional key-word arguments
    def __init__(self, input_dict = {}, **kwargs):
        self.__dict__.update(input_dict)
        self.__dict__.update(kwargs)

    # Support key & index lookups
    def __getitem__(self, key):
        return self.__dict__[key]

    # Support key & attribute assignment
    def __setitem__(self, key, value):
        self.__dict__[key] = value

    '''
    # Trey's Solution
    # To Test for equality
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    # Does the same thing as __getitem__, except it provides a default value
    def get(self, key, default=None):
        return getattr(self, key, default)
    '''


person = EasyDict({'name': "Trey Hunner", 'location': "San Diego"})
print(person.name)
print(person['location'])
person.location = "Portland"
print(person['location'])

person = EasyDict(name="Trey Hunner", location="San Diego")
print(person.location)