#!/usr/bin/env python
# coding: utf-8

# In[1]:


x= 0
ans = int(input("Input any number to get the quad root: "))
while (x**4 < ans):
      x+=1
if x**4 != ans:
    print(ans, " does have a quad root")
else:
    print(x, " is a quad root of ", ans)
    

