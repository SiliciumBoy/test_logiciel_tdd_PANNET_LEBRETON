import numpy as np

def min_function(a, b):
	if a < b:
		return a
	return b

def mean_function(int_list):
	list_sum = 0
	for nb in int_list:
		list_sum += nb
	return list_sum // len(int_list)

def mediane_function(a):
	return np.median(a)

def ecart_type_function(a):
	return np.std(a)
