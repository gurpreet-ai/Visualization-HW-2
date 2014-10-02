import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

def set_spines(xx):
	xx.spines['top'].set_visible(False)
	xx.spines['bottom'].set_linewidth(.5)
	xx.xaxis.set_ticks_position('bottom')

	xx.spines['right'].set_visible(False)
	xx.spines['left'].set_linewidth(0.5)
	xx.yaxis.set_ticks_position('left')

def set_tick_properties(xx):
	xx.xaxis.set_tick_params('major', length=2, labelsize=10)
	xx.yaxis.set_tick_params('major', length=2, labelsize=10)

def set_labels(xx, x, y, title):
	xx.set_xlabel(x, fontsize=10, family='sans-serif')
	xx.set_ylabel(y, fontsize=10, family='sans-serif')
	xx.set_title(title, fontsize=10, family='sans-serif')

def set_lim(xx, xlim, ylim):
	xx.set_xlim((0,xlim))
	xx.set_ylim((0,ylim))

def plot_polyfit(xx, x, y, deg, col):
	z = np.polyfit(x, y, deg)
	p = np.poly1d(z)

	xx.plot(x, y, marker='.', color=col, linestyle='',
        markersize=4, clip_on=False)

	xx.plot(x, p(x), marker='.', color=col, linestyle='-',
        markersize=4, clip_on=False)

def main ():
	data = np.recfromcsv('crabs.csv', usecols=(1, 2, 3, 4, 5, 6, 7, 8))

	CL = [i for i in data['cl']]
	CW = [i for i in data['cw']]
	RW = [i for i in data['rw']]
	FL = [i for i in data['fl']]

	gs   = mpl.gridspec.GridSpec(1, 1)
	fig1 = plt.figure(figsize=(12, 8))

	ax   = fig1.add_subplot(gs[0])
	
	set_spines(ax)
	set_tick_properties(ax)
	set_labels(ax, 'CL carapace length (mm)', 'CW carapace width (mm)', 'CW V. CL')
	set_lim(ax, 50, 60)
			
	ax.plot(CL, CW, marker='.', color='k', linestyle='',
        markersize=4, clip_on=False)

	ax.autoscale_view()

	fig1.savefig('figure_1.png')

	fig2 = plt.figure(figsize=(12,8))
	gs2  = mpl.gridspec.GridSpec(1,2)

	bx   = fig2.add_subplot(gs2[0])
	
	bx.spines['top'].set_visible(False)
	bx.xaxis.set_ticks_position('bottom')

	set_tick_properties(bx)
	set_labels(bx, 'CL carapace length (mm)', 'RW rear width (mm)', 'CL and RW V. FL')
	set_lim(bx, 50, 30)

	bx.plot(CL, FL, marker='.', color='blue', linestyle='',
        markersize=4, clip_on=False)

	bx2  = bx.twinx()
	bx2.set_ylabel('FL frontal lobe size (mm)', fontsize=10, family='sans-serif')
	bx2.yaxis.set_tick_params('major', length=2, labelsize=10)
	bx2.set_ylim(0, 30)
	bx2.plot(RW, FL, marker='.', color='green', linestyle='',
        markersize=4, clip_on=False)
	
	bx.autoscale_view()

	cx   = fig2.add_subplot(gs2[1])
	
	set_spines(cx)
	set_tick_properties(cx)
	set_labels(cx, 'CL carapace length (mm)', 'RW rear width (mm)', 'CL and RW V. FL')
	set_lim(cx, 50, 25)
	
	cx.scatter(CL, FL, s=RW)
	cx.autoscale_view()
	
	fig2.savefig('figure_2.png')

	index			 = data['index'][0:50]
	blue_crab_male 	 = data['fl'][0:50]
	blue_crab_female = data['fl'][50:100]
	oran_crab_male 	 = data['fl'][100:150]
	oran_crab_female = data['fl'][150:200]

	fig3 = plt.figure(figsize=(12,8))
	gs3 = mpl.gridspec.GridSpec(1,1)
	dx = fig3.add_subplot(gs3[0])

	set_spines(dx)
	set_tick_properties(dx)
	set_labels(dx, 'index', 'FL frontal lobe size (mm)', 'FL V. index')

	plot_polyfit(dx, index, blue_crab_male, 2, 'blue')
	plot_polyfit(dx, index, blue_crab_female, 2, 'green')
	plot_polyfit(dx, index, oran_crab_male, 2, 'orange')
	plot_polyfit(dx, index, oran_crab_female, 2, 'black')

	set_lim(dx, 50, 25)
	
	dx.autoscale_view()
	
	fig3.savefig('figure_3.png')


if __name__ == '__main__':
    main()