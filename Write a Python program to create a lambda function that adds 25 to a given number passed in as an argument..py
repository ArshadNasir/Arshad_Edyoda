#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Write a Python program to create a lambda function that adds 25 to a given number passed in as an argument.

r = lambda a : a + 25
print(r(10))
r = lambda x, y : x * y
print(r(12, 4))

