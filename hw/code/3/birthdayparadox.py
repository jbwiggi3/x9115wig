import random
#this is exercise 8 from 10.15's Exercises
def has_duplicates(t):
	t2 = t[:]
	t2.sort()
	temp = t2[0]
	flag = True
	for element in t2:
		if flag:
			flag = False
		else:
			if element == temp:
				return True
			else:
				temp = element
	
	return False
	
list1 = [1,2,3,4]
list2 = [1,1,2,3,4]
list3 = [1,2,3,4,1]
list4 = [1,2,4,3,4,5]
list5 = [5,1,2,3,4,5]
print "The following is for part 1 of exercise 8"
print "For the list " + str(list1)
print has_duplicates(list1)
print "For the list " + str(list2)
print has_duplicates(list2)
print "For the list " + str(list3)
print has_duplicates(list3)
print "For the list " + str(list4)
print has_duplicates(list4)
print "For the list " + str(list5)
print has_duplicates(list5)

print "The following is for part 2 of exercise 8"

def generateClassroom():
	t = []
	for i in range(23):
		t.append(random.randint(0,365))
	return t
	
def simulation(iterations):
	numOfDuplicates = 0;
	for i in range(iterations):
		temp = generateClassroom()
		if has_duplicates(temp):
			numOfDuplicates += 1
	return numOfDuplicates/(iterations/1.0)

iterations = 10
for i in range(5):
	print "After " + str(iterations) + " classroom generations the " + str(simulation(iterations))
	iterations *= 10
