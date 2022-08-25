#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import numpy as np


# In[3]:


df=pd.read_csv("d:/pandas/WHO.csv")


# In[4]:


df.head()


# In[6]:


df[(df['Year'] == 1986) | (df['Year'] == 1987)]


# In[7]:


df


# In[13]:


#write a python programm to find out alchola consumption detail in 1987 ot 1989
result=df[(df['Year'] == 1987) | (df['Year'] == 1989)]
result


# In[24]:


#write a pandas prog to display the alcohol consumption in the year 1987
# where who region is wester pacific and country is viet nam

result=df[df['Year']==1987].where((df['WHO region'] =='Western Pacific') & 
                                  (df['Country'] =='Viet Nam'))
result1=result.dropna()
result1


# In[32]:


#display the horizontal bar chart for the year 1987
import matplotlib.pyplot as plt
plt.barh('Beverage Types','Display Value', data=result1, label='1987',color='green')
plt.xlabel("alcohol consumption")
plt.ylabel("wester pacifica")
plt.show()


# In[34]:


plt.bar('Beverage Types','Display Value', data=result1, label='1987',color='green')
plt.xlabel("alcohol consumption")
plt.ylabel("wester pacifica")
plt.show()


# In[40]:


#write a pandas program to find and display bar chart to out the alcohol consumption details
#in the year 1986 or 1989 where WHO region is 'America or 'EUROPE' from the datasets
result=df[(df['Year']==1986 ) |(df['Year']==1989 ) ].where((df['WHO region']=='Americas') | (df['WHO region']=='Europe'))
result1=result.dropna()
result1.head()


# In[42]:


#select data for the year 1986
result2=result1[result1['Year'] == 1986]
result2


# In[43]:


result3=result1[result1['Year'] == 1989]
result3


# In[49]:


#display the bar char for 1986 and 1989
plt.bar('WHO region','Display Value',label='1986',data=result2,color='green',width=0.5)
plt.show()


# In[53]:



plt.bar('WHO region','Display Value',label='1989',data=result3,color='orange',width=0.5)
plt.legend()
plt.xlabel('who region')
plt.ylabel('alcohol consumption')
plt.show()


# In[60]:


#write a pandas program to find out 'WHO region',country beverage types  in the year
# 1986 or 1989 where who region is americas and europe

result=df[(df['Year']==1986) | (df['Year']==1986)].where((df['WHO region']=='Americas') |(df['WHO region']=='Europe'))[['WHO region','Country','Beverage Types']]
result4=result.dropna()
result4


# In[64]:


#write a pands program to find out the records where consumption of beverages per
# person >5 and beverge types is beer

r=df[(df['Display Value'] > 5) &(df['Beverage Types'] =='Beer')]
r


# In[66]:


#write a pandas pro find out and display the pie char of the record where the consu of 
# of beverage is > 54 and type is beer wine and spiri

r1=df[(df['Display Value'] >=4) &(df['Beverage Types'] =='Beer')]['Display Value']
r1


# In[67]:



r2=df[(df['Display Value'] >=4) &(df['Beverage Types'] =='Wine')]['Display Value']
r2


# In[69]:



r3=df[(df['Display Value'] >=4) &(df['Beverage Types'] =='Spirits')]['Display Value']
r3


# In[71]:


#draw the pie charts
plt.pie(r1,shadow=True,autopct='%.1f%%')
plt.show()
plt.pie(r2,shadow=True,autopct='%.1f%%')
plt.show()
plt.pie(r3,shadow=True,autopct='%.1f%%')
plt.show()


# In[73]:


#pandas pro to filter the who region and beverage types columns and records
#by range 0 to 15
result=df.loc[:15,['WHO region','Beverage Types']]
result


# In[77]:


#pandas pro to filter the records who region containe 'Ea' substring

res=df[df['WHO region'].str.contains('Ea')]
res


# In[81]:


#pandas pro tofilter those records where who region matches  values
#(africa easter mediterrian.europe)
df.rename(columns={'WHO region':'WHO_region'},inplace=True)


# In[82]:


df


# In[84]:


df.query("WHO_region not in ['Afirca','Eastern Mediterranean','Europe']")


# In[85]:


#pands prog to find avrage cosn of wine per person > 2 in datasets
df[(df['Beverage Types'] =='Wine') & (df['Display Value'] > 2)]


# In[89]:


#pro to filter rows based on row number ended with 0 like 0,10,20,30,40
lst=list(range(0,100,10))
lst


# In[90]:


lst


# In[92]:


rows=df.iloc[lst,:]
rows


# In[95]:


#to also select rows with index label 0 to 9 
res=df.iloc[:10,:]
res


# In[99]:


rows=df.iloc[0:101:10,:][['Year','WHO_region']]
rows


# In[101]:


#to filter all columns where all entries present ,check which rows and columns have 
# nan finally drop the nan

df[df.loc[:,:].isna()]


# In[103]:


df.isnull().sum()


# In[104]:


df.dropna()


# In[105]:


#filter all records starting from the year and access every othe alternative columns

df.iloc[:,0::2]


# In[108]:


#to filter all records starting from 2nd row ,access every fifth row

df.iloc[2:100:5,:]


# In[109]:


#to rename the all the columns names

df.rename(columns={'Year':'_year','Beverage Types':'Beverage_types',"Display Value":'Display_values'})


# In[ ]:




