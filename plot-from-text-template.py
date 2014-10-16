#!/usr/bin/python

import matplotlib as mpl
import numpy as np
from matplotlib import gridspec
from pylab import *
from scipy import stats
from scipy import optimize
from scipy import integrate

from mpl_toolkits.axes_grid1 import make_axes_locatable

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
f35ca = '35-ca-gofr-oxygens-unconstrained.dat' 
f35mg = '35-mg-gofr-oxygens-unconstrained.dat'
f45ca = '45-ca-gofr-oxygens-single-for-angles.dat'
f45mg = '45-mg-gofr-oxygens-single-for-angles.dat'
a, b = np.loadtxt(f35ca, usecols=(0,1), unpack=True)
c, d = np.loadtxt(f35mg, usecols=(0,1), unpack=True)
e, f = np.loadtxt(f45ca, usecols=(0,1), unpack=True)
g, h = np.loadtxt(f45mg, usecols=(0,1), unpack=True)

x = np.linspace(0, 10.0, num = 200)

b_int = integrate.cumtrapz(b, a, initial = 0)
d_int = integrate.cumtrapz(d, c, initial = 0)
f_int = integrate.cumtrapz(f, e, initial = 0)
h_int = integrate.cumtrapz(h, g, initial = 0)

fig = plt.figure(figsize=(11,8.5))
gs = gridspec.GridSpec(1,1,wspace=0.2,hspace=0.05)
ax1 = fig.add_subplot(gs[0])

ax1.plot(a,b/sum(b_int),c='g')
ax1.plot(c,d/sum(d_int),c='g')
ax1.plot(e,f/sum(f_int),c='g')
ax1.plot(g,h/sum(h_int),c='g')

plt.show()
