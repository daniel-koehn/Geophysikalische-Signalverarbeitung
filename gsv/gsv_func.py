# Import Libraries 
# ----------------
import numpy as np
import matplotlib.pyplot as plt

def create_gauss_1st_derv(T,f0):
	
	p = 1./ f0                  # period [s]	
	dt = T / 10000              # sampling interval is 1/10000 of the recording time
	t0 = p                      # time-shift [s]
	time = np.arange(0,T,dt)    # define time vector
	sigma = 4./p                # half-width
	
	# Define gaussian function          
	gauss_1st = -2 * sigma * (time-t0) * np.exp(-(sigma * (time-t0))**2)
	
	return time, gauss_1st
	
def create_gauss_1st_derv_timeseries(T,f0):
	
	p = 1./ f0                  # period [s]	
	dt = T / 10000              # sampling interval is 1/10000 of the recording time
	t0 = 4*p                    # time-shift [s]
	t1 = 8*p 
	t2 = 12*p
	time = np.arange(0,T,dt)    # define time vector
	sigma = 4./p                # half-width
	
	# Define gaussian functions          
	gauss_1 = -2 * sigma * (time-t0) * np.exp(-(sigma * (time-t0))**2)
	gauss_2 = 1 * sigma * (time-t1) * np.exp(-(sigma * (time-t1))**2)
	gauss_3 = -0.5 * sigma * (time-t2) * np.exp(-(sigma * (time-t2))**2)
	
	# Compute final time series
	gauss_final = gauss_1 + gauss_2 + gauss_3
	
	return time, gauss_final	
	
def create_gauss(ts,hw,a):
	
	T = 4.                      # recording time of time series
	dt = T / 4000               # sampling interval is 1/4000 of tmax	
	time = np.arange(0,T,dt)    # define time vector
	
	# Define gaussian function          
	gauss = a * np.exp(-(time-ts)**2/(2*hw**2))
	
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
	
def create_sine_int(f0,T):
	
	w = 2 * np.pi * f0              # circular frequency
	tmax = 4.                       # set maximum time to 4 s
	dt = tmax / 4000                # sampling interval is 1/4000 of tmax
	nt = (int) (tmax/dt)            # number of time samples 
	time = np.arange(0,nt*dt,dt)    # define time vector
	sine = np.sin(w*time)           # calculate sine function
	
	# set sine function outside [0,T] to zero
	ntmax = (int)(T/dt)
	sine[ntmax:-1] = 0.0
	
	return time, sine

def create_sweep(f1,f2,T):
	
	w1 = 2 * np.pi * f1             # circular frequency w1
	w2 = 2 * np.pi * f2             # circular frequency w2
	tmax = 10.                       # set maximum time to 2 s
	dt = tmax / 8000                # sampling interval is 1/8000 of tmax
	nt = (int) (tmax/dt)            # number of time samples 
	time = np.arange(0,nt*dt,dt)    # define time vector
	
	# define sweep
	k = w1 + ((w2-w1) * time / T)
	sweep = np.sin(k * time)        # calculate sine function
		
	return time, sweep
	
def create_rectf(T):

	tmax = 4 * T                           # define maximum recording time as 4 * temporal length of rectangle
	dt = T/1000						       # sampling interval is 1/1000 of temporal length of rectangle
	time = np.arange(0,tmax,dt)            # define time vector
	rect = np.zeros(len(time))		       # initialize rectangular function
	
	nth_rect = (int)((T/dt)/2)             # half length of rectangular function [gridpoints]
	nth = (int)((tmax/dt)/2) 			   # half length of time series [gridpoints]   
	rect[nth-nth_rect:nth+nth_rect] = 1.0  # add rectangle to rectangular function
	
	return time, rect
	
def create_delta(ts,amp):

	tmax = 4                               # define maximum recording time tmax = 4 s
	dt = tmax/4000						   # sampling interval is 1/4000 of temporal length of time series
	time = np.arange(0,tmax,dt)            # define time vector	
	nth = (int)(ts/dt) 			           # time-shift of delta function [gridpoints]  
	
	delta = np.zeros(len(time))            # initialize delta function
	delta[nth] = amp                       # add delta-function
	
	return time, delta	
	
def create_white_noise(mean,std):

	tmax = 4.                                          # define maximum recording time tmax = 4 s
	dt = tmax/4000						               # sampling interval is 1/4000 of temporal length of time series
	time = np.arange(0,tmax,dt)                        # define time vector
	nt = len(time)	                                   # number of time samples 
	white_noise = np.random.normal(mean, std, size=nt) # create white noise

	return time, white_noise	
	
def draw_func(time,f,title,xlabel,ylabel):
	
	# plot time series
	plt.plot(time, f, 'b-',lw=3) 
	plt.title(title)
	plt.xlabel(xlabel)
	plt.ylabel(ylabel)
	plt.grid()
	#plt.show()
	
def draw_func1(time,f,title,xlabel,ylabel):
	
	# plot time series
	plt.plot(time, f, 'b-') 
	plt.title(title)
	plt.xlabel(xlabel)
	plt.ylabel(ylabel)
	plt.grid()
	#plt.show()	
	
def draw_func2(time,f,f1,title,xlabel,ylabel):
	
	# plot time series
	plt.plot(time, f1/np.amax(f1), 'r-',lw=5,label='Spike-Response')
	plt.plot(time, f/np.amax(f), 'b-',label='KKF(vibro,sweep)')  
	plt.title(title)
	plt.xlabel(xlabel)
	plt.ylabel(ylabel)
	plt.grid()
	plt.legend()
	#plt.show()		
	
def comp_AKF_rect(lags,AKF,T,title,xlabel,ylabel):
	
	# Analytical AKF T - abs(lags)
	AKF_an = T - np.abs(lags) 
	
	# Set analytical AKF outside lags [-T,T] to zero
	nth = (int)(len(lags)/2)
	dt = lags[-1] - lags[-2]
	nT = (int)(T/dt)
	AKF_an[0:nth-nT] = 0.0
	AKF_an[nth+nT:-1] = 0.0
	AKF_an[-1] = 0.0
	
	# plot AKF
	plt.plot(lags, AKF, 'b-',lw=3,label='numerisch')
	plt.plot(lags, AKF_an, 'r--',lw=3,label='analytisch')	
	plt.title(title)
	plt.xlabel(xlabel)
	plt.ylabel(ylabel)	
	plt.legend()
	plt.grid()	
	
def comp_AKF_delta(lags,AKF,amp,title,xlabel,ylabel):
	
	# Analytical AKF 
	AKF_an = np.zeros(len(lags))
	nth = (int)(len(lags)/2)
	AKF_an[nth] = amp
	
	# plot AKF
	plt.plot(lags, AKF, 'b-',lw=3,label='numerisch')
	plt.plot(lags, AKF_an, 'r--',lw=3,label='analytisch')	
	plt.title(title)
	plt.xlabel(xlabel)
	plt.ylabel(ylabel)	
	plt.legend()
	plt.grid()

def comp_AKF_delta_sum(lags,AKF,ts2,a,b,title,xlabel,ylabel):
	
	# Analytical AKF 
	AKF_an = np.zeros(len(lags))
	nth = (int)(len(lags)/2)
	dt = lags[-1] - lags[-2]
	nshift = (int)(ts2/dt)
	AKF_an[nth] = (a**2 + b**2)  # zero lag delta function
	AKF_an[nth+nshift] = (a*b)   # positive lag delta function
	AKF_an[nth-nshift] = (a*b)   # negative lag delta function
	
	# plot AKF
	plt.plot(lags, AKF, 'b-',lw=3,label='numerisch')
	plt.plot(lags, AKF_an, 'r--',lw=3,label='analytisch')	
	plt.title(title)
	plt.xlabel(xlabel)
	plt.ylabel(ylabel)	
	plt.legend()
	plt.grid()

def comp_AKF_gauss(lags,AKF,a,T,title,xlabel,ylabel):
	
	# Analytical AKF 
	AKF_an = a**2 * T * np.sqrt(np.pi) * np.exp(-lags**2 / (4 * T**2))
	
	# plot AKF
	plt.plot(lags, AKF, 'b-',lw=3,label='numerisch')
	plt.plot(lags, AKF_an, 'r--',lw=3,label='analytisch')	
	plt.title(title)
	plt.xlabel(xlabel)
	plt.ylabel(ylabel)	
	plt.legend()
	plt.grid()

def comp_AKF_sine(lags,AKF,f0,T,title,xlabel,ylabel):
	
	# Analytical AKF
	w0 = 2. * np.pi * f0    # circular frequency
	AKF_an = 0.5 * (1-(np.abs(lags)/T))*np.cos(w0*lags)
	
	# set AKF for lags > abs(T) to zero
	nth = (int)(len(lags)/2)
	dt = lags[-1] - lags[-2]
	nT = (int)(T/dt)
	AKF_an[0:nth-nT] = 0.0
	AKF_an[nth+nT:-1] = 0.0
	AKF_an[-1] = 0.0
	
	# plot AKF
	plt.plot(lags, AKF, 'b-',lw=3,label='numerisch')
	plt.plot(lags, AKF_an, 'r--',lw=3,label='analytisch')	
	plt.title(title)
	plt.xlabel(xlabel)
	plt.ylabel(ylabel)	
	plt.legend()
	plt.grid()	
	
def comp_AKF_sine_1(lags,AKF,f0,T,title,xlabel,ylabel):
	
	# Analytical AKF
	w0 = 2. * np.pi * f0    # circular frequency
	AKF_an = 0.5 * T * (1-(np.abs(lags)/T))*np.cos(w0*lags) / (T - np.abs(lags))
	
	# set AKF for lags > abs(T) to zero
	nth = (int)(len(lags)/2)
	dt = lags[-1] - lags[-2]
	nT = (int)(T/dt)
	
	AKF_an[0:nth-nT] = 0.0
	AKF_an[nth+nT:-1] = 0.0
	AKF_an[-1] = 0.0
	
	AKF[0:nth-nT] = 0.0
	AKF[nth+nT:-1] = 0.0
	AKF[-1] = 0.0
	
	# plot AKF
	plt.plot(lags, AKF, 'b-',lw=3,label='numerisch')
	plt.plot(lags, AKF_an, 'r--',lw=3,label='analytisch')	
	plt.title(title)
	plt.xlabel(xlabel)
	plt.ylabel(ylabel)	
	plt.legend()
	plt.grid()

def comp_AKF_sweep(lags,AKF,f1,f2,T,title,xlabel,ylabel):
	
	# Analytical AKF 
	k = np.pi * (f2 - f1) * lags 
	k1 = np.pi * (f2 + f1) * lags
	AKF_an = (np.sin(k) / k) * np.cos(k1)
	
	# plot AKF
	plt.plot(lags, AKF, 'b-',lw=3,label='numerisch')
	plt.plot(lags, AKF_an, 'r-',lw=2,label='analytisch')	
	plt.title(title)
	plt.xlabel(xlabel)
	plt.ylabel(ylabel)	
	plt.legend()
	plt.grid()	

def comp_AKF_sweep1(lags,AKF,AKF1,title,xlabel,ylabel):
	
	# plot AKF
	plt.plot(lags, AKF, 'b-',lw=1,label='Sweep [f1 = 10 Hz, f2 = 100 Hz]')
	plt.plot(lags, AKF1, 'r-',lw=1,label='Sweep [f1 = 10 Hz, f2 = 40 Hz]')	
	plt.title(title)
	plt.xlabel(xlabel)
	plt.ylabel(ylabel)	
	plt.legend()
	plt.grid()		
	
def comp_AKF_wnoise(lags,AKF,std,title,xlabel,ylabel):
	
	# Analytical AKF
	AKF_an = np.zeros(len(lags))	
	nth = (int)(len(lags)/2)
	AKF_an[nth] = (2*std)**2
	
	# plot AKF
	plt.plot(lags, AKF, 'b-',lw=3,label='numerisch')
	plt.plot(lags, AKF_an, 'r--',lw=3,label='analytisch')	
	plt.title(title)
	plt.xlabel(xlabel)
	plt.ylabel(ylabel)	
	plt.legend()
	plt.grid()		
	
def draw_corr(time,f,f1,title,xlabel,ylabel,rho):
	
	# plot time series
	plt.plot(time, f1, 'r-',lw=3)
	plt.plot(time, f, 'b--',lw=3)	
	title1 = title + ' = ' + str(rho[0])
	plt.title(title1)
	plt.xlabel(xlabel)
	plt.ylabel(ylabel)	
	plt.grid()	

def plot_spec(time,signal,fmax,title,xlabel,ylabel):
	
	spec = np.fft.fft(signal)   # fft of signal
	dt = time[1] - time[0]
	freq = np.fft.fftfreq(spec.size, d = dt) # frequency axis
	
	# plot time series
	plt.plot(np.abs(freq), np.abs(spec), 'r-',lw=3)	
	plt.title(title)
	plt.xlabel(xlabel)
	plt.ylabel(ylabel)	
	plt.xlim(0,fmax)
	plt.grid()
	
def create_spike_3_layers(time):	
	
	t_r1 = 0.3325 # traveltime of 1st reflection
	t_r2 = 0.7325 # traveltime of 2nd reflection
	
	t_rr1 = 0.665 # multiple of 1st reflection
	t_rr2 = 1.465 # multiple of 2nd reflection
	
	# corresponding amplitudes of Greens function
	a_r1 = 8.772e-5
	a_r2 = 0.0001425
	a_rr1 = -1.649e-6
	a_rr2 = -1.015e-5
	
	dt = time[1] - time[0] # define dt
	nt = (int)(len(time))  # number of time samples
	green = np.zeros(nt)   # initialize Greens function
	
	# calculate Greens function
	green[(int)(t_r1/dt)] = a_r1 
	green[(int)(t_r2/dt)] = a_r2
	green[(int)(t_rr1/dt)] = a_rr1
	green[(int)(t_rr2/dt)] = a_rr2
	
	return green
	
