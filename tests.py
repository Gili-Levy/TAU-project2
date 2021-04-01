#binary


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




#roulette



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
"""


# dividors

"""
counter = 0

# 6a


def divisors(n):
	# lst = [x for x in range(1, n) if n % x == 0]
	global counter
	lst = []
	for x in range(1, n):
		if n % x == 0:
			lst.append(x)
		counter += 1
	return lst


# 6b
def perfect_numbers(n):
	global counter
	perfects = 0
	lst = []
	#inside_counter = 0
	
	i = 2  # the numbers we're going through
	inside_counter = 0
	while perfects < n:  # we want to find n numbers
		sum_divs = 0
		lstlst = divisors(i)
		inside_counter += (len(lstlst) + (i-1))
		for div in lstlst:  # summing up the dividers
			sum_divs += div
			counter += 1
		if sum_divs == i:  # is perfect number?
			lst.append(i)
			perfects += 1
		i += 1
	print(inside_counter)
	return lst


print(perfect_numbers(3), counter)
"""


# 4b

def old_has_repeat2(s, k):
	for i in range(0, len(s)-k):
		str1 = s[i:i+k]
		for j in range(i+1, len(s)-k+1):
			str2 = s[j:j+k]
			if str1 == str2:
				return True
	return False



def has_repeat2(s, k):
	for i in range(0, len(s)-k): # i is the beginning of the 1st string
		for j in range (i+1, len(s)-k+1): # j is the beginning of the 2nd string
			s1 = s[i]
			s2 = s[j]
			if (s1 == s2) & (k == 1):  # if letters are equal
				return True
			if  s1 == s2:  # if letters are equal
				counter = 1
				for n in range (1, k):  # go through the next k-1 letters and check them
					s1 = s[i+n]
					s2 = s[j+n]
					if s1 != s2:  # if strings are not equal, search for a differnt j
						break
					elif s1 == s2: # checks if each letter is equal
						counter += 1
					
					if counter == k: # found k notes that are equal
						return True
	return False

print (has_repeat2("aba",1))

"""
if not has_repeat2("ababa", 3) or \
			has_repeat2("ababa", 4) or \
			not has_repeat2("aba", 1):

"""
