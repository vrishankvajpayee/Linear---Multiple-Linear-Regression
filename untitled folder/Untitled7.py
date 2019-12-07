#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

from sklearn.linear_model import LinearRegression


# In[4]:


data=pd.read_csv('udemy.csv')
data


# In[5]:


x=data['SAT']
y=data['GPA']


# In[6]:


x.shape


# In[10]:


y.shape


# In[14]:


x_matrix = x.values.reshape(-1,1)
x_matrix.shape


# In[8]:


reg = LinearRegression()


# In[16]:


reg.fit(x_matrix,y)


# In[ ]:




