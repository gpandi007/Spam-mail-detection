#!/usr/bin/env python
# coding: utf-8

# In[2]:


#!/usr/bin/env python
# coding: utf-8

# Importing the Dependencies

# In[1]:


import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


# Data Collection & Pre-Processing

# In[5]:


# loading the data from csv file to a pandas Dataframe
####raw_mail_data = pd.read_csv(r'C:\Users\ashish.jaiswal\Downloads\mail_data.csv')

raw_mail_data = pd.read_csv(r'C:\Users\HP\Downloads\spam mail\mail_data.csv')
# In[6]:


# In[3]:




print(raw_mail_data)


# In[7]:


# replace the null values with a null string
mail_data = raw_mail_data.where((pd.notnull(raw_mail_data)),'')


# In[8]:


# printing the first 5 rows of the dataframe
mail_data.head()


# In[9]:


# checking the number of rows and columns in the dataframe
mail_data.shape


# Label Encoding

# In[10]:


# label spam mail as 0;  ham mail as 1;

mail_data.loc[mail_data['Category'] == 'spam', 'Category',] = 0
mail_data.loc[mail_data['Category'] == 'ham', 'Category',] = 1


# spam  -  0
# 
# ham  -  1

# In[11]:


# separating the data as texts and label

X = mail_data['Message']

Y = mail_data['Category']


# In[12]:


print(X)


# In[13]:


print(Y)


# Splitting the data into training data & test data

# In[14]:


X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=3)


# In[15]:


print(X.shape)
print(X_train.shape)
print(X_test.shape)


# Feature Extraction

# In[16]:


# transform the text data to feature vectors that can be used as input to the Logistic regression

feature_extraction = TfidfVectorizer(min_df = 1, stop_words='english', lowercase='True')

X_train_features = feature_extraction.fit_transform(X_train)
X_test_features = feature_extraction.transform(X_test)

# convert Y_train and Y_test values as integers

Y_train = Y_train.astype('int')
Y_test = Y_test.astype('int')


# In[17]:


print(X_train)


# In[18]:


print(X_train_features)


# Training the Model

# Logistic Regression

# In[19]:


model = LogisticRegression()


# In[20]:


# training the Logistic Regression model with the training data
model.fit(X_train_features, Y_train)


# Evaluating the trained model

# In[21]:


# prediction on training data

prediction_on_training_data = model.predict(X_train_features)
accuracy_on_training_data = accuracy_score(Y_train, prediction_on_training_data)


# In[22]:


print('Accuracy on training data : ', accuracy_on_training_data)


# In[23]:


# prediction on test data

prediction_on_test_data = model.predict(X_test_features)
accuracy_on_test_data = accuracy_score(Y_test, prediction_on_test_data)


# In[24]:


print('Accuracy on test data : ', accuracy_on_test_data)


# Building a Predictive System

# In[31]:


input_mail = ["Free tickets for Water Park. Send message for coupons."]

# convert text to feature vectors
input_data_features = feature_extraction.transform(input_mail)

# making prediction

prediction = model.predict(input_data_features)
print(prediction)


if (prediction[0]==1):
  print('Ham mail')

else:
  print('Spam mail')


# In[ ]:





# In[ ]:





# In[ ]:




