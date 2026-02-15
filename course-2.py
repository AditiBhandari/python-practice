### MODULE 1 ASSIGNMENT: PARSE TEXT STRINGS
# text = "X-DSPAM-Confidence:    0.8475"
# print(float(text[text.find('0'):]))



### MODULE 3 ASSIGNMENT: READ A FILE AND PROCESS ITS DATA
# filename = input("Enter filename:")
# openFile = open(filename, "r")

# cumulative = 0
# count = 0

# for line in openFile:
# 	if not line.startswith("X-DSPAM-Confidence:"):
# 		continue
# 	cumulative = cumulative + float(line.rstrip()[-6:])
# 	count = count + 1

# average = cumulative/count

# print("Average spam confidence:",average)



### MODULE 4 ASSIGNMENT: CREATE A SORTED WORD LIST
# fname = input("Enter file name:")
# openFname = open(fname,"r")

# newList = list()
# count = 0

# for eachLine in openFname:
# 	eachSplit = eachLine.split()
# 	while count < len(eachSplit):
# 		if eachSplit[count] not in newList:
# 			newList.append(eachSplit[count])
# 		count = count+1
# 	count = 0

# newList.sort()

# print(newList)



### MODULE 5 ASSIGNMENT: FIND THE MOST FREQUENT SENDER
# handle = open("mbox-short.txt","r")

# sendersDict = dict()

# for eachLine in handle:
# 	if eachLine.startswith("From "):
# 		sender = eachLine.split()[1]
# 		sendersDict[sender] = sendersDict.get(sender,0)+1

# bigcount = None
# bigword = None

# for sender,emails in sendersDict.items():
# 	if bigcount is None or emails > bigcount:
# 		bigcount = emails
# 		bigword = sender
# print(bigword, bigcount)



### MODULE 6 ASSIGNMENT: SORT AND COUNT MESSAGES
# filename = open("mbox-short.txt","r")

# hours = dict()
# tempList = list()

# for line in filename:
# 	if line.startswith("From "):
# 		line = line.strip().split()[5]
# 		line = line[0:2]
# 		hours[line] = hours.get(line,0)+1

# for hour,freq in hours.items():
# 	tempList.append((hour,freq))
# 	tempList = sorted(tempList)

# for tup in tempList:
# 	print(tup[0],tup[1])