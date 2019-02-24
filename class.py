class Person:
	name = " "
	age = 0
	number = 0
	
	def __init__(self, name, age, number):
		self.number = number
		self.name = name
		self.age = age

	#def set(self, name, age, number):
	#	self.name = name
	#	self.age = age
	#	self.number = number

class student(Person):
	course = 0

	def set(self, name, age, course, number):
		self.name = name
		self.age = age
		self.number = number
		self.course = course

freshman = student("Name", 15, 0)
#freshman.course = 2
freshman.set ("Makel", 19, 2, 0)
print  ("Name: " + freshman.name + '\n' + "Age: " + str(freshman.age) + '\n' + "Course " 
	+ str(freshman.course) + '\n' + "Number " + str(freshman.number))

David = Person ("David", 19, 0)
#David.set ("Давид", 19, 380957013329)
print ('\n' "Name: " + David.name + '\n' + "Age: " + str(David.age)  + '\n' + "Number: "
 + str(David.number))

ivan = Person ("Vano", 18, 0)
#ivan.set ("Иван", 18, 380502340415)
print ('\n' "Name: " + ivan.name + '\n' + "Age: " + str(ivan.age) + '\n' + "Number: " 
	+ str(ivan.number))


#class Some:
#   pass # Класс может ничего не возвращать
#obj_new = Some() # Создание объекта
#obj_second = Some() # Создание 2 объекта
