#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Write a python function to sum all the numbers in a list


def sum(numbers):
    total = 0
    for x in numbers:
        total += x
    return total
print(sum((6, 10, 13, 0, 100)))

