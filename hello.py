print("Hello, World!")

s = input("s:")
t = input("t:")

if s == t:
   print("Same")
else:
     print("Different")


before = input("Before: ")
after = before.upper()

print(f"After: {after}")

def main():
   meow(3)

def meow(n):
    for i in range(n): 
      print("meow")

main()    


scores = [73, 73, 74]

avarage = sum(scores) / len(scores)

print(f"Avarage {avarage}")



from sys import argv

if len(argv) == 2:
    print(f"hello, {argv[1]}")
else:
    print("hello, world")



import csv


name = input("Name: ")
number = input("Number: ")

with open("phonebook.csv", "a") as file:

  writer = csv.writer(file)
writer.writerow([name, number])

## Second option

name = input("Name: ")
number = input("Number: ")

with open("phonebook.csv", "a") as file:

    writer = csv.DictWriter(file, fieldnames=["name", "number"])
    writer.writerow({"name": name, "number": number})


