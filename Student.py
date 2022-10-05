import time
import sys
#Student class
class Student:
    #The student constructor class.
    def __init__(self,id,fname, sname, email,major):
        #Student class attributes
        self.Id = id
        self.fname = fname
        self.sname = sname
        self.email = email
        self.Major = major
#This method writes into a file
def writeToFile(fileName,student):
    #Open the file
    file = open(fileName,'w')
    #Write into the file, line by line.
    for i in range(len(student)):
        #Write the student's details into the file.
        file.write(str(student[i].Id) + " " + str(student[i].fname) +
                   " " + str(student[i].sname) + " " + str(student[i].email) + " " + str(student[i].Major))
#The selection sort method
def selectionSort1(students):
    #Sort the file named students using Selection sort
    for index in range(len(students)):
        min_index = index
        for j in range(index + 1, len(students)):
            #Sort based on id.
            if students[j].Id <  students[index].Id:
                #Swap the element index accordingly.
                min_index = j
#Swap the elements accordingly
        (students[index],students[min_index]) = (students[min_index], students[index])
        #Write the result to the file
    writeToFile('DbSelectionSortId.txt',students)
#Selection sorting using names instead of ids
def selectionSort2(students):
    for index in range(len(students)):
        min_index = index
        for j in range(index + 1, len(students)):
            if students[j].fname <  students[index].fname:
                min_index = j

        (students[index],students[min_index]) = (students[min_index], students[index])
    writeToFile('DbSelectionSortName.txt', students)

#insertion sort using Student's id
def insertionSort(student):
    for i in range(1,len(student)):
        #Get a comparing key
        key = student[i]
        #Get the previous element
        j = i - 1
        while j >= 0 and key.Id < student[j].Id:
            student[j + 1] = student[j]
            j -= 1
        student[j + 1 ] = key
        #Write into the file
    writeToFile('DbinsertionSortId.txt',student)
#Sort using student's name
def insertionSort1(student):
    for i in range(1,len(student)):
        #Get a comparing key
        key = student[i]
        #Get the previous element
        j = i - 1
        while j >= 0 and key.fname < student[j].fname:
            student[j + 1] = student[j]
            j -= 1
        student[j + 1 ] = key
        #Write into a file.
    writeToFile('DbInsertionSortName.txt', student)
#BubbleSort using Student's Id.
def bubbleSort(student):
    n = len(student)

    # Traverse through all array elements
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if student[j].Id > student[j + 1].Id:
                student[j], student[j + 1] = student[j + 1], student[j]
    writeToFile('DbBubbleSort.txt', student)
#BubbleSort using student's name
def bubbleSort1(student):
    n = len(student)

    # Traverse through all array elements
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if student[j].fname > student[j + 1].fname:
                student[j], student[j + 1] = student[j + 1], student[j]
    writeToFile('DbInsertionSortName.txt',student)

#Helper method for the MergeSort using Merge for Student's Id. It Merges the two subarrays.
def merge(student, left, medium, right):
    #the left size of the subarray
    n1 = medium - left + 1
    #The right size of the subarray
    n2 = right - medium

    # create temporary arrays
    L = [0] * (n1)
    R = [0] * (n2)

    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = student[left + i]

    for j in range(0, n2):
        R[j] = student[medium + 1 + j]

    # Merge the temp arrays back into arr[l..r]
    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = left  # Initial index of merged subarray

    while i < n1 and j < n2:
        if L[i].Id <= R[j].Id:
            student[k] = L[i]
            i += 1
        else:
            student[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        student[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        student[k] = R[j]
        j += 1
        k += 1


# l is for left index and r is right index of the
# sub-array of arr to be sorted

#Main MergeSort function
def mergeSort(arr, l, r):
    if l < r:
        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = l + (r - l) // 2

        # Sort first and second halves
        mergeSort1(arr, l, m)
        mergeSort1(arr, m + 1, r)
        merge(arr, l, m, r)
    writeToFile('DbMergeSort.txt', arr)

#Helper function for the Mergesort using Student's name
def merge1(student, left, medium, right):
    n1 = medium - left + 1
    n2 = right - medium

    # create temporary arrays
    L = [0] * (n1)
    R = [0] * (n2)

    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = student[left + i]

    for j in range(0, n2):
        R[j] = student[medium + 1 + j]

    # Merge the temp arrays back into arr[l..r]
    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = left  # Initial index of merged subarray

    while i < n1 and j < n2:
        if L[i].fname <= R[j].fname:
            student[k] = L[i]
            i += 1
        else:
            student[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        student[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        student[k] = R[j]
        j += 1
        k += 1
#Main MergeSort function for the array using the Student's Id
def mergeSort1(arr, l, r):
    if l < r:
        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = l + (r - l) // 2

        # Sort first and second halves
        mergeSort1(arr, l, m)
        mergeSort1(arr, m + 1, r)
        merge1(arr, l, m, r)
    writeToFile('DbMergeSort1.txt',arr)
#Function that reads the Text files
def readtxtFiles():
    students = []
    file = open('Database.txt','r')
    #Read the file and store it in the array
    i = 20
    while i > 0:
        line = file.readline().split(" ")
        print(line)
        studen = Student(line.__getitem__(0),line.__getitem__(1),line.__getitem__(2),line.__getitem__(3),line.__getitem__(4))
        students.append(studen)
        i -=1
    return students
#get the student data into a list
students = readtxtFiles()
#Sorting using Id
print("Sorting using Id")
#Time before the function is executed.
before = time.time()
#Get the Memory size occupied by the Function
size = sys.getsizeof(selectionSort1(students))
#Time after the function is executed.
after = time.time()
#Get the time difference
diff = after - before
#print the differences and repeat the process for each sorting algorithm
print("-> Selection Sort takes: " + str(diff) + " ms" + " and space of: " + str(size))
before = time.time()
size = sys.getsizeof(bubbleSort(students))
after = time.time()
diff = after - before
print("-> Bubble Sort takes: " + str(diff) + " ms" + " and space of: " + str(size))
before = time.time()
size = sys.getsizeof(insertionSort(students))
after = time.time()
diff = after - before
print("-> Insertion Sort takes: " + str(diff) + " ms" + " and space of: " + str(size))
before = time.time()
n = len(students) - 1
size = sys.getsizeof(mergeSort(students, 0, n))
after = time.time()
diff = after - before
print("->Merge Sort takes: " + str(diff) + " ms" + " and space is: " + str(size))
print
#Sorting using the fname
print("----Using Fname for sorting.")
before = time.time()
size = sys.getsizeof(insertionSort1(students))
after = time.time()
diff = after - before
print("-> Insertion Sort takes: " + str(diff) + " ms" + " and space of: " + str(size) )
before = time.time()
size = sys.getsizeof(selectionSort2(students))
after = time.time()
diff = after - before
print("-> Selection Sort takes: " + str(diff) + " ms" + " and space of: " + str(size))
before = time.time()
size = sys.getsizeof(bubbleSort1(students))
after = time.time()
diff = after - before
print("-> Bubble Sort takes: " + str(diff) + " ms" + " and space " + str(size))
before = time.time()
size = sys.getsizeof(mergeSort1(students,0, n))
after = time.time()
diff = after - before
print("-> MergeSort takes: " + str(diff) + " ms" + " and space " + str(size))
