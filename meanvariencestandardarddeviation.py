import numpy
n ,m = map(int, input().split())
l = numpy.array([input().split() for i in range(n)], int)
print(numpy.mean(l, axis = 1))
print(numpy.var(l, axis =0 ))
print(round(numpy.std(l),11))