import sys
#two arrays for the student and their scores.
studentList = ['Jack','Joe','Harry']
marks = [88, 56, 80]



#iterating though the students 
def studentAverage(studentList,marks):
    for i in range(len(studentList)):
        print(studentList[i], end=" ")
        mark = marks[i]
        #comparing student score to class average
        if mark >= classAverage(marks):
            print("is to be congratulated")
        else:
            print('\n')
            
    pass


#simple function to obtain the average of an int array
def classAverage(y):
    total = 0
    for i in marks:
        total += i
    avrg = total / len(marks)
    return(int(avrg))
        

studentAverage(studentList,marks)
