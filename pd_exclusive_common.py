############################################## 
##### install module matplotlib_venn
##### python -m pip install matplotlib-venn

#### pip install numpy
#### python -m pip install scipy
#### python -m pip install -U pip
#### python -m pip install -U matplotlib
#### pip install shapely
#### pip install seaborn   ### conda install seaborn

import pandas as pd



#####################

shubho_a = pd.read_csv(r'SHUBHO_A')


# adding header 
headerList = ['id'] 
# converting data frame to csv 
shubho_a.to_csv("shubho_a.csv", header=headerList, index=False) 
shubho_a = pd.read_csv(r'shubho_a.csv')


shubho_b = pd.read_csv(r'SHUBHO_B')
headerList = ['id'] 
# converting data frame to csv 
shubho_b.to_csv("shubho_b.csv", header=headerList, index=False) 
shubho_b = pd.read_csv(r'shubho_b.csv')


import os
os.remove("shubho_a.csv") 
os.remove("shubho_b.csv") 


# Union
shubho_ab = pd.concat([shubho_a, shubho_b], ignore_index = True)
shubho_ab = shubho_ab.drop_duplicates()


#######################################

######   Intersection
shubho_aUb = shubho_a.merge(shubho_b)

print("********  Intersection checked  *********")

#######################################
#####    Difference

shubho_a_exclusive = shubho_a[shubho_a.id.isin(shubho_b.id) == False]
shubho_b_exclusive = shubho_b[shubho_b.id.isin(shubho_a.id) == False]


print("********  Exclusive checked  *********")

####  Explort result
shubho_ab.to_csv('shubho_ab', sep='\t', index=False, header=False)
shubho_a_exclusive.to_csv('shubho_a_exclusive', sep='\t', index=False, header=False)
shubho_b_exclusive.to_csv('shubho_b_exclusive', sep='\t', index=False, header=False)







