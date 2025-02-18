# conditional statements
x = 10
if x > 5:
    print("x is greater than 5")

# for loops
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# while loops
i = 1
while i <= 5:
    print(i)
    i += 1

# break statement
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    if fruit == "banana":
        break
    print(fruit)

# continue
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    if fruit == "banana":
        continue
    print(fruit)

# pass
if x > 5:
    pass	# TODO: Write code here
else:
    print("x is less than or equal to 5")
