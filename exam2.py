import pandas as pd

class StudentMarks:
	def __init__(self, filename):
		# Read the CSV file using pandas and store in a DataFrame
		self.data = pd.read_csv(filename)
		# Add a new column 'Mean Mark' calculated as 0.4 * 'CC' + 0.6 * 'Exam'
		self.data['Mean Mark'] = 0.4 * self.data['CC1'] + 0.6 * self.data['Exam']
	def summarise(self):
		# Find the highest and lowest mean marks
		highest_mean = self.data['Mean Mark'].max()
		lowest_mean = self.data['Mean Mark'].min()
		# Find the corresponding student names
		highest_student = self.data[self.data['Mean Mark'] == highest_mean]
		lowest_student = self.data[self.data['Mean Mark'] == lowest_mean]
		# Print the results
		print(f"Highest Ranked Student :\n {highest_student}")
		print(f"Lowest Ranked Student :\n {lowest_student}")
	def infostudent(self, name):
		student_info = self.data[cl.data['First name']==name]
		print(student_info)

	def classmean(self):
		# Calculate the class mean mark
		class_average = self.data['Mean Mark'].mean()
		print(f"Class Mean Mark: {class_average:.2f}")
cl=StudentMarks('students.csv')
cl.summarise()
cl.classmean()
cl.infostudent('AFRIT')
