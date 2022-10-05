import numpy as np
import random
class matrix:
    def __init__(self, array2D):
        # self.csv_file = csv_file
        self.array2D = array2D

    def load_from_csv(self, csv_file):
        # matrix from csv file:
        m = matrix('validfilename.csv')  # Read the file
        self.array2D = np.array(np.genfromtxt(m, delimiter=","))  # convert in 2d numPy array

        # transposed matirx:
        self.array2D = self.array2D.transpose()  # transpose it

        self.array2D = matrix(self.array2D).standardise()  # calling the standardise method

        # matrix.get_frequency_count() # calling the frequency count method

        return self.array2D

    def standardise(self):
        # standardize the matrix
        array = self.array2D
        shape = array.shape  # rows and columns of matrix
        # print(array,shape)
        standard_matrix = np.empty(shape, float)  # creating an empty matrix

        for i in range(shape[0]):  # no of rows
            for j in range(shape[1]):  # no of columns

                min_v = array[:, j].min()  # miminum value of j'th column
                max_v = array[:, j].max()  # maximum value of j'th column

                standard_matrix[i][j] = ((array[i][j]) - min_v) / (max_v - min_v)  # standardization formula
        self.array2D = standard_matrix
        return self.array2D

    def get_distance(self, other_matrix, weights, beta, i=None):  # other_matix = centroid

        os = np.array(self.array2D).shape  # shape of data_matrix calling this method
        ws = np.array(weights).shape  # shape of weights matrix

        data_matrix = self.array2D

        if (os[0] == 1) and (ws[0] == 1):
            # apply Weighted_distance function to calculate it

            d_matrix = Weighted_distance(self.array2D, other_matrix, weights, beta)

            return d_matrix

        elif (os[0] > 1) and (ws[0] == 1):
            # apply Weighted_distance function to calculate it

            d_matrix = Weighted_distance(self.array2D, other_matrix, weights, beta)

            return d_matrix

    def get_frequency_count(self):
        # gets frequency in form of array

        sh = self.array2D.shape  # gets the shape of array2D

        if (sh[1] == 1) or (len(sh) == 1):  # compares whether the array2D has 1 column or not

            dic = {}  # empty dictionary to store frequency of each value

            for i in self.array2D:  # parsing each element
                if i in dic:  # checks whther the element is present in the dictionary
                    dic[i] += 1  # increment the value of it by 1 if present
                else:
                    dic[i] = 1  # else assigns 1 to the element's value in dictionary

            freq_list = []  # empty list to store key, value pairs of freq dictionary

            for i in dic:  # parse each keys of dictionary
                freq_list.append([i, dic[i]])  # append the key and its frequncy into freq_list
            return freq_list

        else:
            pass  # if the condition isnt met then it doesnt do any thing


def get_initial_weights(m):
    lst = []
    su = round((m / 2), 2)
    m2 = su
    flag = True

    while flag == True:

        su = round((su - 0.9), 2)

        if su > 0.0:
            lst.append(0.9)
        else:
            lst.append(round(su + 0.9, 3))
            flag = False

    nlst = []
    v = []
    flg = True
    for i in range(len(lst)):

        if lst[i] == max(lst):
            temp = round(random.uniform(0.0, max(lst)), 2)
            te = round((lst[i] - temp), 2)
            nlst.extend((temp, te))
    if (len(nlst) == m) and (sum(nlst) < m2):
        if min(nlst) + lst[-1] <= 1:
            nlst[nlst.index(min(nlst))] = min(nlst) + lst[-1]

    elif (len(nlst) == m - 1) and (sum(nlst) < m2):
        nlst.append(lst[-1])

    if (len(nlst) > m) and (round(sum(nlst), 2) < m2):
        temp = np.sort(nlst)
        # print("temp", temp)
        temp[0] = temp[0] + temp[1]
        temp[1] = 0.0
        s = m2 - np.sum(temp)
        # print(s , "s1", m2)
        temp[1] = m2 - np.sum(temp)
        # print(temp[1])

    if (len(nlst) > m) and (round(sum(nlst), 2) == m2):
        flg = False
        temp = np.sort(nlst)
        temp[0] = temp[0] + temp[1]
        temp[1] = None
        for i in range(len(temp)):
            if np.isnan(temp[i]):
                i = i + 1
            else:
                v.append(temp[i])

    if flg == True:
        nw = np.array([nlst])
        return nw
    elif flg == False:
        np.random.shuffle(v)
        nw = v
        return nw


def Weighted_distance(data_matrix, other_matrix, weights, beta):  # function to implemet the weighted distance formula
    d_lst = []
    #     print("data_matrix ""\n", data_matrix,data_matrix.shape)
    #     print("other_matrix ""\n", other_matrix,other_matrix.shape)
    #     print("weights ""\n", weights , weights.shape)
    for d_row in data_matrix:  # gets each row in data_matrix
        d = 0  # set d after every row in d_row so that wwe have exact weighted distances
        for c_row in other_matrix:

            for i in range(len(d_row)):  # summition implementation using for loop
                d = d + (weights[0][i] ** beta) * ((np.absolute(d_row[i] - c_row[i])) ** beta)  # formula
        d_lst.append([round(d, 2)])

    return d_lst


def get_centroids(data_matrix, S, K):
    temparr = []
    for k in range(K):  # looping for the number of clusters

        rows = []  # inistailize an array to give the rows where c[k] == k

        for i in range(S.shape[0]):  # loop to iterate for S.shape[0] number of times
            if k == S[i][0]:  # if the value of S == k
                rows.append(data_matrix[i][:])  # append the said row of data_matrix to rows
        rows = np.array(
            rows).transpose()  # transpose the rows so that we can find the mean and median of the column Dj easily

        for j in range(rows.shape[0]):
            mean = np.mean(rows[j][:])  # mean of trnasposed rows[j]
            median = np.median(rows[j][:])  # median of trnasposed rows[j]
            mean_median = np.mean([mean, median])  # mean of median of trnasposed rows[j] and mean of trnasposed rows[j]
            te = round(mean_median, 2)  # temporary variable to store the value of mean_median
            temparr.append(te)

    cm = np.zeros((K, data_matrix.shape[1]))  # create matirx with all 0
    A = np.reshape(temparr, (-1, data_matrix.shape[1]))  # reshape temparr to have n * m rows

    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            # update i,j value of A in cm
            u = A[i][j]
            cm[i][j] = u

    return cm


def checker(K, beta):  # a function called by get groups to always get positive values for beta and k from user
    f = False
    if (K >= 0) and (beta >= 0):
        return True
    else:
        while f == False:  # keeps on taking values from user until the user inputs the positive value for beta and K
            K = int(input("positive integer value of K: "))
            beta = int(input("positive integer value of beta: "))
            if (K >= 0) and (beta >= 0):
                f = True
        return f


def get_groups(data_matrix, K, beta):
    m = data_matrix.shape[1]
    # step 1:
    # checks if beta nad k are positive

    x = checker(K, beta)
    #     print(data_matrix)

    #     data_matrix = matrix(data_matrix).load_from_csv(data_matrix) # calling the class to get matrix
    #     print(data_matrix)
    data_matrix = np.array(data_matrix)  # converting the data matrix into 2D np array

    if x == True:  # apply the funtion if it is true

        # step 2:
        weights = get_initial_weights(m)  # weights with 1 row and m columns, where sum of these values = m/2

        # step 3:
        centroids = np.empty((K, m))  # empty matrix with K rows and m columns

        # step 4:
        # print(data_matrix)
        n = data_matrix.shape[0]
        # print(n)
        S = np.zeros((n, 1))  # matrix S with n rows and 1 column, all elements = zero.

        # step 5:
        # for different rows from data_matrix
        unique_row = np.unique(data_matrix, axis=0)  # get all unique rows from the the data_matrix

        # get K number of different rows:
        np.random.shuffle(unique_row)  # shuffling to rows to select rows randomly

        # step 6:
        for i in range(K):
            centroids[i, :] = np.array(unique_row[i, :])  # append selected rows to centroids

        # step 7 part a:
        #         while True:
        weighted_distance = matrix(data_matrix).get_distance(centroids, weights, beta, i=None)

        # step 7 part b:

        lst = []
        temp = []
        for j in centroids:  # parse each row from the centroind matrix
            lst.append(round(sum(j), 2))  # sum the rows of centroid and append to lst
        for row in data_matrix:  # parse each row from the data matrix
            if row in centroids:  # if the row exisits in centroid

                a = (np.where((centroids == row).all(axis=1))[
                    0])  # directly fetch index at which it exist and append it to temp
                temp.append(a[0])
            else:
                if sum(row) in lst:  # if another centroid row has same sum as this row from data matrix fetch its row and append to temp
                    temp.append(lst.index(sum(row)))
                else:
                    a = sum(row) - max(
                        lst)  # if the sum doesnt exisit then subratact to highest sum of row of centroid,
                    if (a <= min(lst)):  # if a is less than the minimum value of row of centroid then append th
                        temp.append(lst.index(max(lst)))  # then the row which has max value is the nearest row
                    else:
                        temp.append(lst.index(min(lst)))  # else the nearest row will be the least sum row
        for i in range(len(temp)):  # append all temp indexes to matrix S
            S[i][0] = temp[i]

            # step 8 :
        if np.count_nonzero(S) != 0:  # counts if all zeros

            # implements step 9 to get new centroids:

            nc = get_centroids(data_matrix, S, K)
            # for empty rows update rows from centroid matrix
            ind = np.argwhere(np.all(nc == 0, axis=1))

            for i in ind:
                ix = i[0]
                nc[ix][:] = centroids[ix][:]
            centroids = nc

            # implements step 10 get__new_weights:
            get_new_weights(data_matrix, centroids, S, beta)
    #             else:
    #                 break;

    return S


def get_count_frequency(mat):
    sh = mat.shape  # gets the shape of array2D

    if (sh[1] == 1) or (len(sh) == 1):  # compares whether the array2D has 1 column or not

        dic = {}  # empty dictionary to store frequency of each value

        for i in mat:  # parsing each element
            if i[0] in dic:  # checks whther the element is present in the dictionary
                dic[i[0]] += 1  # increment the value of it by 1 if present
            else:
                dic[i[0]] = 1  # else assigns 1 to the element's value in dictionary

        freq_list = []  # empty list to store key, value pairs of freq dictionary

        for i in dic:  # parse each keys of dictionary
            freq_list.append([i, dic[i]])  # append the key and its frequncy into freq_list
        return freq_list
    else:
        pass  # if the condition isnt met then it doesnt do any thing


def get_new_weights(matrix, centroid_matrix, S, beta):
    # print("hi")
    pass


def run_test():
    m = matrix("Data.csv").load_from_csv(("csv_dump.csv"))
    for k in range(2, 5):
        for beta in range(11, 25):
            S = get_groups(m, k, beta / 10)
            print(str(k) + "-" + str(beta) + "=" + str(get_count_frequency(S)))
