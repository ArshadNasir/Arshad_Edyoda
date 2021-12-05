#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Write a Python program to triple all numbers of a given list of integers. Use Python map.

nums = (1, 2, 3, 4, 5, 6, 7) 
print("Original list: ", nums)
result = map(lambda x: x + x + x, nums) 
print("\nTriple of said list numbers:")
print(list(result))

