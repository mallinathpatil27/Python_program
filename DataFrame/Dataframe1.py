#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import numpy as np


# In[30]:


df=pd.DataFrame(np.random.randint(0,100,(4,3)),
               columns=('test1','test2','test3'),
               index=['vinay','malli','mohan','avd'])
df


# In[19]:


df.columns=['test1','test2','test3']


# In[20]:


df


# In[21]:


df['name']=['mahesh','malli','mohan','sathis']


# In[22]:


df


# In[28]:


df.set_index('name',inplace=True)


# In[26]:


df


# In[27]:


df


# In[31]:


df


# In[32]:


# pd.set_option('display.max_rows',None)


# In[33]:


cust=pd.read_csv('D:/pandas/shop.csv')
cust


# In[34]:


cust.head(2)


# In[37]:


cust[cust['Income']>23].head()


# In[39]:


cust[cust['Income']==23]


# In[42]:


cust[cust['Income']==23][['ID','Gender']]


# In[48]:


cust[(cust['Income']==23) & (cust['Score']==98)]


# In[51]:


cust[cust.Income==cust.Income.max()]


# In[52]:


cust.agg({'Age':['mean','max','min']})


# In[56]:


cust.Income.unique()


# In[57]:


cust.nsmallest(1,columns='Income')


# In[58]:


cust


# In[63]:


cust['status']='no'


# In[64]:


cust


# In[68]:


cust.loc[cust['Score']==39,'status']='low'
cust


# In[69]:


cust['status'].replace('no','NO',regex=True)


# In[70]:


rng=pd.date_range(start='2022/07/24',periods=100,freq='B')


# In[71]:


rng


# In[72]:


tips=pd.read_csv("d:/pandas/tips.csv")


# In[73]:


tips.head()


# In[78]:


tips['status']=np.where(tips['total_bill']<10,'low','high')


# In[82]:


tips.where(tips['total_bill']>17,"low")


# In[ ]:




