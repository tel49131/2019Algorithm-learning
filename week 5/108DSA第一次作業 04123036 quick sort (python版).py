#!/usr/bin/env python
# coding: utf-8

# In[1]:


#第一次嘗試
a = [2,8,4,5,9]
def quicksort():
    piviot = a[1]
    for i in a:
        if i< piviot:
            x[j] = x[j-1]


# In[2]:


#第一次嘗試
quicksort(a)


# In[3]:


#第二次嘗試
a = [2,8,4,5,9]
def quicksort():
    for i in a:
        key = a[1]
        left_point = a[i+1]
        right_point = a[i-1]
        if left_point < right_point:
            a[i+1] = a[i-1]
        else:
            a[1] = right_point


# In[4]:


#第二次嘗試
quicksort(a)


# In[5]:


#第三次嘗試
def quicksort(list):
    left=[]                 #先創造出一個list存比pivot小的數
    right=[]                #再創造出一個list存比pivot大的數
    pivotlist=[]            #之後創造出一個list存pivot的數
    if len(list)<=1:
        return 
    else:
        pivot=list[0]
        for i in list:
            if i<pivot:              #比pivot小就把它加進left
                left.append(i)
            elif i>pivot:            #比pivot大就把它加進right
                right.append(i)
            else:
                pivotlist.append(i)  #剩下的就一定是pivot
    left = quicksort(left)
    right = quicksort(right)
    return left+pivotlist+right

a=[4,2,7,9,3,8]
quicksort(a)


# In[10]:


#第四次嘗試
left=[]
right=[]
pivotlist=[]
def quicksort(list):
    if len(list)<=1:
        return 
    else:
        pivot=list[0]
        for i in list:
            if i<pivot:
                left.append(i)
            elif i>pivot:
                right.append(i)
            else:
                pivotlist.append(i)
    return left+pivotlist+right


# In[11]:


#第四次嘗試
a=[4,2,7,9,3,8]
quicksort(a)


# In[12]:


#第五次嘗試
left=[]
right=[]
pivotlist=[]
def quicksort(list):
    if len(list)<=1:
        return 
    else:
        pivot=list[0]
        for i in list:
            if i<pivot:
                left.append(i)
            elif i>pivot:
                right.append(i)
            else:
                pivotlist.append(i)
    return quicksort(left)+pivotlist+quicksort(right)


# In[13]:


#第五次嘗試
a=[4,2,7,9,3,8]
quicksort(a)


# In[3]:


#第六次
def quick_sort(list): 
    small = []
    big = []
    keylist = []

    if len(list) <= 1:
        return list

    else:
        key = list[0] 
        for i in list:
            if i < key: 
                small.append(i)
            elif i > key: 
                big.append(i)
            else:
                keylist.append(i)

    small = quick_sort(small)
    big = quick_sort(big)
    return small + keylist + big


# In[4]:


#第六次嘗試
a=[2,9,3,7,6]
quick_sort(a)


# In[ ]:




