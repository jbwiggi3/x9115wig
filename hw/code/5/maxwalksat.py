# Name: Osyczka2
import random
import math

globalmax = 0
globalmin = 0

def objfun1(s):
	a,b,c,d,e,f = s
	x = -1*(25*(a-2)**2+(b-2)**2+(c-1)**2*(d-4)**2+(e-1)**2)
	return x
	
def objfun2(s):
	a,b,c,d,e,f = s
	x = a**2 + b**2 + c**2 + d**2 + e**2 + f**2
	return (x-2)**2
	
def passConstraints(s):
	a,b,c,d,e,f = s
	cOne = 0 <= a + b - 2
	cTwo = 0 <= 6 - a - b
	cThree = 0 <= 2 - b + a
	cFour = 0 <= 2 - a + 3*b
	cFive = 0 <= 4 - (c - 3)**2 - d
	cSix = 0 <= (e - 3)**3 + f - 4
	return cOne and cTwo and cThree and cFour and cFive and cSix
	

def generateVar(max, min):
	range = (max - min)
	newval = range*random.random() + min
	newval = min + (newval - min)%(max - min)
	return newval

def energy(f1, f2):
	#need to run Schaffer 100 times to compute
	global globalmax
	global globalmin
	max = globalmax
	min = globalmin
	return (((f1+f2)-min) / (max - min))
	
def p(oldenergy, newenergy, t):
	return math.exp(((oldenergy*1.0) - (newenergy*1.0))/(t*1.0))
	
def printcurrentline(text,k,eb):
	if k < 25:
		print ", 00" + str(k) + ", :" + str(eb) + " " + text
	elif k < 100:
		print ", 0" + str(k) + ", :" + str(eb) + " " + text
	else:
		print ", " + str(k) + ", :" + str(eb) + " " + text

def generateNewVector():
	a = generateVar(0,10)
	b = generateVar(0,10)
	c = generateVar(1,5)
	d = generateVar(0,6)
	e = generateVar(1,5)
	f = generateVar(0,10)
	return a,b,c,d,e,f


def mutateRandom(s,partToMutate):
	newS = generateNewVector()
	mutant = list(s)
	mutant[partToMutate] = newS[partToMutate]
	while not passConstraints(mutant):
		newS = generateNewVector()
		mutant = list(s)
		mutant[partToMutate] = newS[partToMutate]
	return mutant

# Come back and make the variable generation work
# a & b & f 0,10
# c & e 1,5
# d 0,6
def mutateTowardMax(s,partToMutate):
	max = 0
	min = 0
	if partToMutate == 0 or partToMutate == 1 or partToMutate == 5:
		max = 10
		min = 0
	elif partToMutate == 2 or partToMutate == 4:
		max = 5
		min = 1
	else:
		max = 6
		min = 0
	
	mutant = list(s)
	bestMutant = list(mutant)
	bestMutantEnergy = energy(objfun1(mutant),objfun2(mutant))
	for i in range(10):
		mutant[partToMutate] += (max-min)/10
		#Wrapping
		mutant[partToMutate] = min + (mutant[partToMutate] - min)%(max - min)
		if passConstraints(mutant):
			newEnergy = energy(objfun1(mutant),objfun2(mutant))
			if newEnergy > bestMutantEnergy:
				bestMutantEnergy = newEnergy
				bestMutant = list(mutant)
	return mutant

def maxWalkSat():
	print "Running Max Walk Sat"
	p = .5
	maxTries = 1000
	maxChanges = 100
	threshold = 1.0
	currentline = "!"
	s = generateNewVector()
	while not passConstraints(s):
		s = generateNewVector()
	e = energy(objfun1(s),objfun2(s))
	sb = s
	eb = e
	
	for i in range(maxTries):
		symbol = "."
		sn = generateNewVector()
		while not passConstraints(sn):
			sn = generateNewVector()
		en = energy(objfun1(sn),objfun2(sn))
		for j in range(maxChanges):
			if en > threshold:
				printcurrentline(currentline + symbol,i,eb)
				return "Threshold reached at iteration: "+ str(i) + "\nBest was: " + str(sb) + "\nEnergy: " + str(en)
			
			partToMutate = random.randint(0,5)
			if p < random.random():
				symbol = "."
				sn = mutateRandom(sn,partToMutate)
			else:
				sn = mutateTowardMax(sn,partToMutate)
			en = energy(objfun1(sn),objfun2(sn))
		if en > eb:
			sb,eb = sn,en
			s,e = sn,en
			symbol = "!"
		elif en < e:
			s,e = sn,en
			symbol = "+"		
		if i % 25 == 0 and i != 0:
			printcurrentline(currentline,i,eb)
			currentline = ""
		currentline += symbol
		
	return "Finished MaxWalkSat"+ "\nBest was: " + str(sb) + "\nEnergy: " + str(eb)
				

def prints(s):
	a,b,c,d,e,f = s
	print a
	print b
	print c
	print f
	exit()
			
def generateGlobals():
	count = 0
	s = generateNewVector()
	while not passConstraints(s):
		s = generateNewVector()
	eb = objfun1(s) + objfun2(s)
	ew = eb
	for x in range(10000):
		count += 1
		s = generateNewVector()
		while not passConstraints(s):
			s = generateNewVector()
		e = objfun1(s)+objfun2(s)
		if e > eb:
			eb = e
		if e < ew:
			ew = e
	global globalmax
	global globalmin
	globalmax = eb
	globalmin = ew		
		
print "################MaxWalkSat Demo##############"
generateGlobals()
maxTries = 1000
maxChanges = 100
threshold = 1.0
p = .5
print maxWalkSat()
print "With parameters:\n  Max-Tries: " + str(maxTries) + "\n  Max-Changes: " + str(maxChanges) + "\n  Threshold: " + str(threshold) + "\n  p: " + str(p)
