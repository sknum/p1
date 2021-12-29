#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import random
import csv
import pdb
def read_data(filename):
    with open(filename,'r')as csvfile:
        datareader =csv.reader(csvfile)
        metadata=next(datareader)
        traindata=[]
        for row in datareader:
            traindata.append(row)
    return(metadata,traindata)

def splitdataset(dataset,splitratio):
    trainsize=int(len(dataset)*splitratio)
    trainset=[]
    testset=list(dataset)
    i=0
    while len(trainset)<trainsize:
        trainset.append(testset.pop(i))
    return[trainset,testset]

def classifydata(data,test):
    total_size=data.shape[0]
    print("\n")
    print("training data size=",total_size)
    print("test data size=",test.shape[0])
    countyes=0
    countno=0
    probyes=0
    probno=0
    print("\n")
    print("target count probability")
    for x in range(data.shape[0]):
        if data[x,data.shape[1]-1]=='Yes':
            countyes=countyes+1
        if data[x,data.shape[1]-1]=='No':
            countno=countno+1
    probyes=countyes/total_size
    probno=countno/total_size
    print("yes","\t",countyes,"\t",probyes)
    print("no","\t",countno,"\t",probno)
    prob0=np.zeros((test.shape[1]-1))
    prob1=np.zeros((test.shape[1]-1))
    accuracy=0
    print("\n")
    print("instance prediction target")
    for t in range(test.shape[0]):
        for k in range(test.shape[1]-1):
            count1=count0=0
            for j in range(data.shape[0]):
                if test[t,k]==data[j,k] and data[j,data.shape[1]-1]=='No':
                    count0=count0+1
                if test[t,k]==data[j,k] and data[j,data.shape[1]-1]=='Yes':
                    count1=count1+1
            prob0[k]=count0/countno
            prob1[k]=count1/countyes
       
        probNo=probno
        probYes=probyes
        for i in range(test.shape[1]-1):
            probNo=probNo*prob0[i]
            probYes=probYes*prob1[i]
        if probNo>probYes:
                predict='No'
        else:
                predict='Yes'
       
        print(t+1,"\t",predict,"\t",test[t,test.shape[1]-1])
        if predict==test[t,test.shape[1]-1]:
                accuracy+=1
    final_accuracy=(accuracy/test.shape[0])*100
    print("accuracy",final_accuracy,"%")
    return
   
metadata,traindata=read_data("data3.csv")
print("attribute names of the traning dta are:", metadata)
splitratio=0.6
trainingset,testset=splitdataset(traindata,splitratio)
training=np.array(trainingset)
print("\n tarining data set are")
for x in trainingset:
     print(x)
testing=np.array(testset)
   
print("\n the test data set are:")
for  x in testing:
        print(x)
classifydata(training, testing)
       


# In[ ]:




