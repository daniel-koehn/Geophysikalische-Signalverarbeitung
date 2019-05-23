# Import Libraries 
# ----------------
import numpy as np
import matplotlib.pyplot as plt

def create_gauss_1st_derv(T,t0):
	
	dt = T / 1000               # sampling interval is 1/1000 of the period	
	time = np.arange(0,T,dt)    # define time vector
	a = 1                       # half-width
	
	# Define gaussian function          
	gauss = (1./np.sqrt(2*np.pi*a))*np.exp(-(((time-t0)**2)/(2*a)))
	
	return time, gauss

def create_sine(f0):
	
	w = 2 * np.pi * f0              # circular frequency
	T = 1 / f0                      # period
	tmax = f0 * T                   # define maximum time as 5 * period
	dt = T / 1000                   # sampling interval is 1/1000 of the period
	nt = (int) (tmax/dt)            # number of time samples 
	time = np.arange(0,nt*dt,dt)    # define time vector
	sine = np.sin(w*time)           # calculate sine function
	
	return time, sine
	
def draw_func(time,f,title,xlabel,ylabel):
	
	# plot time series
	plt.plot(time, f, 'b-',lw=3) 
	plt.title(title)
	plt.xlabel(xlabel)
	plt.ylabel(ylabel)
	plt.grid()
	#plt.show()
	
def draw_corr(time,f,f1,title,xlabel,ylabel,rho):
	
	# plot time series
	plt.plot(time, f1, 'r-',lw=3)
	plt.plot(time, f, 'b--',lw=3)	
	title1 = title + ' = ' + str(rho[0])
	plt.title(title1)
	plt.xlabel(xlabel)
	plt.ylabel(ylabel)	
	plt.grid()
	