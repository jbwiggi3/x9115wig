class Employee:
	""" Initialized with name and age """
	def __init__(self, name, age):
		self.name = name
		self.age = age
	
	""" Pretty prints name and age """
	def __repr__(self):
		return "Name: " + self.name + "  Age: " + str(self.age)
		
	""" This method allows employees to be sorted by age """
	def __lt__(self, other):
		if self.age < other.age:
			return True
		return False
		
jeff = Employee("Jeffery",23)
bob = Employee("Robert", 25)
kim = Employee("Kimberly", 71)

t = [bob, kim, jeff]
print "List pre sort:"
print str(t[0])
print str(t[1])
print str(t[2])
print ""
t.sort()
print "List post sort:"
print str(t[0])
print str(t[1])
print str(t[2])