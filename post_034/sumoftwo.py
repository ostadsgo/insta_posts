"""sdf"""

number = -32
number = abs(number)
digit_sum = 0

while number > 0:
    digit = number % 10
    digit_sum += digit
    number //= 10

print(digit_sum)


# number = -32
# digits = str(abs(number))
# digit_sum = sum(int(digit) for digit in digits)
# print(digit_sum)

for i in range(1, 10):
    if x % 2 == 0:
        print(x)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        return f"{self.name} : {self.age}"
