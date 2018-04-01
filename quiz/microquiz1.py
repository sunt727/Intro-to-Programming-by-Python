# x = 3.14159
#
# sum  = 0
#
# for i in str(x):
#      if i in ("13579"):
#          sum += int(i)
#
# print(sum)



# x = 14
#
# sum = 0
#
# for num in range(2, x + 1):
#     if all(num % i != 0 for i in range(2, num)):
#         sum += num
# print(sum)

x = 14

sum = 0

for num in range(2, x):
    if all(num % i != 0 for i in range(2, num)):
        sum += num
print(sum)