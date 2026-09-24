# comment line
# comment line
# comment line

# types:
# IMMUTABLE
# int (nincs értékkészlet, dinamikus méret),
# float (64 bit),
# complex (10+10j)
# bool
# str
# NoneType

# list  - indexed, mutable, can contains dupliceted member
numbers = [1, 2, 3, 4, 5, 1, 2, 3]
numbers[0] = 0
print(numbers[0])

print(type(numbers), numbers)
# tuple - immutable list
numbers = (1, 2, 3)
print(type(numbers), numbers)
print(numbers[0])
# TypeError: 'tuple' object does not support item assignment
# numbers[0] = 0
# set: mutable, unsorted, unindexed, contains uniq elements
x1 = {"a", "b", "c", "d"}
x2 = {"b", "c", "d", "e"}
print(type(x1), x1.union(x2))
duplicated = [1, 2, 3, 1, 1, 2, 3, 1]
unique_elements = list(set(duplicated))
print(unique_elements)
# dict
# key is an immutable type, indexed, not contains duplicated keys
admin_user = {
    "first_name": "John",
    "last_name": "Doe",
    "age": 33,
}
print(type(admin_user), admin_user)
