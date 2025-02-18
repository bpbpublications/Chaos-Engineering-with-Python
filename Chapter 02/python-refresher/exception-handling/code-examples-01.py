# zero-division error
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

# file not found
try:
    f = open("file.txt", "r")
# code to read the file
except FileNotFoundError:
    print("File not found!")
finally:
        f.close()
