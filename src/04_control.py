from numpy import number


salary = 100_000
high_salary_threshold = 120_000

if salary >= high_salary_threshold:
    print("High salary")
else:
    print("Low salary")

grade = "hi"

if grade == 5:
    print("Jeles")
elif grade == 4:
    print("Jó")
elif grade == 3:
    print("Közepes")
elif grade == 2:
    print("ELégséges")
elif grade == 1:
    print("Elégtelen")
else:
    print("EZ nem érdemjegy")

grades = {
    1: "Elégtelen",
    2: "Elégséges",
    3: "Közepes",
    4: "Jó",
    5: "Elégséges",
}

# print(grades[grade])
print(grades.get(grade))

numbers = [1, 2, 3, 4, 5]
for i in numbers:
    print(i)

for i, v in enumerate(numbers):
    print(f"index: {i}, value: {v}")

user = {"first_name": "John", "last_name": "Doe"}
for i in user:
    print(i)

for i in user.values():
    print(i)
