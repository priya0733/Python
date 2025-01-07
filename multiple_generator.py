#create a generator which returns squares of the number as well as fabonicee series

def Fibonacci(nums):
    x,y = 0, 1
    for _ in range(nums):
        x, y = y, x+y
        yield x

def Square(nums):
    for num in nums:
        yield num**2
        
print(sum(Square(Fibonacci(10))))
