# 1st problem : calculator usinig functions.

def calculator(a, b, z):
    if z == "+":
        return a + b
    elif z == "-":
        return a - b
    elif z == "*":
        return a * b
    elif z == "/":
        return a / b
    elif z == "^":
        return a**b

n1 = float(input("Enter first number: "))
z = input("Enter operator: ")
n2 = float(input("Enter second number: "))

print("Result =", calculator(n1, n2, z))

# 2nd problem : save the output in list and a disctionary for the future use 

#list
out_list=[]

output = calculator(n1, n2, z)
out_list.append(output)

print("List =", out_list)

#dict
out_dict=[]








