# convention: snake_case,
# a-z, A-Z, 0-9 (not start with number), _ (special)


class Person:
    __slots__ = (
        "__identity",
        "__salary",
        "age",
        "first_name",
        "last_name",
    )

    def __init__(self, first_name: str, last_name: str, age: int, identity: str, salary: float) -> None:
        self.__identity = identity
        self.__salary = salary
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"first_name: {self.first_name}, last_name: {self.last_name}, age: {self.age}"

    def log_identity(self):
        print(self.__identity)

    @property
    def salary(self):
        return f"{self.__salary:.4f}"

    @salary.setter
    def salary(self, value):
        top_salary = 200_000

        # if value >= top_salary:
        #     self.__salary = top_salary
        # else:
        #     self.__salary =
        self.__salary = max(value, top_salary)


person = Person("John", "Doe", 33, "123456AB", 120_000.1)
print(person)
print(person.first_name)
# print(person.__identity)
# person.hobbies = ["reading", "writing"]
# print(person.hobbies)
person.log_identity()
print(person.salary)
