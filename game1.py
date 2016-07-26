from random import choice
from string import ascii_uppercase

def upperCaseRandomString(size):
	return (''.join(choice(ascii_uppercase) for i in range(size)))

def takeInput(size):
	while True:
		userString = raw_input("Please guess a word of length " + str(size) + ": ").upper() 
		if len(userString) >= size:
			break
	return userString

def appendWithCharacters(myString, ch, size):
	tmp = size - len(myString)
	for i in range(0,tmp):
		myString = myString + ch
	return myString

def countExactMatches(testString, userString, size):
		exactMatches = 0
		checkString = ""
		randomCheckString = ""
		for i in range(0,size):
			if testString[i] == userString[i]:
				exactMatches = exactMatches + 1
			else:
				checkString = checkString + userString[i]
				randomCheckString = randomCheckString + testString[i]
		return exactMatches ,checkString, randomCheckString

def rearrangingRandomString(randomCheckString):
	randomCheckString = "".join(set(randomCheckString))
	randomCheckString = appendWithCharacters(randomCheckString, '-', size)
	return randomCheckString

def countWrongPlaceMatches(checkString, randomCheckString, size):
	matchesWithWrongPlace = 0
	for i in range(0,size):
		for j in range(0,size):
			if checkString[i] == randomCheckString[j]:
				matchesWithWrongPlace = matchesWithWrongPlace + 1
	return matchesWithWrongPlace

size = int(raw_input("Please provide the size of the String: "))
testString = upperCaseRandomString(size)

while True: 
	userString = takeInput(size)
	exactMatches, checkString, randomCheckString = countExactMatches(testString, userString, size)
	if exactMatches == size:
		print "You won the game."
		break
	checkString = appendWithCharacters(checkString, '_', size)
	randomCheckString = rearrangingRandomString(randomCheckString)

	print "Number of characters that are correct, but in the wrong place are " + str(countWrongPlaceMatches(checkString, randomCheckString, size)) + '.'
	print "Number of characters that are correct and in the correct place are " + str(exactMatches) + '.'