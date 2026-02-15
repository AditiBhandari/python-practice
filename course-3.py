### MODULE 2 EXTRACTING DATA WITH REGULAR EXPRESSIONS

import re

filename = open("regex_sum_2363595.txt","r")

total = list()

for line in filename:
	line = line.strip()
	findNum = re.findall('([0-9]+)',line)
	if len(findNum) >= 1:
		# for number in findNum:
		# 	number = float(number)
		# This doesn't work because it doesn't write the converted numbers back into the list
		findNum = list(map(int, findNum))
		sumNum = sum(findNum)
		total.append(sumNum)
print(sum(total))


