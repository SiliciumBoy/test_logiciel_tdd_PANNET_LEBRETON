import numpy as np

def min_function(a, b):
	if a < b:
		return a
	return b

<<<<<<< HEAD
def mean_function(int_list):
	list_sum = 0
	for nb in int_list:
		list_sum += nb
	return list_sum // len(int_list)
=======
def mediane_function(a):
	return np.median(a)
>>>>>>> 955580776fe18d12e67f7f986718267c06051733
