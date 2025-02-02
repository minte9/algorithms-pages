# Find the 3th digit in the number 1024

input = 1024
n = input // 10 % 100
assert n == 2
print(n)


# Find the 2th digit in the number 23456

input = 23456
n = input // 1000 % 10
assert n == 3
print(n)


# Find the 2th digint in the number 1234 using a list, an O(n) algorithm

input = 1234

digits = []
for n in str(input):
    digits.append(n)

reversed = digits[::-1]
result = reversed[2]
result = int(result)

assert result == 2
print(result)
