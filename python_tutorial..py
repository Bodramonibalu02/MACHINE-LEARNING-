#!/usr/bin/env python
# coding: utf-8

# In[1]:


bottle="thumsup"


# In[2]:


bottle


# In[3]:


type(bottle)


# In[10]:


first_name="balu"
last_name="bodramoni"


# In[11]:


first_name
last_name


# In[12]:


apple=100
apple


# In[13]:


banana=60


# In[14]:


banana


# In[15]:


carrot=30.5
carrot


# In[16]:


type(apple)


# In[17]:


type(carrot)


# In[18]:


total=apple+banana+carrot
total


# In[19]:


type(total)


# In[20]:


pi=22/7
pi


# In[21]:


type(pi)


# In[22]:


for=4
for


# In[26]:


principal_amount=100000
rate_of_intrest=3.5
time=2
simple_intrest=(principal_amount*rate_of_intrest*time)/100
simple_intrest


# In[27]:


a=10
a


# In[28]:


id(a)


# In[30]:


b=a


# In[31]:


b


# In[32]:


id(b)


# In[33]:


b=2
b


# In[34]:


id(b)


# In[37]:


base=7
height=10.888
area=(1/2)*base*height
area


# In[38]:


2+2


# In[39]:


2+2*10


# In[40]:


(2+2)*10


# In[46]:


foo=2.9e4#2.3*10**4
foo


# In[43]:


2.4*10**4


# In[49]:


format(9,"b")


# In[50]:


format(145,'o')


# In[54]:


pi=3.14
radius=84
area=pi*(radius**2)
area


# In[55]:


distance=490
time=7
speed=distance/time


# In[56]:


speed


# In[57]:


round(speed)


# In[62]:


first_name="balu"
last_name="bodramoni"
name=first_name+" " +last_name


# In[63]:


name


# In[65]:


name=f"{first_name} {last_name} age is 21"


# In[66]:


name


# In[68]:


name[23]


# In[69]:


name[24]


# In[72]:


name[0:3]


# In[73]:


name[0:4]


# In[74]:


name[:4]


# In[75]:


name[4:4]


# In[76]:


name


# In[78]:


name[-2]


# In[79]:


name[-9:]


# In[82]:


name[-9:]


# In[83]:


my_foods='samosa,panipuri'
my_foods


# In[87]:


"samosa" in my_foods


# In[88]:


"salad" in my_foods


# In[89]:


"salad" not in my_foods


# In[92]:


my_food_story="balu's favourite food is apple"


# In[93]:


my_food_story


# In[94]:


my_review='hyderabad"s best haleem is found at pista house ,king house ,mehfil, lucky,nilouferr, all these places are the best places in hyderabad to try out the haleem in ramzan '


# In[95]:


my_review


# In[96]:


s='patient is charged 50$ in hospital'
s


# In[100]:


s.replace("50$","10$")


# In[101]:


s


# In[102]:


s=s.replace("50$","10$")


# In[103]:


s


# In[106]:


dir(s)


# In[108]:


s.index('is')


# In[109]:


s.strip()


# In[110]:


a='     banana    '
a.strip()


# In[111]:


a.upper()


# In[112]:


txt='my age is '
age=21
txt+age


# In[113]:


str(age)


# In[115]:


txt+str(age)+'years'


# In[123]:


height=171
weight=58
patientinfo=f'height is {height} cm\nweight is {weight} kg '


# In[129]:


print(patientinfo)


# In[128]:


s="hai\tbro"
print(s)


# In[130]:


help(str)


# In[133]:


x="apple",'banana'
y='spinach'
print(f"I eat {y} vegetables and {x} fruits daily")


# In[136]:


text="The Himalayas are one of the youngest mountain ranges on the planet."


# In[137]:


text


# In[139]:


text[:13]


# In[147]:


text[-30:-15]


# In[148]:


text[:13]


# In[150]:


text[-14:]


# In[156]:


text[:13]+" "+text[-14:]


# In[154]:


print(f"{text[:13]} {text[-14:]}")


# In[159]:


string= "There are 9 planets in the solar system"
string.replace("9","8")


# In[160]:


item1="bread"
item2='jam'
item3="pasta"
item4='fruits'


# In[161]:


item1


# In[162]:


items=['bread','jam','pasta','fruits']


# In[163]:


items


# In[164]:


items[0]


# In[165]:


items.append("chokie")


# In[166]:


items


# In[170]:


items.insert(1,"butter")


# In[171]:


items


# In[172]:


items.remove("pasta")
items


# In[173]:


"butter" not in items


# In[192]:


avengers  = ["Iron Man", "Captain America", "Black Widow", "Hulk", "Thor", "Hawkeye"]
avengers


# In[193]:


len(avengers)


# In[194]:


avengers.append("Spider Man")


# In[195]:


avengers


# In[196]:


avengers.remove("Iron Man")


# In[197]:


avengers


# In[198]:


avengers.remove("Black Widow")


# In[199]:


avengers


# In[200]:


avengers.insert(2,"Black Widow")


# In[201]:


avengers


# In[202]:


avengers.clear()


# In[203]:


avengers


# In[206]:


avengers.append("doctor strange")
avengers.append('vision')
avengers.append('wanda')
avengers.append('kante bishop')
avengers.append('ant-man')


# In[207]:


avengers


# In[208]:


avengers.sort()


# In[209]:


avengers


# In[218]:


height=int(input("enter your height in meters:"))
weight=int(input("enter your weight:"))
bmi=weight/(height)**2
print(bmi)
if bmi >= 30:
    print('obesity')
elif bmi >=25 and bmi <= 29:
    print("over weight")
elif bmi >=18.5 and bmi <=24:
    print("normal")
else:
    print("under weight")


# In[222]:


India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]
USA = ["New York","Chicago","Las Vegas", "San Francisco"]
UK = ["London", "Manchester", "Liverpool", "Nottingham"]
city=input("enter city named:")
if city in India:
    print(f"{city} city in india")
elif city in USA:
    print(f"{city} city in USA")
elif city in UK:
    print(f"{city} city in UK")   
else:
          print('i dont know')
    


# In[223]:


city1=input('enter a city name:')
city2=input('enter a city name:')
if city1 and city2 in India:
    print("both cities are in india")
else:
    print("none")


# In[226]:


count=0
transactions = [(456, 'f'), (457, 'n'), (458, 'w'), (459, 'f')]
for transaction in transactions:
    if transaction[1]!='f':
        count+=1
print(count)        


# In[230]:


for i in range(2,1001,2):
    print(i)


# In[232]:


range(5)


# In[233]:


list(range(0,5))


# In[234]:


expenses=[1000,8900,2457,2879,7672]
totalexpense=0
for expense in expenses:
    totalexpense=totalexpense+expense
print(totalexpense)


# In[239]:


for i in range(len(expenses)):
    print(i+1)
    print(expenses[i])


# In[250]:


totalexpense=0
for i in range(len(expenses)):
    print(f"month {i+1} expenses {expenses[i]}")
    totalexpense=totalexpense+expenses[i]
    
print(f"totalexpenses={totalexpense}")    


# In[252]:


expenses=[1000,8900,2457,2879,7672]
for i ,v in enumerate(expenses):
    print(i+1,v)


# In[259]:


for i in range(1,6):
    print(i,end=" ")

    


# In[274]:


for i in range(5,0,-1):
   for j in range(1,i+1):
    print(j, end=" ")
   print() 
    


# In[285]:


for i in range(5,0,-1):
    for j in range(1,i+1):
        print(j,end=' ')
    print()


# In[288]:


n=int(input("enter no of rows;"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()    


# In[291]:


n=int(input("enter no of rows;"))
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print() 


# In[293]:


sum=0
for i in range(1,7):
    if i%2==0:
        sum=sum+i
print(sum)        


# In[296]:


sum=0
for i in range(0,7,2):
     sum=sum+i
print(sum) 


# In[301]:


n=int(input())
count6=0
dice_result  = [5,6,4,2,5,4,4,5,3,3,2,6,1,2,1,1,6,5]
for i in dice_result:
    if i==n:
        count6=count6+1       
print(count6)   


# In[ ]:


pushups=50
if pushups==10:
    print("are you tired?")
    


# In[307]:


n=int(input("enter no of rows"))
for i in range(n,1,-1):
    for j in range(1,n):
        print(j,end=" ")
    print()    


# In[313]:


n=int(input("enter no of rows"))
for i in range(n,0,-1):
   for j in range(1,i+1):
    print(j,end=" ")
   print() 


# In[314]:


for i in range(3):
    for j in range(2):
        print("i =", i, "j =", j)
        


# In[328]:


for i in range(0,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()    


# In[337]:


balu_expenses=[1001,2003,28878,18772]
virat_expenses=[1,2,3]
total=0
for expense in balu_expenses:
    total=total+expense
print(total)

for expense in virat_expenses:
    total=total+expense
print(total)
    


# In[343]:


def total_amount(expenses):
    total=0
    for expense in expenses:
        total=total+expense
    return   

    





balu=[1001,2003,28878,18772]
virat=[1,2,3]


print(total_amount(virat))


# In[347]:


#pirh


def area_cyclinder(r,h):
    pi=3.14
    area=pi*r**2*h
    return area
radius=int(input())
height=int(input())
area_cyclinder(radius,height)


# In[346]:


3.14*6**2*7


# In[351]:


def even_odd(number):
    if number%2==0:
        print("even")
    else:
      print("odd")
num=int(input("enter a number:")) 
print(even_odd(num))


# In[359]:


n=int(input())
if n%2==0:
    for i in range(n,0,-1):
        for j in range(1,i+1):
            print("*",end=" ")
        print()    
else:
    for i in range(1,n+1):
        for j in range(1,i+1):
            print("*",end=" ")
        print()  
    


# In[363]:


def pattern_print(n):
    if n%2==0:
      for i in range(n,0,-1):
        for j in range(1,i+1):
            print("*",end=" ")
        print()    
    else:
        for i in range(1,n+1):
            for j in range(1,i+1):
                print("*",end=" ")
            print() 
            
            

print(pattern_print(6))


# In[366]:


import numpy as np
arr=np.array([1,2,3])
arr


# In[367]:


arr.ndim


# In[381]:


arr1=np.array([[1,2,3],[1,2,3]])
arr1.ndim


# In[383]:


arr1[0,2]


# In[ ]:




