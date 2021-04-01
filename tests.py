"""
def binary_search(lst, key):
	"""""" lst better be sorted for binary search to work """"""
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

"""
from hw2_316296771 import roulette_repeat

gili = "gili"
i=10
while (i<5) and (gili[4] != "w"):
	print (i)
	i+=1


positive200 = 0
for i in range(1, 101):
	profit = roulette_repeat(100, 200)
	if profit > 0:
		positive200 += 1
print("200: ", positive200)

positive1000 = 0
for i in range(1, 101):
	profit = roulette_repeat(100, 1000)
	if profit > 0:
		positive1000 += 1
print("1000: ", positive1000)

positive10000 = 0
for i in range(1, 101):
	profit = roulette_repeat(100, 10000)
	if profit > 0:
		positive10000 += 1
print("10000: ", positive10000)
