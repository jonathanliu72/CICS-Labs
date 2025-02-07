nums = int(input("How many numbers do you want to enter: "))
lis = []
lis2 = []


for i in range(0, nums):
    input1 = int(input("Enter number: "))
    lis.append(input1)

for i in lis[::-1]:
    lis2.append(i)

print(lis2)
