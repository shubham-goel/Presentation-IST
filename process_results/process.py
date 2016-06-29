import math
from scipy.special import comb
from decimal import *

import time
import pickle
import itertools
import subprocess
import numpy as np

def load_from_file(filename):
	file = open(filename, 'r')
	return  pickle.load(file)

for n in range(4,8):
	m=n
	e=int(2.5*n)
	t=n
	l=n

	filename = 'MONTE_CARLO_dat_files/n{}-m{}-e{}-t{}-l{}.dat'.format(n,m,e,t,l)
	(params,rt_dat,prob) = load_from_file(filename)

	assert params['n'] == n
	assert params['e'] == e
	assert params['m'] == m
	assert params['t'] == t
	assert params['l'] == l

	print n,rt_dat['2m'],rt_dat['2mt']
print ''
print ''
print ''
print ''
print ''
for n in range(11,41):
	m=n
	e=int(2.5*n)
	t=n
	l=n

	filename = 'MONTE_CARLO_dat_files/n{}-m{}-e{}-t{}-l{}.dat'.format(n,m,e,t,l)
	(params,rt_dat,prob) = load_from_file(filename)

	assert params['n'] == n
	assert params['e'] == e
	assert params['m'] == m
	assert params['t'] == t
	assert params['l'] == l

	print n,rt_dat['2m'],rt_dat['2mt']