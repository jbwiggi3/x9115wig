# Name: Schaffer
# Objective functions: x^2 ; (x-2)^2
# n: 1
# Variable bounds: -10^5 <= x 10^5
# Comments: convex
import random
import math

globalmax = 0
globalmin = 0

def objfun1(x):
	return x**2
	
def objfun2(x):
	return (x-2)**2

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
	if k < 27:
		print ", 00" + str(k-26) + ", :" + str(eb) + " " + text
	elif k < 126:
		print ", 0" + str(k-26) + ", :" + str(eb) + " " + text
	else:
		print ", " + str(k-26) + ", :" + str(eb) + " " + text

def mutate(s):
	newval = s
	high = 100000
	low = -100000
	some = (high - low)*.05
	newval = newval - some + 2*some*random.random()
	newval = low + (newval - low)%(high - low)
	return newval

def sa():
	print "Running Schaffer"
	k = 1
	kmax = 1000
	maxlives = 500
	lives = maxlives
	currentline = "!"
	s = 0
	e = energy(objfun1(s),objfun2(s))
	sb = s
	eb = e
	while True:
		symbol = "."
		k += 1
		t = (k/(kmax/1.0))
		sn = mutate(s)
		en = energy(objfun1(sn),objfun2(sn))
		#print str(p(e,en,t)) + " " + str(t)
		if en < e:
			symbol = "+"
			s,e = sn,en
			if en > eb:
				sb,eb = sn,en
				symbol = "!"
		elif p(e,en,t) < random.random():
			#print str(p(e,en,t)) + " " + str(random.random()) + " " + str(p(e,en,t) < random.random())
			#print str(p(e,en,t)) + " " + str(e) + " " + str(en) + " " + str(t)
			symbol = "?"
			s,e = sn,en
		if k % 25 == 1:
			printcurrentline(currentline,k,eb)
			currentline = ""
		else:
			lives -= 1
			if symbol == "!" or symbol == "+":
				lives = maxlives
			if lives < 1:
				return "Ran out of lives at iteration " + str(k) + "\nBest was: " + str(sb) + "\nEnergy: " + str(eb)
			if k > kmax:
				return "Reached Kmax"+ "\nBest was: " + str(sb) + "\nEnergy: " + str(eb)
				
		currentline += symbol
			
def generateGlobals():
	count = 0
	s = 0
	eb = objfun1(s) + objfun2(s)
	ew = eb
	for x in range(1000):
		count += 1
		s = mutate(s)
		e = objfun1(s)+objfun2(s)
		if e > eb:
			eb = e
		if e < ew:
			ew = e
	global globalmax
	global globalmin
	globalmax = eb
	globalmin = ew
		
print "################sa Demo##############"
generateGlobals()
print sa()