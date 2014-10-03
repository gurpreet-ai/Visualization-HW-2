from matplotlib import pyplot as plt
from scipy.io import loadmat
import matplotlib as mpl
import numpy as np
import pandas as pd
from pandas import DataFrame, Series
from datetime import datetime
import calendar

def k2f(t):
    return (t*9/5.0) - 459.67

def read_data(city):
	data = loadmat(city)
	kelvin = data['temperature']
	kelvin = [ j for i in kelvin for j in i]
	x = [k2f(i) for i in kelvin]
	return x, x[0:20000], x[len(x)-20000:]

def set_Spines(x):
	x.spines['top'].set_visible(False)
	x.spines['bottom'].set_linewidth(.8)
	x.xaxis.set_ticks_position('bottom')

	x.spines['right'].set_visible(False)
	x.spines['left'].set_linewidth(0.8)
	x.yaxis.set_ticks_position('left')

def main():

	joh_farh, joh_ist20, joh_lst20  	 = read_data('Johannesburg.mat')
	paris_farh, paris_ist20, paris_lst20 = read_data('Paris.mat')
	SP_farh, SP_ist20, SP_lst20 	   	 = read_data('SaoPaulo.mat')
	Sing_farh, Sing_ist20, Sing_lst20 	 = read_data('Singapore.mat')
	Syd_farh, Syd_ist20, Syd_lst20 	 	 = read_data('Sydney.mat')
	Van_farh, Van_ist20, Van_lst20 		 = read_data('Vancouver.mat')

	frame = DataFrame(joh_farh)

	years = [str(n) for n in range(1948, 2008)]
	months = [m for m in calendar.month_abbr[1:]]

	print months

	Winter = [i for i in months if i == 'Dec' or 'Jan' or 'Feb']
	Spring = [i for i in months if i == 'Mar' or 'Apr' or 'May']
	Summer = [i for i in months if i == 'Jun' or 'Jul' or 'Aug']
	Fall =   [i for i in months if i == 'Sep' or 'Oct' or 'Nov']

	

if __name__ == '__main__':
	main()