from matplotlib.colors import ListedColormap
import numpy as np
import matplotlib.pyplot as plt
class plots:
	def __init__(self):
		self.name="Triangular plot"
	def triangularPlot(self,lower,upper,cycles,steps_per_cycle):
		x=np.arange(0,steps_per_cycle*cycles+steps_per_cycle,1)
		y=np.zeros_like(x)
		y1=[]
		for j in range(2*cycles+1):
			if(j%2==0):
				y1.append(lower)
			else:
				y1.append(upper)
		y1=np.array(y1)
		x1=[]
		n=0
		for j in range(2*cycles+1):
			x1.append(n)
			n+=(steps_per_cycle/2)
		x1=np.array(x1)
		plt.plot(x,y+lower,'--g')
		plt.plot(x,y+upper,'--g')
		plt.plot(x1,y1,'-r')
		plt.show()
		