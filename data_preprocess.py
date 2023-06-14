#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import re


# In[2]:
df=''
def get_dataFrame(dataframe):
    global df
    df=dataframe
    change()
    return df




# In[3]:


def convert(row):
    v = re.compile("(\d+)(\.?)(\d*)(\D)")
    v_dct = {'K': 1000, 'M': 1000000}
    x = v.match(row.Views)
    y= v.match(row.Likes)
    z=v.match(row.Subscribers)
    grp1=x.groups()
    grp2=y.groups()
    grp3=z.groups()
    i=float(''.join(grp1[:-1]))
    row.Views=i*(v_dct.get(grp1[-1]))
    j=float(''.join(grp2[:-1]))
    row.Likes=j*(v_dct.get(grp2[-1]))
    k=float(''.join(grp3[:-1]))
    row.Subscribers=k*(v_dct.get(grp3[-1]))
    return row
def change():
    global df
    df=df.apply(convert,axis="columns")
    print(df)



    # In[4]:


    spa=np.linspace(min(df['Views']),max(df['Views']),4)
    groups=['low','mid','high']
    df['Views_groups']=pd.cut(x=df['Views'],labels=groups,bins=spa,include_lowest=True)



    # In[5]:


    spa=np.linspace(min(df['Likes']),max(df['Likes']),4)
    groups=['low','mid','high']
    df['Likes_groups']=pd.cut(x=df['Likes'],labels=groups,bins=spa,include_lowest=True)


    # In[6]:


    spa=np.linspace(min(df['Subscribers']),max(df['Subscribers']),3)
    groups=['low','high']
    df['Subs_groups']=pd.cut(x=df['Subscribers'],labels=groups,bins=spa,include_lowest=True)


    # In[7]:



    # In[8]:




