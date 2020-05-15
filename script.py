import matplotlib
import matplotlib.pyplot as plt
import math

matplotlib.use('Agg')

xAxis = list(range(0,60))


xAxis = list(range(-20,20))


def parabola(xValues):
  yValues = []
  for x in xValues:
    y = x*x
    yValues.append(y)
  return yValues

yAxis = parabola(xAxis)


yAxis = parabola(xAxis)

sliceXAxis  = xAxis[:]
sliceYAxis  = yAxis[:]

style = 'ro'

plt.plot(sliceXAxis , sliceYAxis , style)

plt.axis([-10, 10, 0, 100])

filename = 'graph.png'
plt.savefig(filename)