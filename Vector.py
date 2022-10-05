import array as arr
class Vector:
#Create a constructor
    def __init__(self):
        self.data = [2]
    #This function retuns the length of the Vector.
    def length (self):
        return len(self.data)
#This function returns true if the item is found in the vector, otherwise, false is returned
    def __contains__(self, item):
        return self.__contains__(item)
    #This function returns the item at the specified index
    def __getitem__(self, item):
        return self.__getitem__(item)
    #This function sets the element at the key to be the given value
    def __setitem__(self, key, value):
        self.__setitem__(key, value)
    #This function appends the element at the end of this vector
    def append(self, item):
        self.data.append(item)
    #This function inserts the element into the Vector.
    def insert(self,index, item):
        self.data.insert(index, item)
    #This function removes the item from the Vector
    def remove(self, item):
       return self.data.remove(item)
    #This function returns the index of the supplied item
    def indefOf(self,item):
        index = 0
        #Loop throught the Array for this vector
        for i in range(len(self.data)):
            if i == self.data[i]:
                index = i
        return index
    #This function extends the vector by adding the elements of
    #the new Vector to this Vector
    def extend(self, Vector):
        self.data.extend(Vector)
    #This function returns a slice of the vector from the defined limit
    def subVector(self, start, to):
        if( start < 0 or to > len(self.data)):
            print("The start and to needs to be within the Valid range.")
        else:
            vect = Vector()
            #Slice the vector accordingly
            for i in self.data[start:to]:
                vect.insert(i,self.data[i])
            return vect
#The driver method to test the functions.
if __name__ == "__main__":
    vect = Vector()
    print("Insert Functionality.")
    vect.insert(0,1)
    vect.insert(1, 2)
    vect.insert(2, 3)
    vect.insert(3,5)
    print("Length Functionality")
    print("The length is:")
    print(vect.length())
    print(vect.data)
    print("Subvector:")
    print( vect.subVector(0,1).data)