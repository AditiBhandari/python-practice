# fname = input("Enter file name: ")
# fh = open(fname, 'r')

# for line in fh:
# 	line = line.strip().upper()
# 	print(line)



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

# print("Average spam confidence: ",average)










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




# count = 0

# openFile = open("mbox-short.txt","r")

# for eachLine in openFile:
# 	if eachLine[count].startswith("From"):
# 		print("from")
# 		count = count + 1
# 	print(count)








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








# Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

# filename = open("mbox-short.txt","r")

# sendersList = dict()

# for line in filename:
# 	if line.startswith("From "):
# 		line = line.strip().split()[1]
# 		sendersList[line] = sendersList.get(line,0) + 1
# # print(sendersList)

# maxNum = None
# maxSender = None

# for cle,valuer in sendersList.items():
# 	if maxNum is None or valuer > maxNum:
# 		maxNum = valuer
# 		maxSender = cle
# print(maxNum,maxSender)




filename = open("mbox-short.txt","r")

hours = dict()
tempList = list()

for line in filename:
	if line.startswith("From "):
		line = line.strip().split()[5]
		line = line[0:2]
		hours[line] = hours.get(line,0)+1

for hour,freq in hours.items():
	tempList.append((hour,freq))
	tempList = sorted(tempList,reverse=True)[:6]

for tup in tempList:
	print(tup[0],tup[1])