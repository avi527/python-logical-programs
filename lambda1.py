# Anonymous function means that a function is without a name.as we already know
# that def keywords is used to define the normal function and the lambda keywords is used to create anonymous functions.it
# it has the following syntex:
# syntext : lambda arrgument:expresion

#lambda example 1
g=lambda x:x*x*x
print(g(7))

#lambda example 2
add=lambda a,b:a+b
print(add(2,3))

#lambda example 3
evens=lambda x,y:x*y
print(evens(6,2))

#map function in lambda
li=[2,76,65,45,4,3,9,8,6,7]
sq=list(map(lambda x:x*5,li))
print(sq)

#map function example2
tu=(2,76,65,45,4,3,9,8,6,7)
sqts=tuple(map(lambda x:x*2,tu))
print(sqts)


