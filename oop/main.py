
class Student():
	def __init__(self, name, age, grade):
		self.name = name
		self.age = age
		self.grade = grade

	def __str__(self):
		return f'name: {self.name}, age: {self.age}, grade:{self.grade}'

	def get_grade(self):
		return self.grade

class Course():
	def __init__(self, name, max_students):
		self.name = name
		self.max_students = max_students
		self.studentss = []

	def add_students(self,student):
		if len(self.studentss) < self.max_students:
			self.studentss.append(student)
			return True
		return False

	def get_average_grade(self):
		value = 0
		for student in self.studentss:
			value += student.get_grade()
		if len(self.studentss) > 0:
			return value / len(self.studentss)
		print('ther is no students')

	def get(self):
		print('all students is below\n')
		for x in self.studentss:
			print(f'{x.name} is {x.age} yo grade {x.grade}')

	def __str__(self):
		return self.name

student1 = Student('Kutman',21, 3)
student2 = Student('Askat',21, 79)
student3 = Student('Ayar', 20, 84)

print(student1)
print(student3)
print(student2)

couse = Course('math',30)

couse.add_students(student1)
couse.add_students(student2)
couse.add_students(student3)

print(couse.get_average_grade())