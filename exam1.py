import numpy as np
def summary_stats(arr):
	"""
	This function calculates summary statistics for a NumPy array.
	Args:
	arr: A NumPy array.
	Returns:
	A list containing the mean, max, and min of the array.
	"""
	return [arr.mean(), arr.max(), arr.min()]
#test
a=np.array(np.random.rand(5))
summary=summary_stats(a)
print(summary)