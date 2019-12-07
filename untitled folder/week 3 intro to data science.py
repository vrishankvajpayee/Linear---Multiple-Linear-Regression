#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd

df=pd.DataFrame([{'Name':'Vrishank','Item Purchased':'Soap','Cost':115},
                 {'Name':'Vinita','Item Purchased':'Tea','Cost':190},
                 {'Name':'Vivek','Item Purchased':'Pen','Cost':40},
                 {'Name':'Vernika','Item Purchased':'Bottle','Cost':290}],
                 index=['Store 1','Store 1','Store 2','Store 2'])
df


# In[6]:


df['Date'] =['January 7','February 3','February 6','September 24']
df


# In[8]:


import pandas as pd
adf = df.reset_index()
df=pd.DataFrame()
staff_df = pd.DataFrame([{'Name': 'Vrishank', 'Position':'Asc Team Lead'},
                         {'Name':'Shantnu',   'Position':'Web Lead'},
                         {'Name':'Vivek',     'Position':'Corp Lead'},
                         {'Name':'Himanshu',  'Position':'Web'}])
staff_df = staff_df.set_index('Name')                 
student_df=([{'Name': 'Vivek',   'Occupation':'Engineer'},
             {'Name': 'Vinita',  'Occupation':'Home Maker'},
             {'Name': 'Vrishank','Occupation':'Bache'},
             {'Name': 'Vernika', 'Occupation':'Bache'}])
student_df = student_df.set_index('Name')
print(staff_df.head())
print()
print(student_df.head())




# In[10]:


staff_df = pd.DataFrame([{'Name': 'Vrishank', 'Role': 'Team ASC Lead'},
                         {'Name': 'Shantnu', 'Role': 'Web Lead'},
                         {'Name': 'Anany', 'Role': 'Topper'},
                         {'Name': 'Vivek','Role':'Corp Lead'}])
staff_df = staff_df.set_index('Name')
student_df = pd.DataFrame([{'Name': 'Vivek', 'School': 'Engineering'},
                           {'Name': 'Vinita', 'School': 'Science'},
                           {'Name': 'Vrishank', 'School': 'Engineering'},
                           {'Name': 'Vernika', 'School': 'SNK'}])
student_df = student_df.set_index('Name')
print(staff_df.head())
print()
print(student_df.head())


# In[12]:


pd.merge(staff_df, student_df, how='outer', left_index=True, right_index=True)


# In[16]:


pd.merge(staff_df,student_df,how='inner',left_index=True, right_index=True)


# In[17]:


pd.merge(staff_df,student_df,how='left', left_index=True, right_index=True)


# In[18]:


pd.merge(staff_df,student_df,how='right',left_index=True,right_index=True)


# In[3]:


import pandas as pd
import numpy as np
df=pd.read_csv('census.csv')
df=df[df['SUMLEV']==50]
df


# In[9]:


for group,frame in df.groupby('STNAME'):
    avg=np.average(frame['CENSUS2010POP'])
    print('Counties in state ' + group +' have as average population of' + str(avg))


# In[10]:


df=pd.read_csv('census.csv')
df=df[df['SUMLEV']==50]


# In[11]:


df.groupby('STNAME').agg({'CENSUS2010POP':np.average})


# In[12]:


df=pd.read_csv('cars.csv')
df


# In[14]:


df.pivot_table(values='(kW)',index='YEAR',columns='Make', aggfunc=np.mean)


# In[15]:


import pandas as pd
import numpy as np 


# In[17]:





# In[ ]:





# In[ ]:




