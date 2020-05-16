#!/usr/bin/env python
# coding: utf-8

# In[1]:




import pandas as pd
import numpy as np
df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN',
'londON_StockhOlm',
'Budapest_PaRis', 'Brussels_londOn'],
'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]],
'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )',
'12. Air France', '"Swiss Air"']})



df














# 1. Some values in the the FlightNumber column are missing. These numbers are
# meant to increase by 10 with each row so 10055 and 10075 need to be put in
# place. Fill in these missing numbers and make the column an integer column
# (instead of a float column).

# In[128]:


val=pd.Series([1045,1055,1065,1075,1085],index=[0,1,2,3,4])
val


# In[129]:


df['FlightNumber']=val


# In[130]:


df


# 2. The From_To column would be better as two separate columns! Split each
# string on the underscore delimiter _ to give a new temporary DataFrame with
# the correct values. Assign the correct column names to this temporary
# DataFrame.

# In[131]:


From_To=df["From_To"].str.split("_")


# In[132]:


df1=From_To.to_list()


# In[133]:


df1


# In[134]:


names=["From","To"]


# In[135]:


names


# In[136]:


df2=pd.DataFrame(df1,columns=names)


# In[137]:


df2


# In[138]:


df[["From","To"]]=df2


# In[139]:


df


# 3. Notice how the capitalisation of the city names is all mixed up in this
# temporary DataFrame. Standardise the strings so that only the first letter is
# uppercase (e.g. "londON" should become "London".)
# 

# In[140]:


df['From']=df['From'].str.capitalize()


# In[141]:


df['To']=df['To'].str.capitalize()


# In[142]:


df


# 4. Delete the From_To column from df and attach the temporary DataFrame
# from the previous questions.

# In[143]:


df.drop('From_To',axis=1,inplace=True)


# In[145]:


df


# 5. In the RecentDelays column, the values have been entered into the
# DataFrame as a list. We would like each first value in its own column, each 
# second value in its own column, and so on. If there isn't an Nth value, the value
# should be NaN.
# 

# 

# In[144]:


df5=df['RecentDelays'].to_list()


# In[146]:


df5


# In[147]:


df3 = pd.DataFrame(df['RecentDelays'].values.tolist())


# In[148]:


df3


# In[149]:


index=['delay1','delay2','delay3']


# In[150]:


df3.columns=index


# In[151]:


df3


# In[152]:


df[["delay1","delay2","delay3"]] = df3[["delay1","delay2","delay3"]]


# In[153]:


df


# In[154]:


df.drop('RecentDelays',axis=1,inplace=True)


# In[155]:


df


# 


# In[ ]:




