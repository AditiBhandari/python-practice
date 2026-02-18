### MODULE 2 EXTRACTING DATA WITH REGULAR EXPRESSIONS

# import re

# filename = open("regex_sum_2363595.txt","r")

# total = list()

# for line in filename:
# 	line = line.strip()
# 	findNum = re.findall('([0-9]+)',line)
# 	if len(findNum) >= 1:
# 		# for number in findNum:
# 		# 	number = float(number)
# 		# This doesn't work because it doesn't write the converted numbers back into the list
# 		findNum = list(map(int, findNum))
# 		sumNum = sum(findNum)
# 		total.append(sumNum)
# print(sum(total))


### MODULE 3 UNDERSTANDING THE REQUEST / RESPONSE CYCLE

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()