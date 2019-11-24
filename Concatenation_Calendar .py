#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df1= pd.read_csv('ClCalendarMon.csv')


# In[3]:


df2= pd.read_csv('ClCalendarTor.csv')


# In[4]:


df3= pd.read_csv('ClCalendarVan.csv')


# In[5]:


df=pd.concat([df1,df2,df3],ignore_index=True)


# In[6]:


df.shape


# In[13]:


df.info()


# In[14]:


df.date.min()


# In[16]:


df.to_csv("finalCalendar.csv")

