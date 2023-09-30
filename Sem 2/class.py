import numpy

arr = numpy.array([0, 1, 2, 0, numpy.nan, 5, numpy.nan])

zero = numpy.where(arr == 0)[0]
nonzero = numpy.where(arr != 0)[0]
nan = numpy.where(numpy.isnan(arr))[0]

print("Array", arr)
print("Indices of zero elements:", zero)
print("Indices of non-zero elements:", nonzero)
print("Indices of NaN elements:", nan)
