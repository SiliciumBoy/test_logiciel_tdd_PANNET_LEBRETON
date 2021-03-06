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

def suite_arith_function(int_list):
	int_list.sort()
	if len(int_list) > 1:
		diff = int_list[1] - int_list[0]
		for index in range(1, len(int_list) - 1):
			if (int_list[index + 1] - int_list[index]) != diff:
				return False
		return True
	else:
		return False

def suite_geo_function(int_list):
	int_list.sort()
	zero = 0 in int_list
	if zero is True:
		return False

	not_negative = bool([item for item in int_list if item < 0])
	if not_negative is True:
		return False

	if len(int_list) > 1:
		div = int_list[1] / int_list[0]
		for index in range(1, len(int_list) - 1):
			if (int_list[index + 1] / int_list[index]) != div:
				return False
		return True
	else:
		return False

def suite_arith_next(int_list, n):
		int_list.sort()
		if len(int_list) > 1:
			diff = int_list[1] - int_list[0]
			for index in range(1, len(int_list) - 1):
				if (int_list[index + 1] - int_list[index]) != diff:
					return False, int_list
			if n >= 0:
				for index in range(0, n):
					int_list.append(int_list[-1] + diff)
			return True, int_list
		return False, int_list
	

def suite_geo_next(int_list, n):
	int_list.sort()
	zero = 0 in int_list
	if zero is True:
		return False, int_list

	not_negative = bool([item for item in int_list if item < 0])
	if not_negative is True:
		return False, int_list

	if len(int_list) > 1:
		div = int_list[1] / int_list[0]
		for index in range(1, len(int_list) - 1):
			if (int_list[index + 1] / int_list[index]) != div:
				return False, int_list
		if n >= 0:
			for index in range(0, n):
				int_list.append(int_list[-1] * div)
			int_list.sort()
		return True, int_list
	return False, int_list