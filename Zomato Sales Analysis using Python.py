#!/usr/bin/env python
# coding: utf-8

# ## Zomato data analysis project

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


dataframe=pd.read_csv("Zomato data .csv")
print(dataframe)


# In[4]:


dataframe


# In[5]:


def handleRate(value):
    value=str(value).split('/')
    value=value[0];
    return float(value)
dataframe['rate']=dataframe['rate'].apply(handleRate)
print(dataframe.head())


# In[7]:


dataframe.info()


# # Type of restaurant

# In[8]:


dataframe.head()


# In[13]:


sns.countplot(x=dataframe['listed_in(type)'])
plt.xlabel("type of restaurant")


# # conclusion- majority of the restaurant falls in dining category

# In[14]:


dataframe.head()


# In[21]:


grouped_data=dataframe.groupby('listed_in(type)')['votes'].sum()
result = pd.DataFrame({'votes': grouped_data})
plt.plot(result, c="green", marker="o")
plt.xlabel("Type of restaurant",c="red",size=20)
plt.ylabel("Votes",c="red",size=20)


# # conclusion- dining restaurants has recived maximum votes

# In[22]:


dataframe.head()


# In[23]:


plt.hist(dataframe['rate'],bins=5)
plt.title("ratings distribution")
plt.show


# # conclusion - the majority restaurants recived ratings from 3.5 to 4

# # Average order spending by couples

# In[24]:


dataframe.head()


# In[25]:


couple_data=dataframe['approx_cost(for two people)']
sns.countplot(x=couple_data)


# # conclusion - the majority of couples preffer restaurants with an approximate cost of 300 rypees

# # wich mode receives maximum rating

# In[26]:


dataframe.head()


# In[29]:


plt.figure(figsize=(6,6))
sns.boxplot(x='online_order' , y='rate' , data=dataframe)


# # conclusion - offline order received lower rating compare to online order

# In[30]:


dataframe.head()


# In[31]:


pivot_table = dataframe.pivot_table(index='listed_in(type)', columns='online_order' , aggfunc="size" , fill_value=0)
sns.heatmap(pivot_table, annot=True, cmap="YlGnBu", fmt="d")
plt.title("Heatmap")
plt.xlabel("Online Order")
plt.ylabel("Listed In (Type)")
plt.show()


# # Conclusion: Dining restaurants primarily accept offline orders,whereas cafes primarily receive online orders.This suggests that clients prefer offline order at restaurants,but prefer online ordering at cafes.
