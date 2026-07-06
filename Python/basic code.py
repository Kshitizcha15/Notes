# slicing string code 
# [start:stop:set p]

b = "Hello, World!"
a = list(range(0,100,))
print(a) #adding the number in slicing
print(a[0:100:10])

# ................................................................................................

# leap year

year = int(input("Enter a year: "))
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
   print(year, "is a Leap Year")
else:
   print(year, "is not a Leap Year")

# ................................................................................................

dict = {
 "brand": "Ford",
 "model": "Mustang",
 "year": 1964
}
print(dict["brand"], dict["model"], dict["year"])

# ................................................................................................


