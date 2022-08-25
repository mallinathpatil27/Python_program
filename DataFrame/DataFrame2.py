#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


data=pd.read_csv("D:\pandas\emp.csv")
df=pd.DataFrame(data)
df


# In[7]:


df.head()


# In[8]:


df['empid']


# In[9]:


import pyspark


# In[10]:


import os 
import sys
import findspark
findspark.init()
os.environ["JAVA_HOME"]='C:\bigdata\Java'
os.environ["SPARK_HOME"]='C:\bigdata\spark-3.1.2-bin-hadoop3.2'
from pyspark.sql import *
from pyspark.sql.functios import *


# In[11]:


df


# In[12]:


df.head(2)


# In[16]:


df.shape


# In[17]:


df


# In[18]:


df.head()


# In[19]:


df.tail()


# In[20]:


df.head(2)


# In[21]:


df.tail(2)


# In[22]:


df['ename']


# In[23]:


df[2:4]


# In[26]:


df[::2]


# In[27]:


df[::-1]


# In[28]:


df['ename']


# In[29]:


df.columns


# In[30]:


df.ename


# In[31]:


df['empid']


# In[32]:


df[['ename','empid']]


# In[34]:


df[['ename','sal']]


# In[36]:


df['sal'].min()


# In[38]:


df.describe()


# In[41]:


df[df.sal>50000]


# In[42]:


df[df.sal ==df.sal.max()]


# In[43]:


df[df.sal ==df.sal.min()]


# In[44]:


df[df.sal < df.sal.mean()]


# In[45]:


df.index


# In[47]:


df1=df.set_index('empid')


# In[48]:


df1


# In[49]:


df1.loc[1004]


# In[50]:


df.set_index('empid',inplace=True)


# In[51]:


df


# In[53]:


df.reset_index(inplace=True)


# In[56]:


df


# In[57]:


df=pd.read_csv("D:\pandas\emp.csv")
df


# In[59]:


df1=df.fillna(0)
df1


# In[61]:


df1=df.fillna({'ename':'no_name','sal':'0.00','doj':"00-00-0000"})
df1


# In[62]:


df


# In[64]:


df1=df.dropna()
df1


# In[66]:


df=pd.read_csv("D:\pandas\emp.csv")
df


# In[67]:


df=pd.read_csv("D:\pandas\emp.csv",parse_dates=['doj'])
df


# In[71]:


df1=df.sort_values('doj',ascending=False)
df1


# In[72]:


df


# In[77]:


df.loc[:,['ename','sal']]


# In[78]:


df.iloc[:,[1,2]]


# In[80]:


df.iloc[:,[1,2,3]]


# In[81]:


df.loc[0:3,['ename','sal']]


# In[83]:


df.iloc[0:3]


# In[88]:


df.iloc[3:0:-1]


# In[91]:


df.shape


# In[92]:


df[2:4]


# In[93]:


df.columns


# In[94]:


df[['empid', 'ename', 'sal', 'doj']]


# In[95]:


df.ename


# In[96]:


df[['ename','sal']]


# In[98]:


df[df.sal.max()]


# In[99]:


df['sal'].max()


# In[100]:


df.sal.max()


# In[103]:


df[df.sal>df.sal.max()]


# In[106]:


df[df.sal == df.sal.max()]


# In[109]:


df[df.sal == df.sal.max()]


# In[110]:


df


# In[111]:


df


# In[113]:


df[df.sal>60000]


# In[115]:


df[df.sal !=50000]


# In[116]:


df.sal ==50000


# In[121]:


df[df.ename=='sathish'][['ename','ename']]


# In[123]:


df


# In[125]:


df1=df.set_index('empid')


# In[126]:


df1


# In[128]:


df1.loc[1004]


# In[ ]:




