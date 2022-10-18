#!/usr/bin/env python
# coding: utf-8

# # Basics

# ## Welcome

# ### EduBridge

# #### Happy Learnning

# Comments are annotations to code used to make it easier to understand. They don't affect how code is run. 
# In Python, a comment is created by inserting an octothorpe(otherwise known as a number sign or hash symbol:#).
# All text after it on that line is ignored.

# In[3]:


#first code
print("Hello, Edubridge")


# In[4]:


print("Hello, Edubridge")


# In[5]:


print("vidya")


# In[6]:


import this


# In[7]:


#to know the python version
from platform import python_version
print(python_version())


# In[8]:


import keyword #13-10-22
#there are 33 keywords


# In[9]:


#to get the list of keywords
keyword.kwlist


# In[10]:


#multiple asssignment at the same time
a=b=c=1
print(a,b,c)
a,b,c=1,2.0,"abcd"
print(a,b,c)


# #Data Types

# In[11]:


x=2-5
print(x)
print(type(x))


# In[12]:


#conoverting integer to float
a=100
print(a)
print(type(a))
x=float(a)
print(type(x))


# In[13]:


#converting float to integer
a=100.05
print(a)
print(type(a))
x=int(a)
print(type(x))


# In[14]:


#to give complex numbers
a=30+25J
print(type(a))
print(a.real)
print(a.imag)


# In[15]:


#converting int & float values to complpex numbers
a=30
b=27.0
print(type(a))
print(type(b))
x=complex(a,b)
print(x)


# In[16]:


#string
x='Hello' #single quote
y="@#$%^&*" #double quote
print(x)
print(y)
print(type(x))
print(type(y))


# In[17]:


#converting string to integer
a=input("enter first number:")
b=input("enter secod number:")
print(type(a))
print(type(b)) # by default the input takes as the string

a=int(input("enter first integer number:"))
b=float(input("enter secod float number:"))
print(type(a))
print(type(b))


# LIST 14-10-22

# list is a coma seperated, enclosed with [ ], series of words or numbers:-any datatype.
# 
# list is any array of elements.
# 
# list can be modififed & changed:-means Mutable

# In[18]:


x=[2,-33,4.5,"SAI", 1+5J] # any type of datatypes
print(x)
print(type(x))


# In[19]:


#list Indexing if left to right(foreward) starts with 0,1,2,3.... & 
#right to left(or in reverse/backward) it start with -1,-2,-3,.....
#indexx indicated the position of the specified element


# In[20]:


a=[1,500,60.375,"apple","cat"]
print(a[0])
print(a[-2])


# In[21]:


a="Welcome World"
print(a[6])
print(a[7])
print(a[-1])
print(a[-5])


# In[22]:


x=["aaa","bbb","ccc","ddd","eee","fff","ggg","hhh"]
print(x[:]) #to get all the values in list
print(x[0:3])#to get first three elements
print(x[-3:-1])# to get last second & third elements
print(x[::-1])#to get all elements in reverse order
print(c[-2:])#to get last 2 elements


# In[23]:


c=[["Hai","welcome"],"world","python"]
print(c[0])
print(c[0:1])
print(c[0:2])
print(c[-1])


#list within list
print(c[0])
print(c[0][0])
print(c[0][1])


# In[24]:


print(x)
print(x[3])
x[3]=1234
print(x[3])
print(x)


# In[25]:


#TUPLE enclosed within ( ), they are immutabe-cant be changed.
#tuples are coma separated variables of any datatype


# In[26]:


s=(1,2.5,"aaa",-8,1+2J)
print(type(s))


# In[27]:


print((s[2]))
print(s[0:2])
print(s[-3:])
#  s[2]=1   'tuple' object does not support item assignment


# In[28]:


#dictionary are coma separated with key:value as a pair, enclosed within {}, they are mutable


# In[29]:


dict={"name":"abc","age":20,"education": "inter 2.0"}
print(dict.keys())
print(dict.values())


# In[30]:


dict["name"]="aaaaa" # they are mutable
print(dict)


# In[31]:


d={"name":"abc","age":20,"education": "inter 2.0", "age":100,"place":"India"}
# multiple valuues of keys will be replaced with latest one
d


# In[32]:


del d["education"] #to delete particular key &value using key
d


# #### SETS   17-10-22

# Sets are coma seperated with {} brackets.
# sets are unoredered & unindexed unlike list(so slicing dosn't work).
# Sets not allow duplicate entries.
# Sets do not have mutable entries.

# In[33]:


s={1,2,"abc",2.2,1+2J}
print(s)
print(type(s))


# In[34]:


x={1,2,2,3,5,8,4,3,6,8,12,15,15}
x #omits multiple entries


# In[35]:


#sets cant contain mutable entries
a={1,2,3,4,[5,6]} #since list is mutable entry it will through error
a


# In[36]:


b={1,2,3,4,(5,6)} #tuple is immutable so sets will accept it
b


# In[37]:


c={1,2,3,4,{55,88,3}}
c


# #### Boolean

# In[38]:


s=False
type(s)


# ## Operators in Python

# Operators asre used to carry our operations.
# symbols used to perform action on data are called Operators
# 1) Arthimatic Operators
# 2) Logical Operators
# 3) Relational Operators
# 4) Logical Operators

# ### Arthemataic Operators

# In[39]:


#a,b are operands
# +,-,*,/,% ... are operators
a=int(input("enter first integer value(a): "))
b=int(input("enter the second integer value(b): "))
print("sum=",a+b)
print("difference=",a-b)
print("multiplication=",a*b)
print("division=",a/b)
print("power or exponent (a power b)=",a**b)
print("remainder=",a%b)
print("Quotient=",a//b) # floor division / Quotient


# ### Assignment Operators

# a=2   #assigning
# a+=2 or a=a+2 #add
# a-=3 or a=a-3  #subtract
# a*=4 or a=a*4  #multiplication
# a/=5 or a=a/5  #division
# a%=6 or a=a%6  #modulus or Remainder
# a**=7 or a=a**7 #power or exponent
# a//=8 or a=a//8 #quotient or floor division

# In[40]:


a=4
x,y,z=5,6,7


# In[41]:


print(a)


# In[42]:


a=a+2
a


# In[43]:


a+=4
a


# In[44]:


a+=x
a


# In[45]:


a-=y
a


# In[46]:


print("a",a+z)


# In[47]:


print(a-1)


# In[48]:


#print(a-=1)
#we cant perform assignment operators in print


# #### Unary number

# In[49]:


n=7
n


# In[50]:


-n


# In[51]:


n


# In[52]:


n=-n
n


# ### Relational or Comparision Operators
# 

# #a==b both  are equal
# #a!=b not equal
# #a<=b less than or equal to 
# #a>=b grater than or equal to
# #a>b  grater than
# #a<b  less than

# In[53]:


a=50
b=42
print(a==b)
print(a<b)
print(a>b)
print(a<=b)
print(a>=b)
print(a!=b)


# #### Logical Operator

# **AND**
#  T  T  T
#  F  F  F
#  F  T  F
#  T  F  F
#  
#  **OR**
#  T  T  T
#  T  F  T
#  F  T  T
#  F  F  F

# In[54]:


a,b=10,20
print(a<b or b<=a)
print(a<b and b<=a)


# In[55]:


print(a>b or b<=a)
print(a>b and b<=a)


# In[56]:


print(a>b or b==a)
print(a>b and b==a)
print(a>b or b!=a)
print(a>b and b!=a)


# In[57]:


print((1>2) or (3<6) and (5>7))


# In[58]:


a=not a
a


#     ~ means T=F, F=T
#     for integer values also it works ~n=-(n+1)

# In[59]:


n=7
print(n)
print(~n)


# ## String Manipulation

# there are two operatrs :  + , *
# + means concatenation rather than adding: "string"+"string"
# * means replication rather than multiplying: "string"*int number

# In[60]:


print("hello"+"world")# we will get them side by side i,e concateneation
print("1"+"5")
print("hello"*3)#it will repeat it thrice i.e replication: for this we need a string & number
print(2*"world")
print(5*"123 ")#space can also be given


# In[61]:


"1"+8.0
#it will give an error since string cant be added to a number(int/float)


# In[ ]:


"2"*"2" # we need string and a number, so it is error


# In[ ]:


x="hello"
y="hello world"
x in y


# In[ ]:


x not in y


# In[62]:


"abcd" in "efghi"


# In[63]:


"abcdef" not in "ghi"


# ### comoparision operators

# In[64]:


"a"=="a"


# In[65]:


"abc"=="ABC"


# In[66]:



"123"=="12a"


# In[67]:


"hello"=='hello' #single or double is same in python

