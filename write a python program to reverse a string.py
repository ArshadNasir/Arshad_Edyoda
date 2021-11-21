#!/usr/bin/env python
# coding: utf-8

# In[1]:


#write a python program to reverse a string

def reverse_string(str):  
    str1 = ""  
    for i in str:  
        str1 = i + str1  
    return str1
     
str = "1234abcd"     
print("The original string is: ",str)  
print("The reverse string is",reverse_string(str))  

