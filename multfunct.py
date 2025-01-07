def multiply(num,count):
    return num*count
n = int(input("enter a number:"))
i = 1
for i in range(1,11):
    print(n,"*",i,"=",multiply(n,i))
    i = i+1

