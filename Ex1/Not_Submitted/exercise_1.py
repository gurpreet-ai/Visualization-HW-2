import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

def set_spines(xx):
	xx.spines['top'].set_visible(False)
	xx.spines['bottom'].set_linewidth(0.5)
	xx.xaxis.set_ticks_position('bottom')

	xx.spines['right'].set_visible(False)
	xx.spines['left'].set_linewidth(0.5)
	xx.yaxis.set_ticks_position('left')

def set_tick_properties(xx):
	xx.xaxis.set_tick_params('major', length=2, labelsize=10)
	xx.yaxis.set_tick_params('major', length=2, labelsize=10)

def set_labels(xx, x, y, title):
	xx.set_xlabel(x, fontsize=12, family='sans-serif')
	xx.set_ylabel(y, fontsize=12, family='sans-serif')
	xx.set_title(title, fontsize=15, family='sans-serif')

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
	BD = [i for i in data['bd']]

	gs   = mpl.gridspec.GridSpec(1, 1)
	fig1 = plt.figure(figsize=(14, 8))

	ax   = fig1.add_subplot(gs[0])
	
	set_spines(ax)
	set_tick_properties(ax)
	set_labels(ax, r'$Carapace  Length [mm]$', r'$Carapace  Width [mm]$', r'$Carapace  Width [mm]$  V.  $Carapace  Length [mm]$')
	set_lim(ax, 50, 60)
			
	ax.plot(CL, CW, marker='.', color='k', linestyle='',
        markersize=4, clip_on=False)

	ax.autoscale_view()

	fig1.savefig('figure_1.png')

	# CL dependent (y) variable, CW independent (x) variable
	fig2 = plt.figure(figsize=(14,8))
	gs2  = mpl.gridspec.GridSpec(1,2)
	bx   = fig2.add_subplot(gs2[0])	

	bx.spines['top'].set_visible(False)
	bx.xaxis.set_ticks_position('bottom')
	set_tick_properties(bx)
	set_labels(bx, r'$Carapace  Width  [mm]$', r'$Carapace  Length [mm]$', 'CL and FL V. CW')
	set_lim(bx, 60, 60)

	a = bx.plot(CW, CL, marker='.', color='blue', linestyle='',
        markersize=4, clip_on=False)
	
	fig2.subplots_adjust(left=0.075, right=0.95, top=0.9, bottom=.5)
	
	bx.legend(a,['CL V CW'])

	bx2  = bx.twinx()
	bx2.set_ylabel(r'$Frontal  Lobe Size [mm]$', fontsize=12, family='sans-serif', rotation=270)
	bx2.yaxis.set_tick_params('major', length=2, labelsize=10)
	bx2.set_ylim(0, 60)
	bx2.set_xlim(10, 60)

	b = bx2.plot(CW, FL, marker='.', color='green', linestyle='',
        markersize=4, clip_on=False)
	
	bx2.legend(b, ['FL V CW'], loc="upper left")

	plt.subplots_adjust(left=0.075, right=0.95, top=0.9, bottom=.1)

	bx.autoscale_view()
	bx2.autoscale_view()

	cx   = fig2.add_subplot(gs2[1])
	
	set_spines(cx)
	set_tick_properties(cx)
	set_labels(cx, r'$Carapace  Width [mm]$', r'$Frontal  Lobe  Size [mm]$', 'CL and FL V. CW')
	set_lim(cx, 60, 30)
	
	cx.scatter(CW, FL, s=CL, alpha=1)
	cx.autoscale_view()
	
	fig2.savefig('figure_2.png')

	fig3 = plt.figure(figsize=(14,8))
	gs3 = mpl.gridspec.GridSpec(1,1)
	dx = fig3.add_subplot(gs3[0])
	set_spines(dx)
	set_tick_properties(dx)
	set_labels(dx, r'$Carapace  Width [mm]$', r'$Frontal  Lobe  Size [mm]$', 'CL and FL V. CW')
	
	CL_Blue_male   = [i['cl'] for i in data if i['sp'] == 'B' and i['sex'] == 'M']
	CL_Blue_female = [i['cl'] for i in data if i['sp'] == 'B' and i['sex'] == 'F']
	CL_Oran_male   = [i['cl'] for i in data if i['sp'] == 'O' and i['sex'] == 'M']
	CL_Oran_female = [i['cl'] for i in data if i['sp'] == 'O' and i['sex'] == 'F']

	CW_Blue_male   = [i['cw'] for i in data if i['sp'] == 'B' and i['sex'] == 'M']
	CW_Blue_female = [i['cw'] for i in data if i['sp'] == 'B' and i['sex'] == 'F']
	CW_Oran_male   = [i['cw'] for i in data if i['sp'] == 'O' and i['sex'] == 'M']
	CW_Oran_female = [i['cw'] for i in data if i['sp'] == 'O' and i['sex'] == 'F']

	FL_Blue_male   = [i['fl'] for i in data if i['sp'] == 'B' and i['sex'] == 'M']
	FL_Blue_female = [i['fl'] for i in data if i['sp'] == 'B' and i['sex'] == 'F']
	FL_Oran_male   = [i['fl'] for i in data if i['sp'] == 'O' and i['sex'] == 'M']
	FL_Oran_female = [i['fl'] for i in data if i['sp'] == 'O' and i['sex'] == 'F']

	dx.scatter(CW_Blue_male, FL_Blue_male, s=CL_Blue_male, alpha=1, color="Navy", label="Blue Male")
	dx.scatter(CW_Blue_female, FL_Blue_female, s=CL_Blue_female, alpha=1, color="Aqua", label="Blue female")
	dx.scatter(CW_Oran_male, FL_Oran_male, s=CL_Oran_male, alpha=1, color="Orange", label="Orange Male")
	dx.scatter(CW_Oran_female, FL_Oran_female, s=CL_Oran_female, alpha=1, color="OrangeRed", label="Orange female")
	
	dx.legend(loc='upper left')

	fig3.savefig('figure_3.png')

	fig4 = plt.figure(figsize=(14,8))
	gs4 = mpl.gridspec.GridSpec(1,2)
	ex = fig4.add_subplot(gs4[0])
	
	ex.spines['top'].set_visible(False)
	ex.xaxis.set_ticks_position('bottom')
	set_tick_properties(ex)
	set_labels(ex, r'$Carapace  Width  [mm]$', r'$Body Depth [mm]$', 'BD and RW V. CW')
	set_lim(ex, 60, 60)

	a = ex.plot(CW, BD, marker='.', color='blue', linestyle='',
        markersize=4, clip_on=False)

	
	fig4.subplots_adjust(left=0.075, right=0.95, top=0.9, bottom=.5)
	
	ex.legend(a,['BD V CW'])

	ex2  = ex.twinx()
	ex2.set_ylabel(r'$Rear Width [mm]$', fontsize=12, family='sans-serif', rotation=270)
	ex2.yaxis.set_tick_params('major', length=2, labelsize=10)
	#ex2.set_ylim(0, 60)
	#ex2.set_xlim(10, 60)

	b = ex2.plot(CW, RW, marker='.', color='green', linestyle='',
        markersize=4, clip_on=False)
	
	ex2.legend(b, ['RW V CW'], loc="upper left")

	plt.subplots_adjust(left=0.075, right=0.95, top=0.9, bottom=.1)

	ex.autoscale_view()
	ex2.autoscale_view()

	fx   = fig4.add_subplot(gs4[1])
	
	set_spines(fx)
	set_tick_properties(fx)
	set_labels(fx, r'$Carapace  Width [mm]$', r'$Body Depth [mm]$', 'BD and RW V. CW')
	set_lim(fx, 60, 30)
	
	fx.scatter(CW, BD, s=RW, cmap='jet')
	fx.autoscale_view()
	
	fig4.savefig('figure_4.png')


	fig5 = plt.figure(figsize=(14,8))
	gs5 = mpl.gridspec.GridSpec(1,1)
	gx = fig5.add_subplot(gs3[0])
	set_spines(gx)
	set_tick_properties(gx)
	set_labels(gx, r'$Carapace  Width [mm]$', r'$Body Depth [mm]$', 'BD and RW V. CW')
	
	BD_Blue_male   = [i['bd'] for i in data if i['sp'] == 'B' and i['sex'] == 'M']
	BD_Blue_female = [i['bd'] for i in data if i['sp'] == 'B' and i['sex'] == 'F']
	BD_Oran_male   = [i['bd'] for i in data if i['sp'] == 'O' and i['sex'] == 'M']
	BD_Oran_female = [i['bd'] for i in data if i['sp'] == 'O' and i['sex'] == 'F']

	CW_Blue_male   = [i['cw'] for i in data if i['sp'] == 'B' and i['sex'] == 'M']
	CW_Blue_female = [i['cw'] for i in data if i['sp'] == 'B' and i['sex'] == 'F']
	CW_Oran_male   = [i['cw'] for i in data if i['sp'] == 'O' and i['sex'] == 'M']
	CW_Oran_female = [i['cw'] for i in data if i['sp'] == 'O' and i['sex'] == 'F']

	RW_Blue_male   = [i['rw'] for i in data if i['sp'] == 'B' and i['sex'] == 'M']
	RW_Blue_female = [i['rw'] for i in data if i['sp'] == 'B' and i['sex'] == 'F']
	RW_Oran_male   = [i['rw'] for i in data if i['sp'] == 'O' and i['sex'] == 'M']
	RW_Oran_female = [i['rw'] for i in data if i['sp'] == 'O' and i['sex'] == 'F']

	gx.scatter(CW_Blue_male, 	BD_Blue_male,   s=RW_Blue_male, alpha=1, color="Navy", label="Blue Male")
	gx.scatter(CW_Blue_female,  BD_Blue_female, s=RW_Blue_female, alpha=1, color="Aqua", label="Blue female")
	gx.scatter(CW_Oran_male, 	BD_Oran_male,   s=RW_Oran_male, alpha=1, color="Orange", label="Orange Male")
	gx.scatter(CW_Oran_female, 	BD_Oran_female, s=RW_Oran_female, alpha=1, color="OrangeRed", label="Orange female")
	
	gx.legend(loc='upper left')

	fig5.savefig('figure_5.png')


if __name__ == '__main__':
    main()