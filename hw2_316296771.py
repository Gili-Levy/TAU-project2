import random  # loads python's random module in order to use random.random() in question 2

SUBMISSION_IDS = ["316296771"]

############
# QUESTION 1
############


# 1a
def risk_factor(n):
	if n==0: #no vaccines
		return 1
	elif n<21: # 1st vaccine
		return (1-(n/21*0.5))
	return (0.5-((min(14,(n-21))/14*0.4))) # 2nd vaccine


# 1b
def students_risk_factors(students):
	dict={}
	for key in students:
		dict[key] = risk_factor(students[key])
	return dict


# 1c
def class_risk_factor(student_factors):
	length = len(student_factors)
	sum = 0
	if length == 0: #empty dict
		return sum
	for key in student_factors:
		sum+=student_factors[key]
	return (sum/length)


# 1d
def convert_to_list(student_factors):
	lst = []
	for key in student_factors: #create list of tuples
		lst.append((key,student_factors[key]))
	sorted_lst = sorted(lst, key=lambda tup: tup[1]) #sort tuples by risk factor
	return sorted_lst


# 1e
def partition_class(student_factors, threshold):
	campus = {}
	campus_check = {}
	home = {}
	sorted_tup_list = convert_to_list(student_factors)
	for student in sorted_tup_list: # enters the allowed students to campus dict (empty dict if no student is allowed)
		campus_check[student[0]] = student[1]
		if class_risk_factor(campus_check) < threshold:
			campus[student[0]] = student[1]
		else:
			home[student[0]] = student[1]
	return (campus, home)


############
# QUESTION 2
############

# 2a
def coin():
	rand = random.random()
	if rand < 0.5:
		return True
	return False


def roll_dice(d):
	return random.randint(1, d)


def roulette(bet_size, parity):
	num = roll_dice(37)-1
	if num == 0:
		return 0
	if num % 2 == 0: #checks num parity
		parity_num="even"
	else:
		parity_num="odd"
	if parity_num == parity: # win
		return bet_size * 2
	return 0 # lose


def roulette_repeat(bet_size, n):
	profit = 0
	for i in range(0,n):
		if coin() == True: # chooses odd/even
			parity= "odd"
		else:
			parity = "even"
		profit += roulette(bet_size,parity) - bet_size # checks each game profit
	return profit

"""
positive = 0
for i in range (1,101):
	profit = roulette_repeat(100,10000)
	if profit > 0:
		positive += 1
print (positive)
"""

############
# QUESTION 3
############


import time
# 3a
def inc(binary):
	binary = binary[::-1] # flip string
	for i in range (0,len(binary)): # go through bits
		if binary[i] == "1": # if 1 - turn to 0
			binary = binary[:i] + "0" + binary[i+1:]
		elif binary[i] == "0": # if 0 - turn to 1 - and stop
			binary = binary[:i] + "1" + binary[i+1:]
			return (binary[::-1])
	binary = binary + "1" # if only zeros(=originally only 1's) - add 1
	return (binary[::-1])


# 3b
def dec(binary):
	binary = binary[::-1]  # flip string
	for i in range(0, len(binary)) :  # go through bits
		if (binary[i] == "1") and (i==0): # 1 is 1st
			binary = "0" + binary[i+1:]
			return (binary[::-1])
		elif (binary[i] == "1") and (i == len(binary)-1) : # 1 is last
			binary = "1"*(len(binary)-1)
			return binary
		elif binary[i]  == "1" : # 1 is in the middle
			binary = "1"*i + "0" + binary[i+1:]
			return (binary[::-1])


# 3c
def add(bin1, bin2):
	pass  # replace with your code


# 3d
def leq(bin1, bin2):
	pass  # replace with your code


# 3e
def is_divisor(bin1, bin2):
	pass  # replace with your code


############
# QUESTION 4
############

# 4a
def has_repeat1(s, k):
	pass  # replace with your code


# 4b
def has_repeat2(s, k):
	pass  # replace with your code


############
# QUESTION 5
############

def parse_primes(filename):
	primes = []
	with open(filename, "r") as f:
		for line in f:
			primes += [int(num_str)
					   for num_str in line.split(" ")[:-1] if num_str]
	return set(primes)

# 5a


def check_goldbach_for_num(n, primes_set):
	pass  # replace with your code


# 5b
def check_goldbach_for_range(limit, primes_set):
	pass  # replace with your code


# 5c1
def check_goldbach_for_num_stats(n, primes_set):
	pass  # replace with your code


# 5c2
def check_goldbach_stats(limit, primes_set):
	pass  # replace with your code

############
# QUESTION 6
############


# 6a
def divisors(n):
	pass  # replace with your code


# 6b
def perfect_numbers(n):
	pass  # replace with your code


# 6c
def abundant_density(n):
	pass  # replace with your code


# 6e
def semi_perfect_3(n):
	pass  # replace with your code


########
# Tester
########

def test():
	if risk_factor(0) != 1 or \
			risk_factor(10) != 16/21 or \
			risk_factor(25) != 27/70 or \
			risk_factor(100) != 0.5 - 0.4:
		print("#1a - error in risk_factor")

	students = {"Alon": 10, "Gal": 25}
	risk_factors = students_risk_factors(students)
	if len(risk_factors) != 2:
		print("#1b1 - error in students_risk_factors")
	if risk_factors["Alon"] != 16/21 or risk_factors["Gal"] != 27/70:
		print("#1b2 - error in students_risk_factors")

	students = {"Tom": 0.65, "Alon": 0.3, "Gal": 0.55}
	if class_risk_factor(students) != 0.5:
		print("#1c - error in class_risk_factor")

	students = {"Tom": 0.65, "Alon": 0.3, "Gal": 0.55}
	if convert_to_list(students) != [('Alon', 0.3), ('Gal', 0.55), ('Tom', 0.65)]:
		print("#1d - error in convert_to_list")

	students = {"Tom": 0.65, "Alon": 0.3, "Gal": 0.55}
	if convert_to_list(students) != [("Alon", 0.3), ("Gal", 0.55), ("Tom", 0.65)] or \
	   partition_class(students, 0.55) != ({"Alon": 0.3, "Tom": 0.65, "Gal": 0.55}, {}) or \
	   partition_class(students, 0.45) != ({"Alon": 0.3, "Gal": 0.55}, {"Tom": 0.65}) or \
	   partition_class(students, 0.4) != ({"Alon": 0.3}, {"Tom": 0.65, "Gal": 0.55}) or \
	   partition_class(students, 0.25) != ({}, {"Alon": 0.3, "Tom": 0.65, "Gal": 0.55}):
		print("#1e - error in partition_class")

	for i in range(10):
		if coin() not in {True, False}:
			print("#2a - error in coin")
			break

	for i in range(10):
		if roll_dice(6) not in {1, 2, 3, 4, 5, 6}:
			print("2b - error in roll_dice")
			break

	for i in range(10):
		if (roulette(100, "even") not in {0, 200}) or (roulette(100, "odd") not in {0, 200}):
			print("2c - error in roulette")
			break

	if inc("0") != "1" or \
	   inc("1") != "10" or \
	   inc("101") != "110" or \
	   inc("111") != "1000" or \
	   inc(inc("111")) != "1001":
		print("#3a - error in inc")

	if dec("1") != "0" or \
	   dec("10") != "1" or \
	   dec("110") != "101" or \
	   dec("1000") != "111" or \
	   dec(dec("1001")) != "111":
		print("#3b - error in dec")

	if add("0", "1") != "1" or \
	   add("1", "1") != "10" or \
	   add("110", "11") != "1001" or \
	   add("111", "111") != "1110":
		print("#3c - error in add")

	if not leq("1010", "1010") or \
	   leq("1010", "0") or \
	   leq("1011", "1010"):
		print("#3d - error in leq")

	if not is_divisor("1000", "100") or \
	   is_divisor("1001", "101") or \
	   is_divisor("111", "100"):
		print("#3d - error in is_divisor")

	if not has_repeat1("ababa", 3) or \
			has_repeat1("ababa", 4) or \
			not has_repeat1("aba", 1):
		print("#4a - error in has_repeat1")

	if not has_repeat2("ababa", 3) or \
			has_repeat2("ababa", 4) or \
			not has_repeat2("aba", 1):
		print("#4b - error in has_repeat2")

	if not check_goldbach_for_num(10, {2, 3, 5, 7}) or \
	   check_goldbach_for_num(10, {2, 3}):
		print("5a - error in check_goldbach_for_num")

	if not check_goldbach_for_range(20, {2, 3, 5, 7, 11}) or \
	   check_goldbach_for_range(21, {2, 3, 5, 7, 11}):
		print("5b - error in check_goldbach_for_range")

	primes_set = parse_primes('primes.txt')
	if check_goldbach_for_num_stats(20, primes_set) != 2 or \
	   check_goldbach_for_num_stats(10, primes_set) != 2:
		print("5c - error in check_goldbach_for_num_stats()")

	if check_goldbach_stats(11, primes_set) != {1: 3, 2: 1}:
		print("error in check_goldbach_stats")

	if divisors(6) != [1, 2, 3] or divisors(7) != [1]:
		print("6a - error in divisors")

	if perfect_numbers(2) != [6, 28]:
		print("6b - error in perfect_numbers")

	if abundant_density(20) != 0.15:
		print("6c - error in adundant_density")

	if semi_perfect_3(18) != [3, 6, 9] or semi_perfect_3(20) is not None:
		print("6e - error in semi_perfect_3")
