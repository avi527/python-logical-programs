#even number show using generater
def even(n):
    for num in range(1,n+1):
        yield (num)
number=even(10)
for evennum in number:
    if (evennum%2==0):
        print(evennum)





