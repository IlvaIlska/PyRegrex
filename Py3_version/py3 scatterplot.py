#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd #plotting package
import numpy as np #arrays
import sklearn #regression package
import scipy as sp #trash
import matplotlib.pyplot as mpl #plotting our scatters

from sklearn.linear_model import LinearRegression 


# In[2]:


read = pd.read_csv(file)
read.plot.scatter(x = 'x', y = 'y', title = "Python 3 scatter")

mpl.savefig("py_orig.png")
mpl.show()
# # remake 1D array into 2D, then split data into training and test sets 

# In[3]:



data = sklearn.linear_model.LinearRegression()
X = read['x'].values.reshape(-1,1)
y = read['y'].values.reshape(-1,1)

#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
X_train = X
X_test = X
y_train = y
y_test = y


# # training the algo, then making predition with test set

# In[4]:


regressor = LinearRegression()  
regressor.fit(X_train, y_train) #training the algorithm
y_pred = regressor.predict(X_test)


# # plot output for test data

# In[5]:


mpl.scatter(X_test, y_test,  color='gray')
mpl.plot(X_test, y_pred, color='red', linewidth=2)
#mpl.plot()
mpl.savefig("py_Im.png")
mpl.show()


# # plot linear model with original data

# In[6]:


mpl.scatter(read['x'], read['y'],  color='blue')
mpl.plot(X_test, y_pred, color='red', linewidth=2)
#mpl.plot()
mpl.show()


# In[ ]:




