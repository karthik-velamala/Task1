#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


data=pd.read_csv("C:\Users\vardhan\Downloads\01.Data Cleaning and Preprocessing.csv")


# In[3]:


data=pd.read_csv('C:\Users\vardhan\Downloads\01.Data Cleaning and Preprocessing.csv')


# In[4]:


data = pd.read_csv(r'C:\Users\vardhan\Downloads\01.Data Cleaning and Preprocessing.csv')


# In[5]:


type(data)


# In[6]:


data.info


# In[7]:


data.describe()


# In[8]:


data=data.drop_duplicates()
data


# In[9]:


data.isnull()


# In[10]:


data.isnull().sum()


# In[11]:


data.notnull()


# In[12]:


data.isnull().sum()


# In[13]:


data.notnull()


# In[14]:


data.isnull().sum().sum()


# In[15]:


data2=data.fillna(value=0)


# In[16]:


data2


# In[17]:


data.isnull().sum()


# In[18]:


data.notnull()


# In[19]:


data2.isnull().sum().sum()


# In[20]:


data2


# In[21]:


data3=data.fillna(method='pad')
data3


# In[22]:


data2=data.fillna(value=0)


# In[23]:


data2


# In[24]:


data4=data.fillna(method='bfill')
data4


# In[ ]:




