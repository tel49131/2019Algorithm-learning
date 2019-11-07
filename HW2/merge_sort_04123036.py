#!/usr/bin/env python
# coding: utf-8

# # 第一次

# In[7]:


# 分割
a = [12,88,1,2,37,54,4]
n= len(a)
middle = int(len(a)/2)
middle
b = a[:middle]
c = a[middle:]
b_ = int(len(b)/2)
d = b[:b_]
e = b[b_:]
c_ = int(len(c)/2)
f = c[:c_]
g =c[c_:]
e_ = int(len(e)/2)
h =e[:e_]
i = e[e_:]
f_ = int(len(f)/2)
j = f[:f_]
k = f[f_:]
g_ = int(len(g)/2)
l = g[:g_]
m = g[g_:]

# 這方法實在太蠢，而且不是一個function


# # 第二次

# In[8]:


# 想想想
def cutfunction(List):
    middle = int(len(List))
    left = List[:middle]
    right = List[middle:]
    cutfunction(left)
    cutfunction(right)
    
    
    


# In[9]:


a = [3,2,1,5,7,8]
cutfunction(a)


# # 第三次

# In[10]:


def cutfunction(List):
    middle = int(len(List))
    left = List[:middle]
    right = List[middle:]
    keep_left = cutfunction(left)   #這一行參考網路，但不是直接抄，理解過後5小時寫
    keep_right = cutfunction(right)
    return keep_left + keep_right


# In[11]:


a = [3,2,1,5,7,8]
cutfunction(a)


# In[2]:


#還是不行，還是錯誤，回去重新學習，先把問題放著
#我先去寫合併部分


# # 合併第一次

# In[1]:


def mergesort(left_list,right_list):
    if left_list[0]<right_list[0]:
        return left_list[0]+mergesort([left_list[1:]+right_list])
    elif right_list[0]<left_list[0]:
        return right_list[0]+mergesort([right_list[1:]+left_list])
    else:
        return left_list+right_list
    
    if len(left_list) == 0:
        return right_list
    elif len(right_list) == 0:
        return left_list
        


# In[2]:


a = [1,4,6,2,3]
b = [4,2,7,5,9]


# In[3]:


mergesort(a,b)


# # 第二次

# In[5]:


#根據上面的錯誤，我知道我錯在哪
#我左右邊放錯


# In[11]:


def mergesort(left_list,right_list):
    if left_list[0]<right_list[0]:
        return left_list[0]+mergesort([left_list[1:]+right_list])
    elif right_list[0]<left_list[0]:
        return right_list[0]+mergesort([left_list+right_list[1:]])
    else:
        return left_list+right_list
    
    if len(left_list) == 0:
        return right_list
    elif len(right_list) == 0:
        return left_list


# In[12]:


a = [1,4,6,2,3]
b = [4,2,7,5,9]


# In[13]:


mergesort(a,b)


# # 第三次

# In[14]:


def mergesort(left_list,right_list):
    if left_list[0]<right_list[0]:
        return [left_list[0]]+mergesort(left_list[1:]+right_list)
    elif right_list[0]<left_list[0]:
        return [right_list[0]]+mergesort(left_list+right_list[1:])
    else:
        return left_list+right_list
    
    if len(left_list) == 0:
        return right_list
    elif len(right_list) == 0:
        return left_list


# In[15]:


a = [1,4,6,2,3]
b = [4,2,7,5,9]


# In[16]:


mergesort(a,b)


# # 第四次

# In[ ]:


#都是同樣的錯誤，後來我重新回去看一下網上的參考，我就發現錯誤了。
#因為在第三行那邊我原本是寫left_list[1:]和right_list要加起來，但其實在那一條裡面他們是家不起來的，我並沒有給right_list東西加。
#所以我後來想說是把他們當作分開的兩種，然後是外面相加。因為前面已經比過大小，是左邊的比較小，所以左邊的放下去才在加右邊繼續比大小的值。


# In[45]:


def mergesort(left_list,right_list):
    if left_list[0]<right_list[0]:
        return [left_list[0]]+ mergesort(left_list[1:],right_list)
    elif right_list[0]<left_list[0]:
        return [right_list[0]]+ mergesort(left_list,right_list[1:])
    else:
        return left_list+right_list
    
    if len(left_list) == 0:
        return right_list
    elif len(right_list) == 0:
        return left_list


# In[49]:


a = [1,4,6,2,3]
b = [1,2,7,5,9]


# In[50]:


mergesort(a,b)


# In[51]:


print(mergesort(a,b))


# # 繼續寫分割

# In[26]:


def cutfunction(List):
    middle = int(len(List)/2)
    left= List[:middle]
    right = List[middle:]
    cutfunction(left)   #這一行參考網路，但不是直接抄，理解過後5小時寫
    cutfunction(right)
    return mergesort(left,right)


# In[27]:


c =[6,3,8,9,7]


# In[28]:


print(cutfunction(c))


# # 新版

# In[15]:


# 因為一直錯，所以參考其他網路後3小時自己寫


# In[14]:


def mergesort(List):
    n = len(List)
    if n != 0:                   #先做切割
        middle = int(len(List))
        left_list = List[:middle]
        right_list = List[middle:]
        mergesort(left_list)
        mergesort(right_list)
    else:
        return List
    
    left_index = 0              #初設預設值，且是list裡的
    right_index = 0
    merge_index = 0
    while left_index <= len(left_list) and right_index <= len(right_list):  #分三個狀況 第一個是左右裡面的值都小於分割後左右list的長度
        if left_list[left_index] < right_list[right_index]:
            left_list[left_index] = merge_index                            
            left_index = left_list +1                                            
        else: 
            right_list[right_index] < left_list[left_index]
            right_list[right_index] = merge_index                          
            right_index = right_list+1
                
    while left_index < len(left_list):                                       #第二個狀況是，把左邊拿出來比較
        if right_list[right_index] < left_list[left_index]:
            right_list[right_index] = merge_index
            right_index = right_list+1
            
    while right_index < len(right_list):                                      #第三個狀況是，把右邊拿出來比較
        if right_list[right_index] < left_list[left_index]:
            right_list[right_index] = merge_index
            right_index = right_list+1
            
    
        
            
    


# In[16]:


def mergesort(List):
    n = len(List)
    if n != 0:                   #先做切割
        middle = int(len(List))
        left_list = List[:middle]
        right_list = List[middle:]
        mergesort(left_list)
        mergesort(right_list)
    else:
        return List
    
    left_index = 0              #初設預設值，且是list裡的
    right_index = 0
    merge_index = 0
    while left_index <= len(left_list) and right_index <= len(right_list):  #分三個狀況 第一個是左右裡面的值都小於分割後左右list的長度
        if left_list[left_index] < right_list[right_index]:
            left_list[left_index] = List[merge_index]                             #這一行有問題，改成List裡的merge_index
            left_index = left_index +1                                            #不是left_list要加1 因為left_list是原本的list,現在要變的是list裡面的值
        else:                                                                     #因為上面已經有if條件，else這裡本來就不用再加條件
            right_list[right_index] = List[merge_index]                           #這一行也是，改成List裡的merge_index
            right_index = right_index+1                                           #不是right_list要加1 因為right_list是原本的list,現在要變的是list裡面的值
                
    while left_index < len(left_list):                                           #第二個狀況是，把左邊拿出來比較
        if right_list[right_index] < left_list[left_index]:
            right_list[right_index] = List[merge_index]
            right_index = right_list+1
            
    while right_index < len(right_list):
        if right_list[right_index] < left_list[left_index]:
            right_list[right_index] = List[merge_index]
            right_index = right_list+1


# In[18]:


def mergesort(List):
    n = len(List)
    if n != 0:                   #先做切割
        middle = int(len(List))
        left_list = List[:middle]
        right_list = List[middle:]
        mergesort(left_list)
        mergesort(right_list)
    else:
        return List
    
    left_index = 0              #初設預設值，且是list裡的
    right_index = 0
    merge_index = 0
    while left_index <= len(left_list) and right_index <= len(right_list):  #分三個狀況 第一個是左右裡面的值都小於分割後左右list的長度
        if left_list[left_index] < right_list[right_index]:
            List[merge_index] = left_list[left_index]                             #這一行有問題，改成List裡的merge_index,並且是merge_index是left_index
            left_index = left_index +1                                            #不是left_list要加1 因為left_list是原本的list,現在要變的是list裡面的值
        else:                                                                     #因為上面已經有if條件，else這裡本來就不用再加條件
            List[merge_index] = right_list[right_index]                           #這一行也是，改成List裡的merge_index,並且是merge_index是right_index
            right_index = right_index+1                                           #不是right_list要加1 因為right_list是原本的list,現在要變的是list裡面的值
    
    List[merge_index] = merge_index +1
    
    while left_index < len(left_list):                                           #第二個狀況是，把左邊拿出來比較
        if right_list[right_index] < left_list[left_index]:
            List[merge_index] = right_list[right_index]                          #同上面 merge_index是left_index
            right_index = right_list+1
            
    while right_index < len(right_list):
        if right_list[right_index] < left_list[left_index]:
            List[merge_index] = right_list[right_index]                         #同上面 merge_index是right_index
            right_index = right_list+1


# In[21]:


# 後來回去看網頁的教學 我知道我錯在哪裡了


# In[11]:


def mergesort(List):
    n = len(List)
    if n != 0:                   #先做切割
        middle = len(List)//2
        left_list = List[:middle]
        right_list = List[middle:]
        mergesort(left_list)
        mergesort(right_list)
    
        left_index = 0;              #初設預設值，且是list裡的
        right_index = 0;
        merge_index = 0;
        while left_index < len(left_list) and right_index < len(right_list):       #分三個狀況 第一個是左右裡面的值都小於分割後左右list的長度
            if (left_list[left_index] < right_list[right_index]):
                List[merge_index] = left_list[left_index]                             #這一行有問題，改成List裡的merge_index,並且是merge_index是left_index
                left_index = left_index +1                                            #不是left_list要加1 因為left_list是原本的list,現在要變的是list裡面的值
            else:                                                                     #因為上面已經有if條件，else這裡本來就不用再加條件
                List[merge_index] = right_list[right_index]                           #這一行也是，改成List裡的merge_index,並且是merge_index是right_index
                right_index = right_index+1                                           #不是right_list要加1 因為right_list是原本的list,現在要變的是list裡面的值
    
            merge_index = merge_index +1                                                  #因為我這裡已經將left_index和right_index都指成merge_index,
                                                                                  #所以這裡他要加一才能再繼續動，而且不是list裡的，是merge_index值
    
        while left_index < len(left_list):                                       #第二個狀況是，整理左邊的數
            List[merge_index] = left_list[left_index]                          #同上面 merge_index是left_index
            left_index = left_list+1                                           
            merge_index = merge_index +1                                         #因為我這裡已經將left_index指成merge_index,
                                                                                #所以這裡他要加一才能再繼續動，而且不是list裡的，是merge_index值
            
        while right_index < len(right_list):
            List[merge_index] = right_list[right_index]                         #同上面 merge_index是right_index
            right_index = right_list+1
            merge_index = merge_index +1                                        #因為我這裡已經將right_index指成merge_index,
                                                                                #所以這裡他要加一才能再繼續動，而且不是list裡的，是merge_index值


# In[12]:


Numbers = [41, 33, 17, 80, 61, 5, 55]
mergesort(Numbers)
print(Numbers)


# # 完成

# In[30]:


def mergesort(List):
    if len(List) > 1:
        middle = int(len(List)/2)
        left_list = List[:middle]
        right_list = List[middle:]

        Merge_Sort(left_list)
        Merge_Sort(right_list)

        right_index = 0;
        left_index = 0;
        merged_index = 0;
        while left_index < len(left_list) and right_index < len(right_list):#分三個狀況 第一個是左右裡面的值都小於分割後左右list的長度
            if(left_list[left_index] < right_list[right_index]):#這一行有問題，改成List裡的merge_index,並且是merge_index是left_index
                List[merged_index] = left_list[left_index] #不是left_list要加1 因為left_list是原本的list,現在要變的是list裡面的值
                left_index = left_index + 1 #因為上面已經有if條件，else這裡本來就不用再加條件
            else:
                List[merged_index] = right_list[right_index] #這一行也是，改成List裡的merge_index,並且是merge_index是right_index
                right_index = right_index + 1 #不是right_list要加1 因為right_list是原本的list,現在要變的是list裡面的值

            merged_index = merged_index + 1#因為我這裡已經將left_index和right_index都指成merge_index,
                                           #所以這裡他要加一才能再繼續動，而且不是list裡的，是merge_index值
            
        while right_index < len(right_list): #第二個狀況是，整理右邊的數
            List[merged_index] = right_list[right_index] #同上面 merge_index是left_index
            right_index = right_index + 1
            merged_index = merged_index + 1 #因為我這裡已經將right_index指成merge_index,
                                            #所以這裡他要加一才能再繼續動，而且不是list裡的，是merge_index值

        while left_index < len(left_list):
            List[merged_index] = left_list[left_index]
            left_index = left_index + 1
            merged_index = merged_index + 1 #因為我這裡已經將left_index指成merge_index,
                                            #所以這裡他要加一才能再繼續動，而且不是list裡的，是merge_index值


# In[32]:


Numbers = [7,3,9,0,2,0]
mergesort(Numbers)
print(Numbers)


# # reference
# # https://newaurora.pixnet.net/blog/post/224658923-%E5%90%88%E4%BD%B5%E6%8E%92%E5%BA%8F%E6%B3%95---%E4%BD%BF%E7%94%A8python
# # https://medium.com/appworks-school/%E5%88%9D%E5%AD%B8%E8%80%85%E5%AD%B8%E6%BC%94%E7%AE%97%E6%B3%95-%E6%8E%92%E5%BA%8F%E6%B3%95%E9%80%B2%E9%9A%8E-%E5%90%88%E4%BD%B5%E6%8E%92%E5%BA%8F%E6%B3%95-6252651c6f7e
# 

# In[ ]:




