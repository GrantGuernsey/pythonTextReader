

import math

#variable declerations
grades_file = open("HW3p1.txt","r")
studentID = []
finalGrade = []
letterGrade = []
AsBs = 0
lowestA = 100
lowAID = 0
hwAverage = 0
BandD = 0
standDev = []

#running through the text and putting each of the things in the text doccument into their own list
#this also servers as a place to start the calcualtions for taks 2 of the homework
for line in grades_file:
    k = line.split()
    if k[0] != "ID":
        studentID.append(k[0])
        gradeCalculation = round((float(k[1]) * 0.15) + (float(k[2]) * .2) + (float(k[3]) * .25) + (float(k[4]) * .2) + (float(k[5]) * .2))
        finalGrade.append(gradeCalculation)
        if gradeCalculation >= 90:
            letterGrade.append("A")
            AsBs += 1
            if float(k[5]) <= lowestA: #this is finding the student with an A that has the lowest final test grade
                lowestA = float(k[5])
                lowAID = k[0]
        elif gradeCalculation >= 80:
            letterGrade.append("B")
            AsBs +=1
        elif gradeCalculation >= 70:
            letterGrade.append("C")
        elif gradeCalculation >= 60:
            letterGrade.append("D")
            hwAverage += float(k[2])
            BandD += 1
            standDev.append(float(k[2]))
        else:
            letterGrade.append("F")
            hwAverage += float(k[2])
            BandD += 1
            standDev.append(float(k[2]))



grades_file.close()

my_new = open("CourseGrade.txt","w")
my_new.write("ID    Course Average    Letter Grade\n")
 
#this is pritning all of the values into a formatted manner into the new COurrseGrade.txt
for x in range(len(studentID)):
    if( x / 9 < 1):
        my_new.write("{0}             {1}              {2}\n".format(studentID[x], finalGrade[x], letterGrade[x]))
    elif(x / 99 < 1):
        my_new.write("{0}            {1}              {2}\n".format(studentID[x], finalGrade[x], letterGrade[x]))
    elif(x/999 < 1):
        my_new.write("{0}           {1}              {2}\n".format(studentID[x], finalGrade[x], letterGrade[x]))
    else:
        my_new.write("{0}          {1}              {2}\n".format(studentID[x], finalGrade[x], letterGrade[x]))
my_new.close()

#calculation for 2.1
AsBs /= len(finalGrade)
AsBs *= 100
#calculation for 2.3
hwAverage /= BandD

#calculation for 2.4
n = len(standDev)
standardDeviation = (sum([((x - hwAverage) ** 2) for x in standDev]) / n) ** 0.5

#print statement for all of task 2
print("The percentage of students that got A's or B's in the class is {0:.2f}%".format(AsBs))
print("The lowest final grade for a student that received an A was {0:.2f} accomplished by student ID {1}".format(lowestA,lowAID))
print("The overall homework average for students that received a D or an F in the course is {0:.2f}".format(hwAverage))
print("The standard deviation of the homework grades for all students that received a D or an F is {0:.2f}".format(standardDeviation))

