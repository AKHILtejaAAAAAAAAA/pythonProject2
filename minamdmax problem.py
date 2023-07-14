import numpy
my_array = numpy.array([[2, 5],
                        [3, 7],
                        [1, 3],
                        [4, 0]])
print numpy.max(my_array, axis = 0)
print numpy.max(my_array, axis = 1)
print numpy.max(my_array, axis = None)
print numpy.max(my_array)