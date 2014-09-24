import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib as mpl

# generate some random data
t = np.arange(0.1, 9.2, 0.15)
#print "t\n", t
#print len(t)
y = t + np.random.rand(len(t))
#print "y\n", y
#print len(y)

#first create the figure
fig = plt.figure(figsize=(5,3))

#create a grid of 1 row and 1 column for the plot
#[left, bottom, width, height]
gs = mpl.gridspec.GridSpec(1,1)
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
ax.xaxis.set_tick_params('major', length=2, labelsize=6)
ax.yaxis.set_tick_params('major', length=2, labelsize=6)

#plot data and customize look of plot
ax.plot(t,y, marker='.', color='k', linestyle='',
        markersize=4, clip_on=False)

#set axis limits 
ax.set_xlim((-2,12))
ax.set_ylim((-2,12))

#scale the view to show all datapoints
ax.autoscale_view()

#set labels
ax.set_xlabel(r'voltage (V, $\mu$V)', fontsize=6, family='sans-serif')
ax.set_ylabel('luminescence (L)', fontsize=6, family='sans-serif')

fig.savefig('mpl_template.png')