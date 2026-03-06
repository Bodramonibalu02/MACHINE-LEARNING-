#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[3]:


arr=np.array([1,2,3,4,5])
arr
arr.ndim


# In[9]:


arr1=np.array([[1,2,3,4],[1,2,3,4]])
arr1
arr1.ndim


# In[31]:


q1=np.array([10,21,43])
q1.ndim


# In[34]:


rev=np.array([[10,28,45],[81,45,67]])
rev


# In[42]:


rev[1,1]


# In[43]:


rev.dtype


# In[45]:


rev[1,1]=22
rev


# In[48]:


rev=np.array([[10,28,45],[81,45,67]], dtype=np.float64)
rev.dtype


# In[49]:


rev


# In[50]:


rev.size


# In[51]:


rev.itemsize


# In[69]:


np.sort(rev,axis=None)


# In[60]:


zero_array=np.zeros([2,3])
zero_array


# In[61]:


ones_array=np.ones([3,3])
ones_array


# In[75]:


np.arange(10,29,2)


# In[79]:


np.linspace(1,50,7)


# In[80]:


rev


# In[84]:


np.reshape(rev,(3,2))


# In[85]:


rev.reshape(3,2)


# In[90]:


a=rev.flatten()


# In[91]:


a.sort()
a


# In[92]:


rev


# In[93]:


rev.min()


# In[96]:


rev.max()


# In[97]:


rev.sum()


# In[102]:


rev.sum(axis=1)


# In[104]:


rev.sum(axis=0)


# In[105]:


rev


# In[106]:


for row in rev:
    print(row)


# In[111]:


a=np.array([1,3,9,4,16])
np.sqrt(a)


# In[112]:


np.square(a)


# In[113]:


np.std(a)


# In[10]:


q1 = np.array([
    [200, 220, 250],  # Product A
    [150, 180, 210],  # Product B
    [300, 330, 360]   # Product C
])

q2 = np.array([
    [209, 231, 259],  # Product A
    [155, 192, 222],  # Product B
    [310, 340, 375]   # Product C
])


# In[11]:


q1.ndim


# In[12]:


q1+q2


# In[13]:


q1-q2


# In[14]:


(q2-q1)*100/q1


# In[15]:


prices = np.array([
    [10, 12, 11],  # Prices for Product A in different regions
    [8,  9,  10],  # Prices for Product B
    [15, 16, 17]   # Prices for Product C
])
q1_revenue=q1*prices


# In[16]:


q1_revenue


# In[18]:


q1_discount=q1*0.2
q1_discount


# In[19]:


A=[10,78,29,8,98,67,67,56,45,98,76,0,67,97,56,54,98]
A.sort()


# In[26]:


prices = np.array([
    [10, 12 ],  # Prices for Product A in different regions
    [8,  9  ],  # Prices for Product B
      # Prices for Product C
])


weights=np.array([100,2])
dot_product=np.dot(prices,weights)
dot_product


# In[28]:


a=np.array([1,2,3])
b=np.array([1,2,3])
cross_product=np.cross(a,b)


# In[29]:


cross_product


# In[114]:


a=np.array([2,6,7,8])
a


# In[117]:


a[0:2]


# In[118]:


a[-2:]


# In[121]:


b=np.array([[1,2,3],[4,5,6],[7,8,9]])
b


# In[123]:


b[1,2]


# In[124]:


b[2,0]


# In[125]:


b[-1]


# In[126]:


b[-1,0:2]


# In[130]:


b[:,1:3]


# In[131]:


c=np.array([[101,'mira'],['102','abdul'],['103','maria']])


# In[132]:


c


# In[133]:


d=np.array([[101,250,'2025-08-1'],[102,150,'2025-08-2'],[103,180,'2025-08-1']])


# In[134]:


d


# In[135]:


np.hstack((c,d))


# In[136]:


e=np.array([[104,"venkat"],[105,"john"],[106,'kathy']])


# In[137]:


e


# In[138]:


np.vstack((c,e))


# In[146]:


transactions=np.array([['101', 'mira',  '250', '2025-08-1'],
       ['102', 'abdul',  '150', '2025-08-2'],
       ['103', 'maria',  '180', '2025-08-1']])


# In[147]:


transactions


# In[148]:


np.hsplit(transactions,[3])


# In[151]:


x,y=np.vsplit(transactions,[2])


# In[152]:


x


# In[153]:


y


# In[154]:


monthly_sales=np.array([20,30,21,26,71])
result=monthly_sales>25


# In[155]:


result


# In[156]:


monthly_sales[result]


# In[157]:


monthly_sales.max()


# In[163]:


index=monthly_sales.argmax() 
index


# In[164]:


transactions


# In[175]:


transactions[:,2].astype(float)


# In[182]:


t_index=np.argmax(transactions[:,2].astype(float))

