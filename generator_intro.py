#create your first generator function
#yield is a keyword for create generator function
def num(n):
    for i in range(1,n+1):
        yield (i)
number=num(10)
for numb in number:
    print(numb)


