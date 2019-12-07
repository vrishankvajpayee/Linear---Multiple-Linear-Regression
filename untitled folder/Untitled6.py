#!/usr/bin/env python
# coding: utf-8

# In[1]:


import datetime as dt
import time as tm


# In[2]:


tm.time()


# In[3]:


dtnow=dt.datetime.fromtimestamp(tm.time())
dtnow


# In[4]:


dtnow.year,dtnow.month,dtnow.day,dtnow.hour,dtnow.minute,dtnow.second


# In[5]:


my_function=lambda a,b,c:a+b


# In[6]:


my_function(1,2,3)


# In[7]:


import numpy as np


# In[8]:


mylist=[1,2,3]
x=np.array(mylist)
x


# In[9]:


y=np.array((4,5,6))
y


# In[10]:


m=np.array(([7,8,9])([10,11,12]))


# In[13]:


m=np.array([[7,8,9],[10,11,12]])
m.shape


# In[14]:


x+y


# In[15]:


import pandas pd


# In[16]:


import pandas as pd


# In[17]:


get_ipython().run_line_magic('pinfo', 'pd.Series')


# In[18]:


animals=['Genda','Bandar','Mouse']
pd.Series(animals)


# In[19]:


sports={'Archery':'Bhutan',
        'Golf':'Scotland',
        'Sumo':'Japan',
        'Cricket':'India'}
s=pd.Series(sports)
s


# In[20]:


s.iloc[2]


# In[21]:


s.loc['Cricket']


# In[22]:


v=pd.Series([100.0,150.0,123.0,120.0])
v


# In[23]:


import numpy as np
total=np.sum(v)
print(total)


# In[24]:


v+=2
v.head


# In[41]:


import pandas as pd
purchase_1=pd.Series({'Name':'Vrishank',
                      'Item purchased':'Kutta',
                      'Cost':'24.23'})
purchase_2=pd.Series({'Name':'Vinita',
                      'Item purchased':'Billi',
                      'Cost':'23.24'})
purchase_3=pd.Series({'Name':'Vivek',
                      'Item purchased':'Tota',
                      'Cost':'22.23'})
df=pd.DataFrame([purchase_1,purchase_2,purchase_3],index=['Store 1','Store 2','Store 3'])
df.head()


# In[32]:


df.loc['Store 2']


# In[34]:


type(df.loc['Store 2'])


# In[35]:


df.loc['Store 1']


# In[39]:


df.loc['Store 1','Cost']


# In[40]:


df.T


# In[42]:


df.T


# In[44]:


df.drop('Store 2')


# In[45]:


df


# In[46]:


df['Location']=None
df


# In[49]:


df['Location']=['Kalawad Road','Amin Marg','Dhebar Road']


# In[48]:


df


# In[50]:


df


# In[57]:


import pandas as pd
purchase_1=pd.Series({'Name':'Vrishank',
                      'Item purchased':'Kutta',
                      'Cost':'24.23',
                      'Location':'Kalawad Road'})
purchase_2=pd.Series({'Name':'Vinita',
                      'Item purchased':'Billi',
                      'Cost':'23.24',
                      'Location':'Amin Marg'})
purchase_3=pd.Series({'Name':'Vivek',
                      'Item purchased':'Tota',
                      'Cost':'22.23',
                      'Location':'Dhebar Road'})
purchase_4=pd.Series({'Name':'Vernika',
                      'Item purchased':'Teddy',
                       'Cost':'23.98',
                       'Location':'Gondal Road'})
df=pd.DataFrame([purchase_1,purchase_2,purchase_3,purchase_4],index=['Store 1','Store 2','Store 3','Store 2'])
df.head()


# In[54]:


df.loc['Store 2']


# In[55]:


df


# In[58]:


df.loc['Store 2']


# In[59]:


df.loc['Location']


# In[ ]:




