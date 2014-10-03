from matplotlib import pyplot as plt
from scipy.io import loadmat
import matplotlib as mpl
import numpy as np

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

	fig = plt.figure(figsize=(10,8))
	gs = mpl.gridspec.GridSpec(1,1)
	ax = fig.add_subplot(gs[0])
	plt.subplots_adjust(left=0.075, right=0.95, top=0.9, bottom=0.25)
	set_Spines(ax)

	cities = ['Johannesburg', 'Paris', 'SaoPaulo', 'Singapore', 'Sydney', 'Vancouver']
	xtickNames = plt.setp(ax, xticklabels=cities)
	plt.setp(xtickNames, rotation=45, fontsize=10)

	data = [joh_farh, paris_farh, SP_farh, Sing_farh, Syd_farh, Van_farh]
	ax.boxplot(data)
	ax.set_title('Temperature of cities in the World')
	ax.set_xlabel('Cities in the World')
	ax.set_ylabel('Temperature (Farh) ')
	ax.autoscale_view()
l
	fig.savefig('partA_fig1.png')

	fig2 = plt.figure(figsize=(10,8))
	gs1 = mpl.gridspec.GridSpec(1,2)

	bx = fig2.add_subplot(gs1[0])
	xtickNames = plt.setp(bx, xticklabels=cities)
	plt.setp(xtickNames, rotation=45, fontsize=10)
	plt.subplots_adjust(left=0.075, right=0.95, top=0.9, bottom=.1)
	bx.set_title('Temperature of cities in the World')
	bx.set_xlabel('Cities in the World')
	bx.set_ylabel('Temperature (Farh) (First 20000)')
	set_Spines(bx)
	
	data_ist20 = [joh_ist20, paris_ist20, SP_ist20, Sing_ist20, Syd_ist20, Van_ist20]
	bx.boxplot(data_ist20)

	cx = fig2.add_subplot(gs1[1])
	xtickNames = plt.setp(cx, xticklabels=cities)
	plt.setp(xtickNames, rotation=45, fontsize=10)
	plt.subplots_adjust(left=0.075, right=0.95, top=0.9, bottom=0.25)
	data_lst20 = [joh_lst20, paris_lst20, SP_lst20, Sing_lst20, Syd_lst20, Van_lst20]
	cx.set_title('Temperature of cities in the World')
	cx.set_xlabel('Cities in the World')
	cx.set_ylabel('Temperature (Farh) (Last 20000)')
	set_Spines(cx)
	
	cx.boxplot(data_lst20)
	fig2.savefig('partA_fig2.png')

if __name__ == '__main__':
    main()