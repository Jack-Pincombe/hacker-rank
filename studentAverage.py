import sys

studentList = ['Jack','Joe','Harry']
marks = [88, 56, 80]




def studentAverage(studentList,marks):
    for i in range(len(studentList)):
        print(studentList[i], end=" ")
        mark = marks[i]
        if mark >= classAverage(marks):
            print("is to be congratulated")
        else:
            print('\n')
            
    pass



def classAverage(y):
    total = 0
    for i in marks:
        total += i
    avrg = total / len(marks)
    return(int(avrg))
        

studentAverage(studentList,marks)
