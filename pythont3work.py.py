#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#theoretical Questions:
#q1 we can call it by using super() command
#q2 class Parent:
        pass
 class Child(Parent):
        pass
#q3  people={1:{'name':'John','age':'27','sex':'Male'}
        2:{'name':'Marie','age','22','sex':'Female'}}
 print(people)

    


# In[20]:


#set A
#q1
items=[]
for i in range(1000,3000):
    s=str(i)
    if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0):
        items.append(s)
print( ",".join(items))


# In[19]:


#q2
def calculateSum (a,b):
    s=int(a)+int(b)
    return s
# Main code
# take two integral numbers as strings
num1="10"
num2="20"
# calculate sum
sum=calculateSum(num1,num2)
# print sum
print("Sum=",sum)


# In[ ]:




