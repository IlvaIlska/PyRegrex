#!/usr/bin/env python
# coding: utf-8

# In[26]:


import pandas as pd #plotting package
import numpy as np #arrays
import sklearn #regression package
import scipy as sp #trash
import matplotlib.pyplot as mpl #plotting our scatters

import sys

from sklearn.linear_model import LinearRegression 

# # plot points only

# In[27]:


read = pd.read_csv(sys.argv[1])
read.plot.scatter(x = 'x', y = 'y', title = "Python 3 Scatter")
mpl.savefig('py_orig.png')

# # remake 1D array into 2D, then split data into training and test sets 

# # [training disabled for this exercise]

# In[28]:



data = sklearn.linear_model.LinearRegression()
X = read['x'].values.reshape(-1,1)
y = read['y'].values.reshape(-1,1)

#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
X_train = X
X_test = X
y_train = y
y_test = y


# # training the algo, then making predition with test set

# # [training disabled for this exercise]

# In[29]:


regressor = LinearRegression()  
regressor.fit(X_train, y_train) #training the algorithm
y_pred = regressor.predict(X_test)


# # plot linear model with original data

# In[32]:


mpl.scatter(read['x'], read['y'],  color='blue')
mpl.plot(X_test, y_pred, color='red', linewidth=2)
mpl.title = "Python 3 Scatter With Regression"
mpl.xlabel('x')
mpl.ylabel('y')
#mpl.plot()
mpl.show()
mpl.savefig('py_lm.png')

# In[ ]:




