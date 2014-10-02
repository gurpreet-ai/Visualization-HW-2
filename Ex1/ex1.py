import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib as mpl

def main ():
	data = np.recfromcsv('crabs.csv', usecols=(1, 2, 3, 4, 5, 6, 7, 8))
	
	# plotting the CL carapace length (mm) V. CW carapace width (mm).
	CL = data['cl']
	line1 = [i for i in data['cl']]

	CW = data['cw']
	line2 = [i for i in CW]

	#CL and RW each against FL
	RW = data['rw']
	line3 = [i for i in RW]

	FL = data['fl']
	line4 = [i for i in FL]

	#first create the figure
	fig1 = plt.figure(figsize=(12,8))

	#create a grid of 1 row and 1 column for the plot
	#[left, bottom, width, height]
	gs = mpl.gridspec.GridSpec(1,1)
	
	#put a plot in the first row, first column
	ax = fig1.add_subplot(gs[0])

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

	fig1.savefig('figure1.png')

	#put a plot in the first row, second column
	#CL and RW each against FL

	fig2 = plt.figure(figsize=(12,8))
	gs2 = mpl.gridspec.GridSpec(1,2)

	bx = fig2.add_subplot(gs2[0])

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
	cx = fig2.add_subplot(gs2[1])

	#Have only two spines visible and set properties
	cx.spines['top'].set_visible(False)
	cx.spines['bottom'].set_linewidth(.5)
	cx.xaxis.set_ticks_position('bottom')

	cx.spines['right'].set_visible(False)
	cx.spines['left'].set_linewidth(0.5)
	cx.yaxis.set_ticks_position('left')

	cx.xaxis.set_tick_params('major', length=2, labelsize=10)
	cx.yaxis.set_tick_params('major', length=2, labelsize=10)

	cx.set_xlim((0,50))
	cx.set_ylim((0,60))

	cx.set_xlabel('CL carapace length (mm)', fontsize=10, family='sans-serif')
	cx.set_ylabel('RW rear width (mm)', fontsize=10, family='sans-serif')
	cx.set_title('CL and RW V. FL', fontsize=10, family='sans-serif')

	cx.scatter(line1, line4, s=line3)

	fig2.savefig('figure2.png')

	index			 = data['index'][0:50]
	blue_crab_male 	 = data['fl'][0:50]
	blue_crab_female = data['fl'][50:100]
	oran_crab_male 	 = data['fl'][100:150]
	oran_crab_female = data['fl'][150:200]

	fig3 = plt.figure(figsize=(12,8))
	gs3 = mpl.gridspec.GridSpec(1,1)

	dx = fig3.add_subplot(gs3[0])

	#Have only two spines visible and set properties
	dx.spines['top'].set_visible(False)
	dx.spines['bottom'].set_linewidth(.5)
	dx.xaxis.set_ticks_position('bottom')

	dx.spines['right'].set_visible(False)
	dx.spines['left'].set_linewidth(0.5)
	dx.yaxis.set_ticks_position('left')

	dx.xaxis.set_tick_params('major', length=2, labelsize=10)
	dx.yaxis.set_tick_params('major', length=2, labelsize=10)

	dx.set_xlabel('index', fontsize=10, family='sans-serif')
	dx.set_ylabel('FL frontal lobe size (mm)', fontsize=10, family='sans-serif')
	dx.set_title('FL V. index', fontsize=10, family='sans-serif')

	z = np.polyfit(index, blue_crab_male, 2)
	p = np.poly1d(z)

	dx.plot(index, blue_crab_male, marker='.', color='blue', linestyle='',
        markersize=4, clip_on=False)

	dx.plot(index, p(index), marker='.', color='blue', linestyle='-',
        markersize=4, clip_on=False)

	z = np.polyfit(index, blue_crab_female, 2)
	p = np.poly1d(z)

	dx.plot(index, blue_crab_female, marker='.', color='green', linestyle='',
        markersize=4, clip_on=False)

	dx.plot(index, p(index), marker='.', color='blue', linestyle='-',
        markersize=4, clip_on=False)

	z = np.polyfit(index, oran_crab_male, 2)
	p = np.poly1d(z)
	
	dx.plot(index, oran_crab_male, marker='.', color='black', linestyle='',
        markersize=4, clip_on=False)

	dx.plot(index, p(index), marker='.', color='black', linestyle='-',
        markersize=4, clip_on=False)

	z = np.polyfit(index, oran_crab_female, 2)
	p = np.poly1d(z)

	dx.plot(index, oran_crab_female, marker='.', color='orange', linestyle='',
        markersize=4, clip_on=False)

	dx.plot(index, p(index), marker='.', color='orange', linestyle='-',
        markersize=4, clip_on=False)

	dx.set_xlim((0,50))
	dx.set_ylim((0,25))

	#scale the view to show all datapoints
	dx.autoscale_view()
	
	fig3.savefig('figure3.png')


if __name__ == '__main__':
    main()