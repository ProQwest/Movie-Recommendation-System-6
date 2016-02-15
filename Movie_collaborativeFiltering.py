__author__ = 'shilpagulati'

import sys
import math
import heapq
import itertools
import operator

#Find Pearson correlation between 2 users

def Pearson_correlation(user1,user2):
    L1=UserRatings[[x[0] for x in UserRatings].index(user1)]
    if len(L1[1])==0:
        avg1=0
    else:

        avg1=sum(L1[1])/len(L1[1])
    L2=UserRatings[[x[0] for x in UserRatings].index(user2)]

    if len(L2[1])==0:
        avg2=0
    else:

        avg2=sum(L2[1])/len(L2[1])

    num=0.0
    den1=0.0
    den2=0.0
    for each in L1[2]:
        if each in L2[2]:

            num+=(L1[1][L1[2].index(each)]-avg1)*(L2[1][L2[2].index(each)]-avg2)
            den1+=(L1[1][L1[2].index(each)]-avg1)**2
            den2+=(L2[1][L2[2].index(each)]-avg2)**2
    if den1==0 or den2==0:
        similarity=0
    else:

        similarity=num/(math.sqrt(den1)*math.sqrt(den2))
    return similarity

# calculate K nearest neighbours of a user based on similarity

def K_nearest_neighbors(user1,item,k):
    NearestNeighbours={}

    for each in [x[0] for x in UserRatings]:
        if each!=user1:
                NearestNeighbours.setdefault(each,Pearson_correlation(user1,each))

    Knearest=sorted(NearestNeighbours.items(),key=operator.itemgetter(1))
    KnearesNew=Knearest[::-1]

    return KnearesNew[:k]

# Return the Predicted rating of the movie for the user

def Predict(user1,item,kvalue):
    Users=K_nearest_neighbors(user1,item,kvalue)


    for each in Users:

        print each[0],each[1]

    Prediction=0.0
    num=0.0
    den=0.0
    # den=sum([x[0] for x in Users])
    for each in Users:

        if item in UserRatings[[x[0] for x in UserRatings].index(each[0])][2]:
            index= UserRatings[[x[0] for x in UserRatings].index(each[0])][2].index(item)
            rating= UserRatings[[x[0] for x in UserRatings].index(each[0])][1][index]
            num+=each[1]*rating
            den+=each[1]
    if den==0:
        Prediction= 0
    else:
        Prediction=num/den
    print "\n"
    print  Prediction





UserRatings=[]
def main():


    Input=open(sys.argv[1])
    user1=sys.argv[2]

    item=sys.argv[3]

    kvalue=int(sys.argv[4])


    InputValues=[]
    for line in Input:
        line = line.rstrip().split('\t')
        InputValues.append(line)




    for each in InputValues:

        if each[0] not in [x[0] for x in UserRatings]:

            UserRatings.append([each[0],[float(each[1])],[each[2]]])
        else:
            UserRatings[[x[0] for x in UserRatings].index(each[0])][1].append(float(each[1]))
            UserRatings[[x[0] for x in UserRatings].index(each[0])][2].append(each[2])


    Predict(user1,item,kvalue)


if __name__ == '__main__':
    main()









