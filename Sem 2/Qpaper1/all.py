#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
a=np.array([1,2,3,4,5])
b=np.array([1,3,2,4,5])
np.where(a==b)


# In[5]:


dict={'a':100,'b':200,'c':300,'d':400,'e':500}
ser=pd.Series(dict)


# In[6]:


ser


# In[7]:


dataframe3=pd.DataFrame({'col1':[1,2,3,4,7,11],'col2':[4,5,6,9,5,0],'col3':[7,5,8,12,1,11]})
series3=dataframe3['col1']
type(series3)


# In[8]:


series4=pd.Series(range(10))
series4[series4>6]


# In[9]:


series5=pd.Series(range(4))
series5.reindex([2,3,0,1])


# In[11]:


series6=pd.Series(np.random.randint(0,10,35))
dataframe6=pd.DataFrame(series6.values.reshape(7,5))
print(dataframe6)


# In[12]:


ser1=pd.Series([1,2,3,4,5])
ser2=pd.Series([3,4,5])
np.setdiff1d(ser1,ser2)


# In[16]:


frame=pd.read_csv(r'C:\Users\prac\Downloads\test_data.csv')
frame


# In[17]:


frame.isna()


# In[19]:


col1 = frame.isna().sum()
col1[col1>0]


# In[20]:


frame.isna().sum()


# In[31]:


count_row=frame.isna().sum(axis=1)
drop=count_row[count_row>0]
frame.drop(drop.index)


# In[24]:


frame.dropna(axis=0,how='all')


# In[29]:


drop2=count_row[count_row<2]
frame.drop(drop2.index)


# In[32]:


frame.isna().sum().sum()


# In[33]:


frame.fillna(frame.iloc[0])


# In[34]:


frame.fillna(axis=0,method='ffill')


# In[36]:


frame['ord_no'].fillna(frame['ord_no'].mean())


# In[ ]:




