# open file in write mode
with open("file.txt", "w") as file:
    file.write("Hello, World!")

# open a file in append mode
with open("file.txt", "a") as file:
    file.write("Hello, World!")

# open file in read mode
with open("file.txt", "r") as file:
    contents = file.read()
    print(contents)
