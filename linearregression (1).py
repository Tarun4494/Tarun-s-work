#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import sklearn
from sklearn.datasets import load_boston










# In[2]:


boston = load_boston()
bos = pd.DataFrame(boston.data)
bos.head()


# In[3]:


bos.shape


# In[4]:



# keys in data set
print(boston.keys())


# In[5]:



#describe dataset and find the columns name
print(boston.DESCR)


# In[6]:



boston.feature_names


# In[7]:


bos= pd.DataFrame(boston.data, columns=boston.feature_names)
bos.head()


# In[8]:


#MEDV-------> Median value of owner-occupied homes in $1000's

bos['MEDV']=boston.target


# In[9]:


bos.head()


# In[10]:


#data preprocessing
bos.info()   # depict that all columns contains equal 506 values


# In[11]:


bos.isnull().sum()   # contains no null values


# In[12]:


#Exploratory data analysis
import seaborn as sns
#explanation of seaborn distplot()
# https://seaborn.pydata.org/generated/seaborn.distplot.html
sns.set(rc={'figure.figsize':(11,9)})  
sns.distplot(bos['MEDV'], bins=30)    #more-- https://towardsdatascience.com/histograms-and-density-plots-in-python-f6bda88f5ac0
plt.show()


# In[13]:


#We will use the heatmap function from the seaborn library to plot the correlation matrix
correlation_matrix = bos.corr().round(2)
# annot = True to print the values inside the square
sns.heatmap(data=correlation_matrix, annot=True)


# In[15]:


#The correlation coefficient ranges from -1 to 1. If the value is close to 1, it means that there is a strong positive correlation between the two variables. When it is close to -1, the variables have a strong negative correlation.
# visualize the relationship between the features and the response using scatterplots
fig, axs = plt.subplots(1, 2, sharey=True)
bos.plot(kind='scatter', x='RM', y='MEDV', ax=axs[0], figsize=(16, 8))
bos.plot(kind='scatter', x='LSTAT', y='MEDV', ax=axs[1])


# In[16]:


#Preparing the data for training the model & import the liner regression from sk learn
# create X and y
feature_cols = ['LSTAT', 'RM']
X = bos[feature_cols]
Y = bos['MEDV']



# #or We concatenate the LSTAT and RM columns using np.c_ provided by the numpy library.
# X1 = pd.DataFrame(np.c_[bos['LSTAT'], bos['RM']], columns = ['LSTAT','RM'])

#both are similar


# In[17]:


#Splitting the data into training and testing sets
from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state=5)
print(X_train.shape)
print(X_test.shape)
print(Y_train.shape)
print(Y_test.shape)


# In[18]:


#Training and testing the model
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
my_Model= LinearRegression()
my_Model.fit(X_train, Y_train)


# In[19]:


#Model evaluation
print(my_Model.intercept_)        
print(my_Model.coef_)


# In[20]:


# model evaluation for training set
y_train_predict = my_Model.predict(X_train)
rmse = (np.sqrt(mean_squared_error(Y_train, y_train_predict)))
r2 = r2_score(Y_train, y_train_predict)

print("The model performance for training set")
print("--------------------------------------")
print('RMSE is {}'.format(rmse))
print('R2 score is {}'.format(r2))
print("\n")

# model evaluation for testing set
y_test_predict = my_Model.predict(X_test)
rmse = (np.sqrt(mean_squared_error(Y_test, y_test_predict)))
r2 = r2_score(Y_test, y_test_predict)

print("The model performance for testing set")
print("--------------------------------------")
print('RMSE is {}'.format(rmse))
print('R2 score is {}'.format(r2))


# In[21]:


#Evaluating model by stats OLS method
#claculating confidence interval


import statsmodels.formula.api as smf
lm = smf.ols(formula='MEDV ~ RM + LSTAT', data=bos).fit()
lm.conf_int(alpha = 0.05)   # will provide dataframe of (interval of intercept) as Intercept and (interval of slopes) as RM, 95% confidence interval
# lm.conf_int()    # will by default provide 95% confidence interval between parameters 

#note: Confidence interval would based on the student's t-distribution


# In[22]:


lm.rsquared   # closer to the r2_score and towards 1


# In[23]:


lm.pvalues     # very less hance not in critical region


# In[24]:


lm.bse     #standard error


# In[25]:


lm.summary()


# In[26]:


# visualize the relationship between the features and the response using scatterplots

plt.scatter(x=X_train['RM'], y=my_Model.predict(X_train))


# In[27]:


plt.scatter(X_train['RM'], Y_train,  color='black')
plt.scatter(X_train['RM'], y_train_predict,  color='green')
plt.scatter(X_test['RM'], y_test_predict,  color='orange')
plt.plot(X_test['RM'], y_test_predict, color='blue')


# In[28]:


X_train['RM']


# In[ ]:


#In this story, we applied the concepts of linear regression on the Boston housing dataset.

