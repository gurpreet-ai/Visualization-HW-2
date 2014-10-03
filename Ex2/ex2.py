from matplotlib import pyplot as plt
from scipy.io import loadmat
import matplotlib as mpl
import numpy as np
from scipy.stats.stats import pearsonr


def main():
	data = loadmat('AQUA.2013089.2055.mat')
	
	spercentage = 0.0045

	# B1
	b1_N = data['B1'].shape
	b1_pixels = b1_N[0] * b1_N[1]		# ? 609638
	b1_numSamps = round(b1_pixels * spercentage)
	
	b1_samplesInds = range(1, b1_pixels)
	np.random.shuffle(b1_samplesInds)
	b1_samplesInds = b1_samplesInds[0:int(b1_numSamps)]

	b1 = data['B1']
	b_1 = b1.ravel()[b1_samplesInds]

	# B6
	b6_N = data['B6'].shape
	b6_pixels = b6_N[0] * b6_N[1]		# ? 609638
	b6_numSamps = round(b6_pixels * spercentage)
	
	b6_samplesInds = range(1, b6_pixels)
	np.random.shuffle(b6_samplesInds)
	b6_samplesInds = b6_samplesInds[0:int(b6_numSamps)]

	b6 = data['B6']
	b_6 = b6.ravel()[b6_samplesInds]

	#b7
	b7_N = data['B7'].shape
	b7_pixels = b7_N[0] * b7_N[1]		# ? 609638
	b7_numSamps = round(b7_pixels * spercentage)
	
	b7_samplesInds = range(1, b7_pixels)
	np.random.shuffle(b7_samplesInds)
	b7_samplesInds = b7_samplesInds[0:int(b7_numSamps)]

	b7 = data['B7']
	b_7 = b7.ravel()[b7_samplesInds]

	fig = plt.figure(figsize=(10,8))
	gs = mpl.gridspec.GridSpec(1,1)
	ax = fig.add_subplot(gs[0])

	ax.spines['top'].set_visible(False)
	ax.spines['bottom'].set_linewidth(.8)
	ax.xaxis.set_ticks_position('bottom')

	ax.spines['right'].set_visible(False)
	ax.spines['left'].set_linewidth(0.8)
	ax.yaxis.set_ticks_position('left')

	#set tick properties
	ax.xaxis.set_tick_params('major', length=2, labelsize=10)
	ax.yaxis.set_tick_params('major', length=2, labelsize=10)

	a, b, c = np.polyfit(b_1, b_6, 2)
	z = np.polyfit(b_1, b_6, 2)
	p = np.poly1d(z)
	slope, y_inter = np.polyder(p)

	#plot data and customize look of plot
	ax.plot(b_1, b_6, marker='.', color='k', linestyle='',
	        markersize=4, clip_on=False, alpha=0.7)

	ax.plot(b_1, p(b_1), marker='*', color='red', linestyle='-',
        markersize=4, clip_on=False, label='Linear regression line')

	#set axis limits 
	#ax.set_xlim((0,1.2))
	#ax.set_ylim((0,0.7))
	x = pearsonr(b_1, b_6)
	ax.set_title('A comparison of Band 1 and Band 6 Reflectance.', fontsize=15, family='sans-serif')
	ax.text(0.6, 0.54, r'$Slope = %s$' % round(slope, 4), fontsize=15, horizontalalignment='right')
	ax.text(0.6, 0.57, r'$Correlation Coefficient = %s$' % round(x[0], 4), fontsize=15, horizontalalignment='right')
	
	ax.autoscale_view()

	#set labels
	ax.set_xlabel('Band 1 Reflectance', fontsize=12, family='sans-serif')
	ax.set_ylabel('Band 6 Reflectance', fontsize=12, family='sans-serif')
	
	ax.legend()

	fig.savefig('b1_v_b6.png')

	fig1 = plt.figure(figsize=(10,8))
	gs1 = mpl.gridspec.GridSpec(1,1)
	bx = fig1.add_subplot(gs1[0])

	bx.spines['top'].set_visible(False)
	bx.spines['bottom'].set_linewidth(.8)
	bx.xaxis.set_ticks_position('bottom')

	bx.spines['right'].set_visible(False)
	bx.spines['left'].set_linewidth(0.8)
	bx.yaxis.set_ticks_position('left')

	#set tick properties
	bx.xaxis.set_tick_params('major', length=2, labelsize=10)
	bx.yaxis.set_tick_params('major', length=2, labelsize=10)

	z1 = np.polyfit(b_7, b_6, 2)
	p1 = np.poly1d(z1)
	slope1, y_inter1 = np.polyder(p1)
	x = pearsonr(b_7, b_6)

	bx.text(0.1, 0.57, r'$Correlation Coefficient = %s$' % round(x[0], 4), fontsize=15, horizontalalignment='left')
	bx.text(0.1, 0.54, r'$Slope = %s$' % round(slope1, 4), fontsize=15, horizontalalignment='left')
	
	#plot data and customize look of plot
	bx.plot(b_7, b_6, marker='.', color='k', linestyle='',
	        markersize=4, clip_on=False, alpha=0.9)

	a = bx.plot(b_7, p1(b_7), marker='*', color='red', linestyle='-',
        markersize=4, clip_on=False, label='Linear regression line')

	#set axis limits 
	#ax.set_xlim((0,1.2))
	#ax.set_ylim((0,0.7))
	bx.set_title('A comparison of Band 7 and Band 6 Reflectance.', fontsize=15, family='sans-serif')
	bx.autoscale_view()
	#set labels

	bx.set_xlabel('Band 7 Reflectance', fontsize=12, family='sans-serif')
	bx.set_ylabel('Band 6 Reflectance', fontsize=12, family='sans-serif')	
	bx.legend()

	fig1.savefig('b7_v_b6.png')


if __name__ == '__main__':
    main()