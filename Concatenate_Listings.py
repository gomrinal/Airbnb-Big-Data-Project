#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[6]:


df1= pd.read_csv("ClMonListings.csv")


# In[5]:


df2= pd.read_csv("ClTorListings.csv")


# In[7]:


df3= pd.read_csv("ClVanListings.csv")


# In[10]:


df= pd.concat([df1,df2,df3],ignore_index=True)


# In[12]:


df.shape


# In[13]:


df.info()


# In[14]:


df.to_csv('finalListings.csv')


# In[ ]:




