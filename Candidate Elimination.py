#!/usr/bin/env python
# coding: utf-8

# In[31]:


import numpy as np
import pandas as pd
data=pd.DataFrame(data=pd.read_csv('enjoysport.csv'))
concepts=np.array (data.iloc[:,0:-1])
print("\n Instances are :\n ",concepts)
target=np.array(data.iloc[:,-1])
print("\n Target values are :",target)
def learn(concepts,target):
    specific_h=concepts[0].copy()
    print("initialization of specific_h and general_h")
    print("\n specific Boundary :",specific_h)
    general_h=[["?" for i in range (len(specific_h))] for i in range (len(specific_h))]
    print("\n generic Boundary :",general_h)
    for i,h in enumerate(concepts):
        print("\n Instance",i+1,"is",h)
        if target[i]=='yes':
            print("Instance is positive")
            for x in range (len(specific_h)):
                if h[x]!=specific_h[x]:
                    specific_h[x]='?'
                    general_h[x][x]='?'
        if target[i]=="no":
            print("Instance is negative")
            for x in range (len(specific_h)):
                if h[x]!=specific_h[x]:
                    general_h[x][x]=specific_h[x]
                else:
                    general_h[x][x]='?'
        print("Specific Boundary after",i+1,"Instance is",specific_h)
        print("Generic Boundary after",i+1,"Instance is",general_h)
        print("\n")
    indices=[i for i, val in enumerate (general_h) if val==['?','?','?','?','?','?']]
    for i in indices:
        general_h.remove(['?','?','?','?','?','?'])
    return specific_h,general_h
s_final,g_final=learn(concepts,target)
print("Final specific_h:",s_final,sep="\n")
print("Final general_h:",g_final,sep="\n")


# In[ ]:





# In[ ]:





# In[ ]:




