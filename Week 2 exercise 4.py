"""Week 2 exercise 4"""

try:
  age = int(input("What is your age: "))
  
except ValueError:
        print("Invalid input!")

if age < 13:
    print("U are a child")
elif age > 18 & age < 21:
    print("U are a young adult")
elif age > 21:
    print("U are an adult")
elif age >= 13 & age < 20:
    print("U are a teenager")