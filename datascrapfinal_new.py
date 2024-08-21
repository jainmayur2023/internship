#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip install requests')
get_ipython().system('pip install bs4')


# In[3]:


import requests
from bs4 import BeautifulSoup as Bs
import pandas as pd


# # Question 1- IMDB

# In[23]:


page=requests.get('https://www.imdb.com/list/ls056092300/')
page


# In[7]:


page.content


# In[ ]:


movies=[]
for i in soup.find_all('h3',class_='ipc-title__text'):
    movies.append(i.text)
    
rating=[]
for i in soup.find_all('span',class_='ipc-rating-star--rating'):
    rating.append(i.text)
    
year=[]
year_container=soup.find_all('span',class_='sc-b189961a-8')
for i in year_container:
    if len(i.text==4) and i.text.isdigit():
    year.append(i.text)
    
df1= pd.DataFrame({'Movie Title':movies,'Year Of Release':year,'Rating':rating})
df1


# # Q2. patreon.com

# In[61]:


page2=requests.get("https://www.patreon.com/coreyms")
page2


# In[62]:


soup=Bs(page2.content)
soup
#In this question when I am printing Soup, it is not capturing the full informatiom from the site.
#Might be site has some restrictions.But I have solved the question by finding out the tags and class names. 


# In[67]:


postname=[]
for i in soup.find_all('span',class_="sc-1cvoi1y-0 hxhWXn"):
    postname.append(i.text)
    
date=[]
for i in soup.find_all('span',id="track-click"):
    date.append(i.text)

content=[]
for i in soup.find_all('div',class_="sc-cfnzm4-0 daxSFj"):
    content.append(i.text)

likes=[]
for i in soup.find_all('span',class_="sc-iqseJM"):
    likes.append(i.text)
    
df=pd.DataFrame({'Postname':postname,'Content':content,'Date':date,'Likes':likes})
df
     


# # Q3. House Details

# In[85]:


page2=requests.get("https://www.nobroker.in/property/sale/bangalore/multiple?searchParam=W3sibGF0IjoxMi45MzA3NzM1LCJsb24iOjc3LjU4MzgzMDIsInBsYWNlSWQiOiJDaElKMmRkbFo1Z1ZyanNSaDFCT0FhZi1vcnMiLCJwbGFjZU5hbWUiOiJKYXlhbmFnYXIifSx7ImxhdCI6MTIuOTc4MzY5MiwibG9uIjo3Ny42NDA4MzU2LCJwbGFjZUlkIjoiQ2hJSmtRTjNHS1FXcmpzUk5oQlFKcmhHRDdVIiwicGxhY2VOYW1lIjoiSW5kaXJhbmFnYXIifSx7ImxhdCI6MTIuOTk4MTczMiwibG9uIjo3Ny41NTMwNDQ1OTk5OTk5OSwicGxhY2VJZCI6IkNoSUp4Zlc0RFBNOXJqc1JLc05URy01cF9RUSIsInBsYWNlTmFtZSI6IlJhamFqaW5hZ2FyIn1d&radius=2.0&city=bangalore&locality=Jayanagar,Indiranagar,Rajajinagar#signup-login")
page2
soup=Bs(page2.content)


# In[86]:


house=[]
for i in soup.find_all('a',class_="overflow-hidden"):
    house.append(i.text)

loc=[]
for i in soup.find_all('div',class_="mt-0.5p overflow-hidden overflow-ellipsis whitespace-nowrap max-w-70 text-gray-light leading-4 po:mb-0.1p po:max-w-95"):
    loc.append(i.text)
    
price=[]
for i in soup.find_all('div',class_="font-semi-bold heading-6"):
    span_tag = i.find('span')
    if span_tag and len(span_tag.text)>1:
        #print(span_tag)
        #print(span_tag.text)
        price.append(span_tag.text)
        
emi=[]
for i in soup.find_all('div',id="roomType"):
    emi.append(i.text)
    
area=[]
for i in soup.find_all('div',id='unitCode'):
    area.append(i.text)
    
df3=pd.DataFrame({'House Title':house,'Location':loc,'Price':price,'EMI':emi,'Area':area})
df3


# # Q4 Bewakoof

# In[75]:


page4=requests.get("https://www.bewakoof.com/bestseller?sort=popular")
page4
soup=Bs(page4.content)


# In[78]:


pname=[]
for i in soup.find_all('div',class_="productNaming bkf-ellipsis"):
    pname.append(i.text)

price=[]
for i in soup.find_all('div',class_="discountedPriceText"):
    price.append(i.text)

image = []
for i in soup.find_all("img",class_="productImgTag"):
    image.append(i['src'])

df4=pd.DataFrame({'Product Name':pname,'Price':price,'Image Link':image})
df4


# # Q5 CNBC

# In[79]:


page5=requests.get("https://www.cnbc.com/world/?region=world")
page5
soup=Bs(page5.content)


# In[81]:


heading5=[]
for i in soup.find_all('a',class_="LatestNews-headline"):
    heading5.append(i.text)
    
       
time=[]
for i in soup.find_all('time',class_="LatestNews-timestamp"):
    time.append(i.text)
    
newslink=[]
for i in soup.find_all('a',class_="LatestNews-headline"):
    newslink.append(i['href'])
    
df5=pd.DataFrame({'Headline':heading5,'Time':time,'News Link':newslink})
df5


    


# # Q6 Keaipublishing

# In[82]:


page6=requests.get("https://www.keaipublishing.com/en/journals/artificial-intelligence-in-agriculture/most-downloaded-articles/")
page6
soup=Bs(page6.content)


# In[84]:


papertitle=[]
for i in soup.find_all('h2',class_="h5 article-title"):
    papertitle.append(i.text.replace('\n','').replace('\r',''))

author=[]
for i in soup.find_all('p',class_="article-authors"):
    author.append(i.text)

date=[]
for i in soup.find_all('p',class_="article-date"):
    date.append(i.text)
    
df6=pd.DataFrame({'Paper Title':papertitle,'Author':author,'Date':date})
df6


# In[ ]:




