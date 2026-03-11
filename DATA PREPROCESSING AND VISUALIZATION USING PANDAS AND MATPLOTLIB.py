#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
df=pd.read_csv("movies.csv")
df


# In[2]:


df.head(10)


# In[3]:


df.tail(3)


# In[4]:


df.sample(20)


# In[5]:


df[2:10]


# In[6]:


df.shape


# In[7]:


df["imdb_rating"] #df.imdb_rating


# In[8]:


type(df.imdb_rating)


# In[9]:


type(df)


# In[10]:


dir(df.imdb_rating)


# In[11]:


df.imdb_rating.min(),df.imdb_rating.max(),df.imdb_rating.mean()


# In[12]:


average_imbdrating=df.imdb_rating.mean()
average_imbdrating


# In[13]:


df_bollywood=df[df.industry=='Bollywood']
df_hollywood=df[df.industry=='Hollywood']
df_bollywood


# In[14]:


df_bollywood.imdb_rating.mean()


# In[15]:


df_hollywood.imdb_rating.mean()


# In[16]:


df.shape #property


# In[17]:


df.columns


# In[18]:


df.industry.unique()


# In[19]:


df['language'].unique() ## or df.language.unique()


# In[20]:


df.industry.value_counts() #value_counts() counts the value in a column 


# In[21]:


df.language.value_counts()


# In[22]:


df[['title','imdb_rating','industry']]


# In[23]:


df.head()


# In[24]:


df[(df.release_year>=2000) & (df.release_year<=2010)]



# In[25]:


df.studio.unique()


# In[26]:


df[df.studio=='DVV Entertainment']


# In[27]:


df.describe()


# In[28]:


df.info()


# In[29]:


df.imdb_rating.max()


# In[30]:


df[(df.imdb_rating==(df.imdb_rating.max()))  | (df.imdb_rating==(df.imdb_rating.min()))]


# In[31]:


df['age']=df['release_year'].apply(lambda x :2026-x)
df.head()


# In[32]:


df['profit']=df.apply(lambda x: x["revenue"]-x["budget"], axis =1)                     
df.head()


# In[33]:


df.index


# In[34]:


df.set_index('title',inplace=True)


# In[35]:


df.index


# In[36]:


df


# In[37]:


df.loc[["PK"]]


# In[38]:


df.iloc[1:3]


# In[39]:


df.iloc[1]


# In[40]:


df.reset_index(inplace=True)


# In[41]:


df=pd.read_csv("stock_data.csv")
df


# In[42]:


df=pd.read_csv("stock_data.csv",skiprows=1)
df


# In[43]:


df=pd.read_csv("stock_data.csv",header=1)
df


# In[44]:


df=pd.read_csv("stock_data.csv",header=1,names=['stocksymbol','expense','revenue','price','people'])
df


# In[45]:


df=pd.read_csv("stock_data.csv", header=1,nrows=4)
df


# In[46]:


df=pd.read_csv("stock_data.csv", header=1,na_values={
    'eps':['not available',"-1"],
    "people":["n.a."],
    'revenue':['-1'],
    'price':['n.a.']
})
df


# In[47]:


df=pd.read_csv("stock_data.csv", header=1)
df


# In[48]:


df=pd.read_csv("stock_data.csv", header=1,na_values=['not available','-1','n.a.'])
df


# In[49]:


df['pe']=df['price']/df['eps']
df


# In[50]:


df.to_csv('pe.csv')


# In[51]:


df.to_csv('pe.csv',index=False,header=1)


# In[52]:


df_movies=pd.read_excel('movies_db.xlsx','movies')
df_movies


# In[53]:


df_financials=pd.read_excel('movies_db.xlsx','financials')
df_financials.head()


# In[54]:


def standardized_currency(curr):
    if curr=='$$' or curr=="Dollars":
        return "USD"
    return curr



df_financials=pd.read_excel('movies_db.xlsx','financials',converters={
    'currency':standardized_currency
})
df_financials.head()


# In[55]:


merged_data=pd.merge(df_movies,df_financials, on="movie_id")
merged_data.head()


# In[56]:


merged_data.to_excel("movies_merged.xlsx",sheet_name="merged",index=False)


# In[57]:


df=pd.DataFrame({
    "name":['balu','virat','klrahul'],
    "num":[1,18,12]
})
df


# In[58]:


df=pd.read_csv('weather_data.csv',parse_dates=['day'])
df


# In[59]:


type(df.day[0])


# In[60]:


df.set_index("day",inplace=True)
df


# In[61]:


df.fillna({
    "temperature":df.temperature.mean(),
   "windspeed":df.windspeed.median(),
    'event':df.event.mode()
    
})


# In[62]:


df


# In[63]:


df.fillna(method="ffill")


# In[64]:


df


# In[65]:


df.fillna(method="ffill",limit=2)


# In[66]:


df.interpolate()


# In[67]:


df.dropna()


# In[68]:


df.dropna(how="any")


# In[69]:


df.dropna(how="all")


# In[70]:


df.dropna(thresh=2)


# In[71]:


df=pd.read_csv('weather_data.csv')
df


# In[72]:


df.replace([-99999,-88888],0)


# In[74]:


df.replace({
    "temperature":-99999,
    "windspeed" : [-99999,-88888],
    'event':"no event"
},np.nan)


# In[75]:


import numpy as np


# In[77]:


df.replace({
    -99999:np.nan,
    -88888:np.nan,
    "no event":'sunny'
})


# In[78]:


df=pd.DataFrame({
    "scores":['A','B','A+','O,','B'],
    'names':['balu','dhoni','virat','shreyasiyer','klrahul']
})
df


# In[79]:


df.replace(['A','B','A+','O,','B'],[3,4,2,1,4])


# In[80]:


df=pd.read_csv("weather_by_cities.csv")
df


# In[81]:


df[df.city=='new york'].temperature.max()


# In[82]:


df[df.city=='new york'].temperature.min()


# In[83]:


g=df.groupby("city")
g


# In[87]:


for city, data in g:
    print('city',city)
    print('max',data.windspeed.max())


# In[88]:


indian_weather=pd.DataFrame({
    'city':['delhi','hyd','chennai'],
    'temperature':[47,40,51],
    'humidity':[90,76,98]
})
indian_weather


# In[89]:


us_weather=pd.DataFrame({
    'city':['newyork','washington','chicago'],
    'temperature':[41,29,39],
    'humidity':[95,79,92]
})
us_weather


# In[90]:


df=pd.concat([indian_weather,us_weather])
df


# In[91]:


df=pd.concat([indian_weather,us_weather],ignore_index=True)
df


# In[92]:


df=pd.concat([indian_weather,us_weather],keys=["india","us"])
df


# In[93]:


df.loc['india']


# In[94]:


temperature_df=pd.DataFrame({
    'city':['mumbai','hyderabad','delhi'],
    'temperature':[32,45,20]
})
temperature_df


# In[95]:


windspeed_df=pd.DataFrame({
    'city':['mumbai','delhi'],
    'windspeed':[45,22]
})
windspeed_df


# In[96]:


df=pd.concat([temperature_df,windspeed_df],axis=0)
df


# In[97]:


pd.merge(temperature_df,windspeed_df ,how ='outer')


# In[98]:


df1=pd.DataFrame({
    'city':['mumbai','hyderabad','delhi','chennai'],
    'temperature':[32,45,20,21]
})
df1


# In[99]:


df2=pd.DataFrame({
    'city':['mumbai','chennai','kolkata'],
    'humidity':[52,85,71]
})
df2


# In[100]:


df3=pd.merge(df1,df2)
df3


# In[101]:


df3=pd.merge(df1,df2,how='left')
df3


# In[102]:


df3=pd.merge(df1,df2,how='right')
df3


# In[103]:


df3=pd.merge(df1,df2,how='outer')
df3


# In[104]:


import matplotlib.pyplot as plt 
df=pd.read_excel('linechart.xlsx')


# In[105]:


df


# In[106]:


plt.figure(figsize=(12,3.5))
plt.title('product sales')
plt.xlabel('quarters')
plt.ylabel('revenue in $')
plt.plot(df['Quarter'],df['Fridge'],color='blue',label='fridge')
plt.plot(df['Quarter'],df['Dishwasher'],color='red',label='dishwasher')
plt.plot(df['Quarter'],df['Washing Machine'],color='orange',label='washing machine ')
plt.legend()
plt.show()


# In[109]:


total_sales=df[['Fridge','Dishwasher','Washing Machine']].sum()
total_sales


# In[110]:


plt.pie(total_sales,labels=['fridge','dishwasher','washing machine'],autopct='%1.2f%%',shadow=True,startangle=100,explode=(0.1,0,0))



plt.show()


# In[111]:


df.plot(kind="bar",x="Quarter")
plt.xticks(rotation=45)
plt.show()


# In[112]:


import seaborn as sns 
df=pd.read_excel("histograms.xlsx")
df.head()


# In[113]:


plt.hist(df['Exam_Score'])
plt.show()


# In[114]:


sns.histplot(df['Exam_Score'] , kde=True)
plt.show()


# In[115]:


df=pd.read_excel('scatter_plot.xlsx')
df.head()


# In[116]:


sns.scatterplot( data =df,x='area_square_ft',y='price')


# In[ ]:




