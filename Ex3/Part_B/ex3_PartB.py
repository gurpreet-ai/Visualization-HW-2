from matplotlib import pyplot as plt
from scipy.io import loadmat
import matplotlib as mpl
import numpy as np
import pandas as pd
from pandas import DataFrame, Series

def data_format(series):
	time = series['time']
	temp = series['temperature']

	time_temp = zip(time, temp)
	win = ['12', '01', '02']
	spr = ['03', '04', '05']
	sumer = ['06', '07', '08']
	fal   = ['09', '10', '11']

	year = {}
	
	for k, v in enumerate(range(1948, 2009)):
		q = []
		winter = []
		spring = []
		summer = []
		fall = []
		season = {}
		for i, j in time_temp:
			if i[0:4] == str(v):
				if i[5:7] in win:
					j[0] = k2f(j[0])
					winter.append(j[0])
				elif i[5:7] in spr:
					j[0] = k2f(j[0])
					spring.append(j[0])
				elif i[5:7] in sumer:
					j[0] = k2f(j[0])
					summer.append(j[0])
				elif i[5:7] in fal:
					j[0] = k2f(j[0])
					fall.append(j[0])

		season['winter'] = round(np.average(winter), 2)
		season['spring'] = round(np.average(spring), 2)
		season['summer'] = round(np.average(summer), 2)
		season['fall']   = round(np.average(fall), 2)
		
		year[v] = season

	return year

def k2f(t):
    return (t*9/5.0) - 459.67

def set_Spines(x):
	x.spines['top'].set_visible(False)
	x.spines['bottom'].set_linewidth(.8)
	x.xaxis.set_ticks_position('bottom')

	x.spines['right'].set_visible(False)
	x.spines['left'].set_linewidth(0.8)
	x.yaxis.set_ticks_position('left')

def main():
	data = loadmat('Johannesburg.mat')
	series = Series(data)
	Johannesburg = data_format(series)
	print "Johannesburg"
	sorted(Johannesburg.keys())
	"""
	data = loadmat('Paris.mat')
	series = Series(data)
	Paris = data_format(series)
	print "\nParis"
	sorted(Paris.keys())

	data = loadmat('SaoPaulo.mat')
	series = Series(data)
	SaoPaulo = data_format(series)
	print "\nSaoPaulo"
	sorted(SaoPaulo.keys())

	data = loadmat('Singapore.mat')
	series = Series(data)
	Singapore = data_format(series)
	print "\nSingapore"
	sorted(Singapore.keys())

	data = loadmat('Sydney.mat')
	series = Series(data)
	Sydney = data_format(series)
	print "\nSydney"
	sorted(Sydney.keys())

	data = loadmat('Vancouver.mat')
	series = Series(data)
	Vancouver = Vancouver(series)
	print "\nVancouver"
	sorted(Vancouver.keys())
	"""
	fig = plt.figure(figsize=(18,12))
	gs = mpl.gridspec.GridSpec(1,1)
	ax = fig.add_subplot(gs[0])
	plt.subplots_adjust(left=0.075, right=0.95, top=0.9, bottom=0.25)
	set_Spines(ax)

	x = Johannesburg.values()
	Joh_winter = []
	Joh_spring = []
	Joh_summer = []
	Joh_fall = []
	for i in x:
		Joh_winter.append(i['winter'])
		Joh_spring.append(i['spring'])
		Joh_summer.append(i['summer'])
		Joh_fall.append(i['fall'])

	N = len(Johannesburg.keys())
	ind = np.arange(N)
	width = 0.25
	rect1 = ax.bar(Johannesburg.keys(), Joh_winter, width, color='navy')
	_list = [i+.25 for i in Johannesburg.keys()]
	rect2 = ax.bar(_list, Joh_spring, width, color='tan', alpha=.4)
	_list = [i+.50 for i in Johannesburg.keys()]
	rect3 = ax.bar(_list, Joh_summer, width, color='Aqua', alpha=.4)
	_list = [i+.75 for i in Johannesburg.keys()]
	rect4 = ax.bar(_list, Joh_fall, width, color='bisque', alpha=.4)

	print Johannesburg.keys()
	ax.set_xticks(Johannesburg.keys())
	ax.set_xticklabels(Johannesburg.keys(), rotation=45, fontsize=9)
	ax.set_title('Johannesburg (Temperature 1948 - 1960)')
	ax.set_xlabel('Years')
	ax.set_ylabel('Temperature (Farh)')
	
	ax.set_xlim((1948,2008))
	ax.legend( (rect1[0], rect2[0], rect3[0], rect4[0]), ('Winter', 'Spring', 'Summer', 'Fall') )

	fig.savefig('fig.png')

	

if __name__ == '__main__':
	main()