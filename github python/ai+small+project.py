
# coding: utf-8

# In[1]:

import pandas as pd


# In[4]:

df = pd.read_csv("project 1 dataset.csv")


# In[6]:

df


# In[7]:

df.head


# In[8]:

df.head()


# In[9]:

df.tail()


# In[13]:

inputs = df.drop('salary_more_then_100k',axis='columns')


# In[14]:

inputs


# In[16]:

target=df["salary_more_then_100k"]
target


# In[21]:

from sklearn.preprocessing import LabelEncoder
le_company=LabelEncoder()
le_job=LabelEncoder()
le_degree=LabelEncoder()


# In[22]:

inputs['company_n']=le_company.fit_transform(inputs['company'])
inputs['job_n']=le_job.fit_transform(inputs['job'])
inputs['degree_n']=le_degree.fit_transform(inputs['degree'])


# In[23]:

inputs


# In[31]:

inputs_n=inputs.drop(['company','job','degree'],axis='columns')


# In[28]:

inputs_n


# In[29]:

target


# In[32]:

from sklearn import tree
model = tree.DecisionTreeClassifier()


# In[35]:

model.fit(inputs_n,target)


# In[38]:

model.score(inputs_n,target)


# model.predict([2,1,0])

# In[39]:

model.predict([[2,1,0]])


# In[40]:

model.predict([[2,1,1]])


# In[41]:

model.predict([[0,1,1]])


# In[42]:

model.predict([[0,0,1]])


# In[44]:

model.predict([[3,1,1]])


# In[ ]:




# In[ ]:




# In[ ]:



