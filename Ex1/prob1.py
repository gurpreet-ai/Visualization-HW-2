import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib as mpl

def main ():
	data = np.recfromcsv('crabs.csv', usecols=(1, 2, 3, 4, 5, 6, 7, 8))
	
	size = [x for x in xrange(1, len(data))]
	
	# plotting the CL carapace length (mm) V. CW carapace width (mm).
	CL = data['cl']
	line1 = [i for i in CL]

	CW = data['cw']
	line2 = [i for i in CW]

	#CL and RW each against FL
	RW = data['cl']
	line3 = [i for i in RW]

	FL = data['fl']
	line4 = [i for i in FL]

	#first create the figure
	fig = plt.figure(figsize=(12,8))

	#create a grid of 1 row and 1 column for the plot
	#[left, bottom, width, height]
	gs = mpl.gridspec.GridSpec(1,3)
	#put a plot in the first row, first column
	ax = fig.add_subplot(gs[0])

	#Have only two spines visible and set properties
	ax.spines['top'].set_visible(False)
	ax.spines['bottom'].set_linewidth(.5)
	ax.xaxis.set_ticks_position('bottom')

	ax.spines['right'].set_visible(False)
	ax.spines['left'].set_linewidth(0.5)
	ax.yaxis.set_ticks_position('left')

	#set tick properties
	ax.xaxis.set_tick_params('major', length=2, labelsize=10)
	ax.yaxis.set_tick_params('major', length=2, labelsize=10)

	#plot data and customize look of plot
	ax.plot(line1, line2, marker='.', color='k', linestyle='',
        markersize=4, clip_on=False)

	#set axis limits
	ax.set_xlim((0,50))
	ax.set_ylim((0,60))

	#scale the view to show all datapoints
	ax.autoscale_view()

	#set labels
	ax.set_xlabel('CL carapace length (mm)', fontsize=10, family='sans-serif')
	ax.set_ylabel('CW carapace width (mm)', fontsize=10, family='sans-serif')
	ax.set_title('CW V. CL', fontsize=10, family='sans-serif')

	#put a plot in the first row, second column
	#CL and RW each against FL
	bx = fig.add_subplot(gs[1])

	bx.spines['top'].set_visible(False)
	bx.xaxis.set_ticks_position('bottom')

	bx2 = bx.twinx()

	bx.set_xlabel('CL carapace length (mm)', fontsize=10, family='sans-serif')
	bx.set_ylabel('RW rear width (mm)', fontsize=10, family='sans-serif')
	bx.set_title('CL V. RW V. FL', fontsize=10, family='sans-serif')
	bx2.set_ylabel('FL frontal lobe size (mm)', fontsize=10, family='sans-serif')
	
	bx.xaxis.set_tick_params('major', length=2, labelsize=10)
	bx.yaxis.set_tick_params('major', length=2, labelsize=10)
	bx2.yaxis.set_tick_params('major', length=2, labelsize=10)

	bx.plot(line1, line4, marker='.', color='blue', linestyle='',
        markersize=4, clip_on=False)

	bx2.plot(line3, line4, marker='.', color='green', linestyle='',
        markersize=4, clip_on=False)

	bx2.set_ylim(0, 30)

	bx.set_xlim((0,50))
	bx.set_ylim((0,60))

	#put a plot in the first row, third column
	#CL and RW each against FL
	cx = fig.add_subplot(gs[2])

	#Have only two spines visible and set properties
	cx.spines['top'].set_visible(False)
	cx.spines['bottom'].set_linewidth(.5)
	cx.xaxis.set_ticks_position('bottom')

	cx.spines['left'].set_visible(False)
	cx.spines['right'].set_linewidth(0.5)
	cx.yaxis.set_ticks_position('right')

	cx.xaxis.set_tick_params('major', length=2, labelsize=10)
	cx.yaxis.set_tick_params('major', length=2, labelsize=10)

	cx.set_xlim((0,50))
	cx.set_ylim((0,60))

	cx.scatter(line1, line4, s=line3)

	fig.savefig('figure.png')

	fig1 = plt.figure(figsize=(12,8))

	fig1.savefig('figure1.png')


if __name__ == '__main__':
    main()