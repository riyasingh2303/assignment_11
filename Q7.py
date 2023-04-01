num = int(input("Enter any number : "))
temp = num
count = 0
for i in str(temp):
    temp = temp // 10
    count += 1
print(count)