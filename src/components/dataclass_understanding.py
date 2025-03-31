# The @dataclass decorator is used to create classes that are mainly for storing data.
# It automatically generates special methods like __init__, __repr__, and __eq__ for the class.
# This makes the code cleaner and reduces the amount of boilerplate code needed.
# You can also specify types for the attributes, set default values, and create immutable classes if needed.

from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int
    city: str = "Unknown"  # Default value for city

# Example usage:
person1 = Person(name="Alice", age=30)
print(person1)  # Output: Person(name='Alice', age=30, city='Unknown')

# Notes:
# The @dataclass decorator automatically generates the __init__, __repr__, and __eq__ methods.
# This makes the code cleaner and easier to read and maintain.

# ---------------------------------------------------------------

# Without using @dataclass (more boilerplate code)
class PersonWithoutDataclass:
    def __init__(self, name: str, age: int, city: str = "Unknown"):
        self.name = name
        self.age = age
        self.city = city

    def __repr__(self):
        return f"PersonWithoutDataclass(name='{self.name}', age={self.age}, city='{self.city}')"

    def __eq__(self, other):
        if isinstance(other, PersonWithoutDataclass):
            return (self.name, self.age, self.city) == (other.name, other.age, other.city)
        return False

# Example usage without dataclass
person2 = PersonWithoutDataclass(name="Bob", age=25)
print(person2)  # Output: PersonWithoutDataclass(name='Bob', age=25, city='Unknown')

# Notes:
# This version requires manually defining the __init__, __repr__, and __eq__ methods.
# It is more verbose and less clean compared to the dataclass version.