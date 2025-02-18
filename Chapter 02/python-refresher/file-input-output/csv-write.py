import csv

with open("file.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age"])
    writer.writerow(["John", 30])
    writer.writerow(["Jane", 25])
