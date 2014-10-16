#!/usr/bin/python

import matplotlib as mpl
mpl.use('Agg')
import numpy as np
from matplotlib import gridspec
from pylab import *
from scipy import stats
from scipy import optimize
from scipy import integrate
import gromacs
import gromacs.formats

from mpl_toolkits.axes_grid1 import make_axes_locatable
import brewer2mpl
clrs = [brewer2mpl.get_map('Set1','qualitative',9).mpl_colors[i] for i in range(9)]


font = {'family' : 'sans-serif',
        'size'   : 22}
mpl.rc('font', **font)
mpl.rc('text', usetex=True)
mpl.rc('text.latex', preamble='\usepackage{sfmath}')
mpl.rcParams['text.latex.preamble'] = [r'\usepackage{sfmath}',r'\usepackage{amsmath}',
					r'\usepackage{siunitx}',r'\sisetup{detect-all}',
		                        r'\usepackage{helvet}',r'\usepackage{sansmath}',
		                        r'\sansmath', r'\usepackage{upgreek}']
mpl.rcParams['xtick.major.pad'] = 8
mpl.rcParams['ytick.major.pad'] = 8

dir = ''
input_dir = '' # Dirac

data = gromacs.fileformats.xvg.XVG(filename='histo.xvg')

fig = plt.figure(figsize=(11,8.5))
gs = gridspec.GridSpec(2,1,wspace=0.4,hspace=0.1)
ax1 = fig.add_subplot(gs[0,0])

for i in range(len(data.array)-1):
	ax1.plot(data.array[0],data.array[i+1],c=clrs[i%9],lw=4)
	ax1.fill_between(data.array[0],0,data.array[i+1],facecolor=clrs[i%9],alpha=0.5)
ax1.grid()
ax1.set_ylabel('Counts')
ax1.get_yaxis().set_label_coords(-0.1,0.5)
#ax1.set_xlabel('Distance (A)')
ax1.set_xticklabels([]) 
#ax1.set_ylim([0,-1.5])
#ax1.get_yaxis().set_label_coords(-0.25,0.5)
#ax1.yaxis.set_major_locator(MaxNLocator(5, prune='lower'))

ax2 = fig.add_subplot(gs[1,0])
data = gromacs.fileformats.xvg.XVG(filename='profile.xvg')

ax2.plot(data.array[0],data.array[1],c=clrs[0],lw=4)
ax2.grid()
ax2.set_ylabel('Free energy (kCal/mol)')
ax2.get_yaxis().set_label_coords(-0.1,0.5)
ax2.set_xlabel('Distance (A)')
#ax1.set_xticklabels([]) 
#ax1.set_ylim([0,-1.5])
#ax1.get_yaxis().set_label_coords(-0.25,0.5)
#ax1.yaxis.set_major_locator(MaxNLocator(5, prune='lower'))

gs.tight_layout(fig, rect=[0.0, 0.0, 1, 1]) # Leave space for the common x-label.
plt.savefig('profile.png', dpi=300)
plt.close()
