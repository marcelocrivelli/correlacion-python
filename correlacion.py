# imports
from numpy import mean
from numpy import std
from numpy.random import randn
from numpy.random import seed
from matplotlib import pyplot


# seed random number generator
seed(1)

# data preparation, two correlated variables

# Gaussian distribution (mean= 50, standar dev = 15) 
data1 = 15 * randn(1000) + 50
# Gaussian distribution (mean= 25, standar dev = 5)
data2 = data1 + (5 * randn(1000) + 25)

# summarize
print('data1: mean=%.3f stdv=%.3f' % (mean(data1), std(data1)))
print('data2: mean=%.3f stdv=%.3f' % (mean(data2), std(data2)))


# plot
pyplot.scatter(data1, data2)
pyplot.show()