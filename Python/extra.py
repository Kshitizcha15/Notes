# This program takes a list of numbers and reduces each number to a single digit by repeatedly summing its digits until only one digit remains.
# The final single-digit results are stored in the 'result' list and printed.

var = [111, 501, 100, 515, 424, 899, 991, 605, 103, 1104]

result = []

for num in var:
    temp = num

    while temp >= 10:
        total = 0

        while temp > 0:
            total += temp % 10
            temp //= 10

        temp = total

    result.append(temp)

print(result)

'''
var = [111, 501, 100, 515, 424, 899, 991, 605, 103, 1104]
output_var = []
for i in var:
    count = 0
    for j in str(i):
        count += int(j)
        if count > 10:
            for a in str(count):
                count = 0
                count += int(a)
    output_var.append(count)

print(output_var)
'''

# make a list from user input

var = []
data = input("Enter a list: ")
i = 0
for i in data.split(","):
    var.append(int(i))
print(var)

# data = list(map(int, input("Enter numbers : ").split(",")))
# print(data)


# Draw a pattern 

for i in range(5):
    for j in range(5):

        if (i == j or j == 4 - i):
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()

