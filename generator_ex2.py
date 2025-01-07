# create the generator object

#squares_generator = (i * i for i in range(5))

# iterate over the generator and print the values

#for i in squares_generator:
    #print(i)


#generator for power of the number

def PowTwoGen(max=0):
    n = 0
    while n < max:
        yield 2**n
        n += 1

for value in PowTwoGen(9):
    print(value)
        