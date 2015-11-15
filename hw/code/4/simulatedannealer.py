# Name: Schaffer
# Objective functions: x^2 ; (x-2)^2
# n: 1
# Variable bounds: -10^5 <= x 10^5
# Comments: convex
import random
import math

def objfun1(x):
	return x**2
	
def objfun2(x):
	return (x-2)**2

def energy(f1, f2):
	#need to run Schaffer 100 times to compute
	max = 2001918
	min = 2
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
	high = 1000
	low = -1000
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
	currentline = ""
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
		if en > eb:
			sb,eb = sn,en
			s,e = sn,en
			symbol = "!"
		elif en < e:
			s,e = sn,en
			symbol = "+"
		elif p(e,en,t) < random.random():
			#print str(p(e,en,t)) + " " + str(e) + " " + str(en) + " " + str(t)
			s,e = sn, en
			symbol = "?"
		if k % 25 == 1:
			printcurrentline(currentline,k,eb)
			currentline = ""
		else:
			lives -= 1
			if symbol == "!" or symbol == "+":
				lives = maxlives
			if lives < 1:
				return "Ran out of lives"
			if k > kmax:
				return "Reached Kmax"
				
		currentline += symbol
			
		
		
print "################sa Demo##############"
'''count = 0
s = 0
eb = energy(objfun1(s),objfun2(s))
ew = eb
while True:
	count += 1
	s = mutate(s)
	e = energy(objfun1(s),objfun2(s))
	if e > eb:
		eb = e
	if e < ew:
		ew = e
	if count == 1000:
		print eb
		print ew
		exit()'''
print sa()