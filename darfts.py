def binary_search(lst, key):
	""" lst better be sorted for binary search to work """
	n = len(lst)
	left = 0
	right = n-1
	while left <= right:
		mid = (left+right)//2  # middle rounded down
		if key == lst[mid]:  # item found
			return mid
		elif key < lst[mid]:  # item not in top half
			right = mid
		else:  # item not in bottom half
			left = mid
	print(key, "not found")
	return None


print(binary_search([1,1,1,2,2,2,3,3,3,3,3,4,5,5,6],4))
