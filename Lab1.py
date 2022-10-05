import random
import time
#Declare the List and the Dictionary respectively
import time
finitem = 0
list = []
dic = dict()
#Get the random numbers and add them to the list and dictionary
for i in range(1500):
    ran = random.randrange(1, 10000)
    list.append(ran)
    dic[i] = ran
    finitem = ran
#Start Time
tic = time.time()
#Print the elements from the list

print (list)
#End time
toc = time.time()
#Get the time difference
print ("For list:" + "\t")
diff = (toc - tic) * 1000
print ("Ellapsed time: " + str(diff) + " Milliseconds")
tic = time.time()
#Print the elements from the list
print(dic)
#End time
toc = time.time()
print ("For Dict")
diff = (toc - tic) * 1000
print ("Ellapsed time: " + str(diff) + " Milliseconds")
#Start Time
tic = time.time()
#Find the elements from the list
ranitem = random.randrange(1,10000)
#finitem is used to avoid using the try and catch and also to avoid exception
#being thrown. This ensures the same value returned for both dictionary and the
#list.
itemindex = list.index(finitem)
#End time
toc = time.time()
#Get the time difference
print ("For list Find:")
diff = (toc - tic) * 1000
print ("Ellapsed time: " + str(diff) + " Milliseconds")
#Start Time
ranitem = random.randrange(1,10000)
tic = time.time()
#Find the elements from the list

item = dic.get(finitem)
#End time
toc = time.time()
#Get the time difference
print ("For dic Find:")
diff = (toc - tic) * 1000
print ("Ellapsed time: " + str(diff) + " Milliseconds")
tic = time.time()
ranitem = random.randrange(1,10000)
list.append(ranitem)
print(list)
toc = time.time()
print ("For append list:" )
diff = (toc - tic) * 1000
print ("Ellapsed time: " + str(diff) + " Milliseconds")
tic = time.time()
ranitem = random.randrange(1,10000)
dic[len(dic) + 1] = ranitem
print (dic)
toc = time.time()
print ("For append Dic:")
diff = (toc - tic) * 1000
print ("Ellapsed time: " + str(diff) + " Milliseconds")


#For delete Operations
tic = time.time()
ranitem = random.randrange(1,10000)


list.remove(finitem)

toc = time.time()
diff = (toc - tic) * 1000
print ("For delete Operations for List:")
print ("Ellapsed time: " + str(diff) + " Milliseconds")
#For dic
tic = time.time()
ranitem = random.randrange(1,10000)

del dic[33]

toc = time.time()
diff = (toc - tic) * 1000
print ("For delete Operations for dic:")
print ("Ellapsed time: " + str(diff) + " Milliseconds")