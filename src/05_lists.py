from numpy import number


numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(numbers[0])

# slicing:

print(numbers[:3])  # to the 3. (exclude)
print(numbers[3:])  # from the 3. element
print(numbers[2:5])  # from 2 to 5 (exclude)
print(numbers[2:6:2])  # from 2 to 6. every 2
print(numbers[::3])  # every 3.
print(numbers[::-1])  # reverse

numbers_copy = numbers
print("id numbers", id(numbers))
print("id, numbers copy", id(numbers_copy))
numbers.append(0)
print(numbers)
print(numbers_copy)

numbers_shallow_copy = numbers[:]
print(id(numbers))
print(id(numbers_shallow_copy))

# comprehension

net_prices = [100, 1000, 2500, 6000]
vat_multiplier = 1.27

# gross_prices = []
# for i in net_prices:
#     gross_prices.append(i * vat_multiplier)


gross_prices = [i * vat_multiplier for i in net_prices]

print(gross_prices)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

even = []
for i in numbers:
    if i % 2 == 0:
        even.append(i)


even = [i for i in numbers if i % 2 == 0]
odd = [i for i in numbers if i % 2 != 0]
