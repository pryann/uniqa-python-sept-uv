from dataclasses import dataclass


@dataclass(slots=True)
class User:
    first_name: str
    last_name: str
    age: int


user = User("John", "Doe", 33)
print(user)
