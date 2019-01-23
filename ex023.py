sum = 0

for i in range(0, 6):
    num = int(input("Enter a number: "))
    if num % 2 != 0:
        soma += num
print("The sum of the odd numbers entered was {}".format(sum))
