#1

%matplotlib inline 
import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
temperature = [35, 40, 30, 32, 39, 42, 40, 38, 39, 39]

fig = plt.figure()

plt.plot(days, temperature, color = 'blue', label = "Weather Data")

plt.xlabel('Dates')
plt.ylabel('Temperature(°C)')
plt.title('Weather Report')
plt.legend()
plt.show()

#2
%matplotlib inline
import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
temperature = [35, 40, 30, 32, 39, 42, 40, 38, 39, 39]

fig = plt.figure()

plt.plot(days, temperature, color = 'blue', label = "Weather Data")

plt.xlabel('Dates')
plt.ylabel('Temperature(°C)')
plt.xticks(range(1,11))
plt.yticks(range(30,51))
plt.title('Weather Report')
plt.legend()
plt.show()

#3
%matplotlib inline
import matplotlib.pyplot as plt

age = [40, 42, 32, 35, 30, 33, 26, 30, 50]
blood_pressure = [100, 110, 105, 109, 100, 102, 76, 98, 120]

fig = plt.figure()

plt.scatter(age, blood_pressure)

plt.xlabel('Ages')
plt.ylabel('Blood Pressure')
plt.title('Patients Blood Pressure Report')

plt.show()

#4
%matplotlib inline
import matplotlib.pyplot as plt

names = ['Alex', 'Bert', 'Carl', 'Dave', 'Elly', 'Fran', 'Gwen', 'Hank', 'Ivan']
ages = [40, 42, 32, 35, 30, 33, 26, 30, 50]

fig = plt.figure()

plt.bar(names, ages,label = "Age")

plt.xlabel('Names')
plt.ylabel('Ages')

plt.title('Ages of different persons')
plt.legend()
plt.show()

#5
%matplotlib inline
import matplotlib.pyplot as plt

names = ['Alex', 'Bert', 'Carl', 'Dave', 'Elly', 'Fran', 'Gwen', 'Hank', 'Ivan']
ages = [40, 42, 32, 35, 30, 33, 26, 30, 50]

fig = plt.figure()

plt.bar(names, ages,label = "Age", width=0.2, color='pink')

plt.xlabel('Names')
plt.ylabel('Ages')

plt.title('Ages of different persons')
plt.legend()
plt.show()

#6
%matplotlib inline
import matplotlib.pyplot as plt

subjects = ['Science', 'Maths', 'Physics', 'Economics', 'History']
scores = [65, 85, 60, 80, 70]

fig = plt.figure(figsize=(10,9))

plt.pie(scores,labels=subjects, autopct='%1.2f%%') # display percentage on Pie chart
plt.title("Exam Score of a student")
plt.legend()
plt.show()