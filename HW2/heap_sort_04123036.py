#!/usr/bin/env python
# coding: utf-8

# # 完成  (同第八次)

# In[67]:


def heap_function(List,n,i):
    odd = 2*n+1
    even = odd+1
    largest = i
    if odd < n and List[i] < List[odd]: #這裡錯，後面的偶數比前面的大(i)，這樣才能換
        largest = odd
        
    if even < n and List[largest] <List[even]: #這裡也錯，因為前面已經把i換成largest
        largest = even
        
    if largest != i:
        List[i],List[largest]=List[largest],List[i]
        
        
        heap_function(List,n,largest)
    
def heap_sort(List):
    n = len(List)
    
    for i in range(n,0,-1):                #我是利用從前面去排
        heap_function(List,n,i)
        
    for i in range(n-1,0,-1):
        List[i],List[0]=List[0],List[i]
        heap_function(List,i,0)


# In[71]:


a = [8,1,4,3,9]
b= [8,4,1,2,3]


# In[72]:


heap_sort(b)


# In[73]:


print(b)


# # 第一次

# In[10]:


def heap_function(List,n,i):
    List=[]
    odd = 2*n +1
    even = odd +1
    largest = i
    
    if n<= len(List) and List[odd] > largest:
        List[odd] = largest
        
    if n <= len(List) and List[even] > largest:
        List[even] = largest
        
    heap_function(List,n,i)
        
    


# In[11]:


def heap_sort(list):
    x = len(list)
    
    for i in range(0,x,1):
        heap_function(List,n,i)
        
    for i in range(x-1,-1,-1):
        list[i],list[j]=list[j],list[i]
        heap_function(List,x-1,i)
        
        


# In[12]:


a = [2,45,1,8,3]


# In[13]:


heap_sort(a)


# # 第二次

# In[14]:


def heap_function(List,n,i):
    odd = 2*n +1
    even = odd +1
    largest = i
    
    if n<= len(List) and List[odd] > List[i]:
        List[odd] = largest
        
    if n <= len(List) and List[even] > List[i]:
        List[even] = largest
        
    heap_function(List,n,largest)
        


# In[15]:


def heap_sort(list):
    x = len(list)
    
    for i in range(0,x,1):
        heap_function(List,n,i)
        
    for i in range(x-1,-1,-1):
        list[i],list[j]=list[j],list[i]
        heap_function(List,x-1,i)


# In[16]:


a = [2,45,1,8,3]


# In[17]:


heap_sort(a)


# # 第三次

# In[18]:


def heap_function(List,n,i):
    odd = 2*n +1
    even = odd +1
    largest = i
    
    if List[odd] > List[i]:
        List[odd] = largest
        
    if List[even] > List[i]:
        List[even] = largest
        
    heap_function(List,n,largest)


# In[19]:


def heap_sort(List):
    x = len(List)
    
    for i in range(0,x,1):
        heap_function(List,x,largest)
        
    for i in range(x-1,-1,-1):
        list[i],list[j]=list[j],list[i]
        heap_function(List,x-1,i)


# In[20]:


a = [2,45,1,8,3]


# In[21]:


heap_sort(a)


# # 第四次

# In[22]:


def heap_function(List,n,i):
    odd = 2*n+1
    even = odd+1
    largest = List[i]
    
    if List[odd] < List[i]:
        largest = List[odd]
        
    if List[even] < List[i]:
        largest = List[even]
        
    if List[i] != largest:
        largest = List[i]
        
    heap_function(List,n,largest)
    
def heap_sort(List):
    n = len(List)
    
    for i in range(0,n,1):
        heap_function(List,n,largest)
        
    for i in range(0,n-1,1):
        List[i],List[0]=List[0],List[i]
        heap_function(List,n,0)
        


# In[23]:


a = [3,22,1,6,4]


# In[24]:


heap_sort(a)


# # 第五次

# In[25]:


def heap_function(List,n,i):
    odd = 2*n+1
    even = odd+1
    largest = i
    
        if List[odd] < i:
            largest = odd
        
        if List[even] < i:
            largest = even
        
        if List[i] != largest:
            List[i],largest = largest ,List[i]
        
    heap_function(List,n,largest)
    
def heap_sort(List):
    n = len(List)
    
    for i in range(0,n,1):
        heap_function(List,n,i)
        
    for i in range(0,n-1,1):
        List[i],List[0]=List[0],List[i]
        heap_function(List,n,0)


# In[26]:


a = [3,22,1,6,4]
heap_sort(a)


# # 第六次

# In[27]:


def heap_function(List,n,i):
    odd = 2*n+1
    even = odd+1
    largest = i
    if odd<n and even<n:
        if List[odd] < i:
            largest = odd
        
        if List[even] < i:
            largest = even
        
        if List[i] != largest:
            List[i],largest = largest ,List[i]
        
    heap_function(List,n,largest)
    
def heap_sort(List):
    n = len(List)
    
    for i in range(0,n,1):
        heap_function(List,n,i)
        
    for i in range(0,n-1,1):
        List[i],List[0]=List[0],List[i]
        heap_function(List,n,0)


# In[28]:


a = [3,22,1,6,4]
heap_sort(a)


# # 第七次

# In[ ]:


import sys
sys.setrecursionlimit(100)


# In[10]:


def heap_function(List,n,i):
    odd = 2*n+1
    even = odd+1
    largest = i
    for odd<n and even<n:
        if List[odd] < i:
            largest = odd
        
        if List[even] < i:
            largest = even
        
        if List[i] != largest:
            List[i],largest = largest ,List[i]
        
    heap_function(List,n,largest)
    
def heap_sort(List):
    n = len(List)
    
    for i in range(0,n,1):
        heap_function(List,n,i)
        
    for i in range(0,n-1,1):
        List[i],List[0]=List[0],List[i]
        heap_function(List,n,0)


# In[ ]:


a = [3,22,1,6,4]
heap_sort(a)


# In[9]:


print(a)


# # 第八次  (完成)

# In[29]:


#回去看其他網頁參考後隔3小時寫


# In[63]:


def heap_function(List,n,i):
    odd = 2*n+1
    even = odd+1
    largest = i
    if odd < n and List[i] < List[odd]: #這裡錯，後面的偶數比前面的大(i)，這樣才能換
        largest = odd
        
    if even < n and List[largest] <List[even]: #這裡也錯，因為前面已經把i換成largest
        largest = even
        
    if largest != i:
        List[i],List[largest]=List[largest],List[i]
        
        
        heap_function(List,n,largest)
    
def heap_sort(List):
    n = len(List)
    
    for i in range(n,0,-1):                #我是利用從前面去排
        heap_function(List,n,i)
        
    for i in range(n-1,0,-1):
        List[i],List[0]=List[0],List[i]
        heap_function(List,i,0)


# In[64]:


a = [8,4,1,2,3]


# In[65]:


heap_sort(a) 


# In[66]:


print(a)  #最後雖然有排序出來，但是是倒裝的


# # reference
# # https://www.runoob.com/python3/python-heap-sort.html
# # https://www.varunpant.com/posts/heap-sort

# In[ ]:




