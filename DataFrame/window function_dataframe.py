#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[21]:


df = pd.DataFrame({'a':[1,2,3,4,5,6,7,8],
                    'b':[10,np.nan,np.nan,20,np.nan,np.nan,30,30]}) 


# In[22]:


df


# In[4]:


# find cummulative sum of col 'a'
df['a_cumsum'] = df['a'].cumsum()  # cumsum functions


# In[5]:


df


# In[23]:


# find cummulative min of col 'a'
df['a_cummin'] = df['a'].cummin()  # cumsum functions


# In[13]:


df


# In[10]:


df.loc[df["a"] == 1, "a"] = 5


# In[11]:


df


# In[14]:


df['a']


# In[17]:


df.iloc[1]


# In[19]:


df['a']=np.where(df['a'] == 1,0,1)


# In[20]:





# In[24]:


df


# In[25]:


#find rooling sum on col 'a' for window = 2
obj=df['a'].rolling(window=2)
df['a_rollsum']=obj.sum()


# In[26]:


df


# In[27]:


df['a_cumsum']=df['a'].cumsum()


# In[28]:


df


# In[29]:


#find rooling sum on col 'b' for window = 2
obj=df['b'].rolling(window=2,min_periods=2)
df['b_roll_count']=obj.count()


# In[30]:


df


# In[31]:


#find expanding sum
obj = df['a'].expanding(min_periods=1)
obj


# In[32]:


df['a_exp_sum']=obj.sum()


# In[33]:


df


# In[ ]:


malli


# In[34]:


df


# In[40]:


df=pd.read_csv("D:/pandas/carprice.csv")


# In[41]:


df


# In[44]:


#filter the cols whose names start with 'm'
df.filter(regex='^M', axis=1)


# In[47]:


#filter the col ending with age
df.filter(regex='ge$',axis=1)


# In[48]:


df_car=df['Car Model']


# In[50]:


df_car


# In[51]:


df_car.str.len() #to find the length of the string


# In[58]:


#know if the Audi is there in the car names
df[df_car.str.contains(r'Audi \w+')]


# In[60]:


obj=df_car.str.findall(r'Audi \w+')
obj


# In[61]:


df_car.str.replace(r'Audi','Bodi')


# In[66]:


df_car.str.title() # we can use all the string functions here


# In[70]:


# df1=df_car.str.extract(r'BMW \w\w')
df_car


# In[71]:


df1=df_car.str.extract(r'(BMW \w\w)')


# In[72]:


df1


# In[73]:


df1=df_car.str.extractall(r'(BMW \w\w)')


# In[74]:


df1


# In[75]:


lst=df_car.str.split(r'[XA]\d')
for i in lst:
    print(i)


# In[77]:


df.head()


# In[80]:


df['Mileage'].str.findall(r'5\d*')


# In[81]:


#data time indexing 
#resampling
#data range
#


# In[87]:


df=pd.read_csv("D:/pandas/AAPL1.csv",parse_dates=["Date"],index_col='Date')


# In[88]:


df


# In[91]:


df.loc["2020-01"]


# In[92]:


df


# In[93]:


df.loc["2008-01"]


# In[95]:


df.loc["2008-01"].Close.mean()


# In[96]:


df 


# In[97]:


df.loc["2008-01-05":"2008-01-10"]


# In[100]:


df.describe()


# In[101]:


df.Close.resample('M').mean()  #m= monthly  D for daily w for  W weekly 
# Q querterly  B business H hourly  


# In[104]:


get_ipython().run_line_magic('matplotlib', 'inline')
df.Close.resample('M').mean().plot(kind='line')


# In[105]:


#scatter plot
df.plot.scatter(x = 'Open',y='Close',alpha=0.5)


# In[106]:


df[['High','Low']].plot.box()


# In[107]:


df=pd.read_csv("D:/pandas/AAPL.csv")


# In[108]:


df


# In[111]:


rng=pd.date_range(start="2020/1/20",end="2020/6/7",freq='B')
rng


# In[124]:


rownum=(for i in range(1,101):print(i))


# In[123]:


df.set_index(rng,inplace=True)
df


# In[115]:


df.Close.plot()


# In[116]:


df.head(10).Close.mean()


# In[117]:


df['2020-1-20': '2020-1-31'].Close.mean()


# In[118]:


df.asfreq('D',method='pad')


# In[125]:





# In[127]:


df.set_index(rownu,inplace=True)


# In[120]:


for i in range(1,101):
    print(i)
    


# In[121]:





# In[122]:


rng=pd.date_range(start="2020/1/20",periods=100,freq='B')
rng


# In[128]:


df


# In[133]:


df['row_num'] = np.arange(1,101)


# In[132]:


df


# In[135]:


df


# In[136]:


df.set_index('row_num',inplace=True)


# In[137]:


df


# In[ ]:




