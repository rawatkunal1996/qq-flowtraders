##################################################################################
##################################################################################
## Template file for problem 1. 						##
## First, fill in your answer logic below					##
##################################################################################
#                                LOGIC GOES BELOW                     		#
##################################################################################
#We require 2 variables a and b (let). b to store the current generated random number and a to store the previously generated random number.
#Now initialize a variable e=0 which denotes the expected values. Using while loop we keep on generating random values and if b>a, then we update 
#the value of e by adding e=e+b*1/6. When b<=a, we simply exit the while loop and return the expected value e from the function.
#
#
##################################################################################
##################################################################################
## You have to fill in two functions BELOW 					##
## Both take in input n = number of sides in the die 				##
## 										##									##
## 1. findSumDieRoll(n)	: Return expected value of sum 				##
## 2. findNumberOfRolls(n)  : Return expected value of number of rolls 		##
## 										##									##
## For both, you only have to fill in the math function where indicated     	##
## 										##									##
## You can run this template file to see the output of your functions       	##
## for a 6 sided die.								##
## Simply run: `python problem1_template.py`                            	##
## You should see the output printed once your program runs.                	##
##                                                                          	##
## DO NOT CHANGE ANYTHING ELSE BELOW. ONLY FILL IN THE LOGIC.      		##
##                                                                          	##
## Good Luck!                                                               	##
##################################################################################
##################################################################################


def findSumDieRoll(n):
	##################################
	##          FILL ME IN          ##
	##################################
	# n is a float
	sumRolls = n/2 # Replace me with your answer

	return round(sumRolls, 2)

def findNumberOfRolls(n):
	##################################
	##          FILL ME IN          ##
	##################################
	# n is a float
	numRolls = n/2	# Replace me with your answer

	return round(numRolls, 2)

if __name__ == "__main__":
	numberOfSides = 6.0
	sumOfRolls = findSumDieRoll(numberOfSides)
	numberOfRolls = findNumberOfRolls(numberOfSides)
	print('For a %i-sided die, expected value of sum: %.2f and number of rolls: %.2f'%(numberOfSides, sumOfRolls, numberOfRolls))
