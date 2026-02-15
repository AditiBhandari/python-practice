### MODULE 3 ASSIGNMENT: WRITE HELLO WORLD
# print("hello world")



### MODULE 4 ASSIGNMENT: PAY CALCULATOR
# hrs = input("Enter Hours:")
# rate = input("Enter rate:")

# grossPay = float(hrs)*float(rate)
# print("Pay: " + str(grossPay))



### MODULE 5 ASSIGNMENT: OVERTIME PAY CALCULATOR
# hrs = float(input("Enter hours: "))
# rate = float(input("Enter rate: "))

# if hrs < 40:
# 	print(hrs,rate)
# else:print((40*rate)+((hrs-40)*(rate*1.5)))



### MODULE 6 ASSIGNMENT: BUILD FUNCTIONS
# hours = float(input("Enter hours: "))
# rate = float(input("Enter rate: "))

# def computepay (h, r):
# 	if h < 40:
# 		return h * r
# 	else:
# 		return (40*r)+((h-40)*(r*1.5))

# p = computepay(hours,rate)
# print("Pay",p)



### MODULE 7 ASSIGNMENT: FIND THE LARGEST AND SMALLEST NUMBERS
# largest = None
# smallest = None

# while True:
# 	userNumber = input("Enter an integer: ")
# 	if userNumber == "done":
# 		break
# 	else:
# 		try:
# 			intUN = int(userNumber)
			
# 			if largest is None:
# 				largest = intUN
# 				smallest = intUN
# 			elif largest < intUN:
# 				largest = intUN
# 				if smallest > intUN:
# 					smallest = intUN
# 			else:
# 				if smallest > intUN:
# 					smallest = intUN
# 				continue
# 		except:
# 			print("Invalid input")

# print("Maximum is", largest)
# print("Minimum is", smallest)
