# Name: Osyczka2
import random
import math

def objfun1(a,b,c,d,e,f):
	x = -1*(25*(a-2)**2+(b-2)**2+(c-1)**2*(d-4)**2+(e-1)**2)
	return x
	
def objfun2(a,b,c,d,e,f):
	x = a**2 + b**2 + c**2 + d**2 + e**2 + f**2
	return (x-2)**2
	
def passConstraints(a,b,c,d,e,f):
	cOne = 0 <= a + b - 2
	cTwo = 0 <= 6 - a - b
	cThree = 0 <= 2 - b + a
	cFour = 0 <= 2 - a + 3*b
	cFive = 0 <= 4 - (c - 3)**2 - d
	cSix = 0 <= (e - 3)**3 + f - 4
	return cOne and cTwo and cThree and cFour and cFive and cSix
	
# Come back and make the variable generation work
# a & b & f 0,10
# c & e 1,5
# d 0,6
def generateVar(x, max, min):
	max = 10
	min = 0
	return x

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