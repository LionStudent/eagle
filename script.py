  
import matplotlib

import matplotlib.pyplot as plt
import math

matplotlib.use('Agg')
xAxis = list(range(0,64))
xTenth = []

for x in xAxis:

  xTenth.append(x*0.1)

xAxis = xTenth

def parabola(xValues):

  yValues = []

  for x in xValues:

    #y = x*x
    y=math.sin(x)
    yValues.append(y)

  return yValues


yAxis = parabola(xAxis)
sliceXAxis  = xAxis[:]

sliceYAxis  = yAxis[:]
style = 'b-'

plt.plot(sliceXAxis , sliceYAxis , style)

plt.axis([0, 6.4, -1, 1])

filename = 'graph.png'

plt.savefig(filename)