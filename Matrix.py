import random

import numpy as np

class matrix:
    global array_2d
    def __init__(self, filename):
       self.load_from_csv(self, filename)
    def load_from_csv(self, filename):
        CSV_data = open(filename)
        array_2d = np.loadtxt(CSV_data,delimiter= ',')
        """
        Data standardization
        
        #Let D be a data matrix, so that Dij is the value of D at row i and column j. You can standardize D by
        #following the equation below.
        D′
        ij =
        Dij − min (Dj)
        max (Dj) − min (Dj)
        
        where max(Dj) is the highest value in column j, and min (Dj) is the lowest value in column j. D′
        ij
        
        is the standardized version of Dij – the algorithm below should only be applied to D′
        
        ij (i.e. do not
        
        apply the algorithm below to Dij).
        """
    def standardise(self):
        standardized_arr = [len(array_2d)][len(array_2d[0])]
        #Max for the column
        maxCol = np.max(array_2d, 0)
        #Max for the Row
        maxRow = np.max(array_2d,1)
        minCol = np.min(array_2d,0)
        for j in range(len(array_2d)):
            for i in range(len(array_2d[j])):
                standardval = (array_2d[j][i] - minCol)/ (maxCol - minCol)
                standardized_arr[j][i] = standardval
        return standardval;




    def get_distance(self, matrix, weight, number, beta):
        # Initialize the distance to 0
        dist = 0

        # Loop over the dimensions. Take squared difference and add to 'dist'
        for i in range(len(matrix.array_2d)):
            dist += (weight[i] - matrix.array_2d[i]) ** 2

        return dist

    def get_frequency_count(self):
        mp = dict()
        for i in range(array_2d):
         for j in range(array_2d[i]):
             if array_2d[i][j] in mp.keys():
                 mp[array_2d[i][j]] += 1
             else:
                mp[array_2d[i][j]] = 1
         return mp


def get_initial_weights(m):
    random_Matrix = [1][m]
    n = m /2
    index , sum = 0
    while index < m and sum < n:
        ranint = random.randrange(0,1)
        sum += ranint
        random_Matrix[1][index] = ranint
        index += 1
    return random_Matrix

def get_centroids(dataMatrix,S, K):
    centroidsMatrix = [K][len(dataMatrix)]
    for i in range(centroidsMatrix):
        for j in range(centroidsMatrix[i]):

            if dataMatrix[j] == j:
                matrix =  S.standardise()
                genMean = np.mean(matrix)
                median = np.median(matrix)
                specMean = np.mean(genMean,median)
                centroidsMatrix[i][j] = specMean
    return centroidsMatrix

def get_groups(matrix, groupsK, beta):
    K = 3
    beta = 1
    weights = get_centroids(matrix, groupsK, beta)
    centroids = np.empty(len(array_2d),len(array_2d))
    S = np.empty(len(array_2d), 1)
    S.fill(0)
    rand = random.randrange(0,K)
    centroids[rand][rand] = matrix.array_2d[rand][rand]
    standardize = matrix.standardise()
    for i in range(len(matrix.array_2d)):
        for j in range(len(array_2d)):
            centroids[i][j] = get_new_weights(S,centroids, matrix)
            if(S[i][1] == i):
                break
            else:
                S[i][1] = i
    centroidsMatrix = get_centroids(matrix, S,beta)
    get_new_weights(centroidsMatrix, centroids, S)


def get_new_weights(data, centroids, S):
    matrixS = np.empty(1,len(centroids))
    standardized = S.standardise()
    for i in range(len(centroids)):
        for j in range(len(standardized)):
            matrixS[1][i] = np.abs(standardized[j] - centroids[i]) * data




def run_test():
    m = matrix("Data.csv")

    for k in range(2,5):
        for beta in range(11,25):
            S = get_groups(m, k, beta/10)

            print(str(k)+"-"+str(beta)+"="+str(S.get_count_frequency()))




