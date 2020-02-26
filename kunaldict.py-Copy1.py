#!/usr/bin/env python
# coding: utf-8

# In[7]:


#ques1 
file={
    "a":42,
    "b":56,
    "c:":23,
}
print(file)


# In[10]:


#ques2
rollno={
    1:"rajat",
    2:"ravi",
    3:"kamal",
}
print(rollno)


# In[12]:


#ques3
dict1={
    "a":42,
    "b":56,
    "c:":23,
}
del dict1["a"]
print(dict1)


# In[17]:


#ques4
dict1={
    "a":42,
    "b":56,
    "c":23,
}
for key,value in dict1.items():
    print(key,value)


# In[27]:


#ques5
dict1={
    "mango":"fruit",
    "apple":"fruit",
   "tamato":"vegetable",
}
if ("mango"in dict1):
    print('mango in dict1')
else:
    print('notin dict1')


# In[28]:


#ques7
dict1={
    "a":42,
    "b":56,
    "c":23,
}
dict1["a"]="x"
print(dict1)


# In[33]:


#ques8
dict1={
    "a":42,
    "b":56,
    "c":23,
}
dict1["a"]=(11,21)
print(dict1)


# In[38]:


#ques9
dict1={
    "a":42,
    "b":56,
    "c":23
}
print(dict1)
dict2={
    "a":42,
    "b":56,
    "c":23
}
print(dict2)
if dict1==dict2:
    print('same')


# In[47]:


#ques10
dict={}
for key in range(1,11):
    dict[key]=key*key
print(dict)    


# In[59]:


#ques11
dict1={    "a":12,
    1:"abc",
    5:{"a":16,
        2:"def",
    },
    "c":17,
}
print(dict1)


# In[61]:


dict1={
    "a":42,
    "b":56,
    "c":23,
}
print(dict1.clear())


# In[70]:


#ques
dict1={
    "a":42,
    "b":56,
    "c":23,
}
dict2={
    "d":42,
    "y":56,
    "z":23,
}
dict3={
    "p":42,
    "f":54,
    "g":24,
}
for d in (dict1,dict2,dict3): 
    d.update(d)
    print(d)
    


# In[79]:


dict1={
    "a":42,
    "b":56,
    "c":23,
}
sum=0
for key,value in dict1.items():
    sum=sum+value
print(sum)
    


# In[84]:


dict1={
    "a":42,
    "b":56,
    "c":23,
}
mul=1
for key,value in dict1.items():
    mul=mul*value
print(sum)


# In[87]:


dict1={
    "key":"value1","key2":"value2","key3":{"key31":"value31","key32":"value32"},
}
dict1["key3"]["key32"]


# In[ ]:





# In[ ]:




