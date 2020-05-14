import matplotlib
import matplotlib.pyplot as plt
import math

matplotlib.use('Agg')

xAxis = list(range(0,60))


def parabola(xValues):
  yValues = []
  for x in xValues:
    y = math.sin(x)
    yValues.append(y)
  return yValues


yAxis = parabola(xAxis)

sliceXAxis  = xAxis[:]
sliceYAxis  = yAxis[:]

style = 'ro'

plt.plot(sliceXAxis , sliceYAxis , style)

plt.axis([0, 100, -1, 1])

filename = 'graph.png'
plt.savefig(filename)