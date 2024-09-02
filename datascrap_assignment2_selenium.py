#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install selenium')


# In[2]:


from selenium import webdriver
from selenium.webdriver.common.by import By
import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import time


# In[8]:


driver=webdriver.Chrome()
driver.get('https://www.naukri.com')


# In[9]:


designation=driver.find_element(By.CLASS_NAME, "suggestor-input ")
designation.send_keys('Data Analyst')
search=driver.find_element(By.CLASS_NAME,"qsbSubmit")
search.click()

#loc=driver.find_element(By.XPATH,"/html/body/div/div/main/div[1]/div[1]/div/div/div[2]/div[4]/div[2]/div[3]/label/p/span[1]")
#loc.click()

#salary=driver.find_element(By.XPATH,"/html/body/div/div/main/div[1]/div[1]/div/div/div[2]/div[5]/div[2]/div[2]/label/p/span[1]")
#slary.click()

job_title=[]
job_tag=driver.find_elements(By.XPATH,"/html/body/div/div/main/div[1]/div[2]/div[2]/div/div[1]/div/div[1]/a")
for i in job_tag[0:10]:
    title=i.text
    job_title.append(title)
    
#print(job_title)
#print(len(job_title))
time.sleep(10)

job_location=[]
loc=driver.find_elements(By.CLASS_NAME,"locWdth")
for i in loc[0:10]:
    location=i.text
    job_location.append(location)
    
#print(job_location)
#Print(len(job_location))

time.sleep(10)

company_name=[]
comp=driver.find_elements(By.CLASS_NAME," comp-name mw-25")
for i in comp[0:10]:
    company=i.text
    company_name.append(company)
#print(company_name)
#print(len(company_name))  
time.sleep(10)

experience=[]
exp=driver.find_elements(By.CLASS_NAME,"expwdth")
for i in exp[0:10]:
    expr=i.text
    experience.append(expr)
    
#print(experience)
#print(len(experience))
time.sleep(10)

df=pd.DataFrame({'Job Title':job_title,'Location':job_location,'Company':company_name,'Experience':experience})
df


# # QUES 2

# In[ ]:


driver=webdriver.Chrome()
driver.get('https://www.Shine.com')
designation=driver.find_element(By.ID, "id_q")
designation.send_keys('Data Analyst')
location=driver.find_element(By.ID, "id_loc")
location.send_keys('Bangalore')
search=driver.find_element(By.CLASS_NAME," btn btn-secondary undefined")
search.click()
job_title=[]
job_tag=driver.find_elements(By.XPATH,"//strong[@class='jobCard_pReplaceH2__xWmHg']/a/]")
for i in job_tag[0:10]:
    title=i.text
    job_title.append(title)
    
print(job_title)
print(len(job_title))
time.sleep(10)

job_location=[]
loc=driver.find_elements(By.XPATH,"/html/body/div[1]/div[2]/div[4]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]']")
for i in loc[0:10]:
    location=i.text
    job_location.append(location)
    
print(job_location)
print(len(job_location))

time.sleep(10)

company_name=[]
comp=driver.find_elements(By.CLASS_NAME,"jobCard_jobCard_cName__mYnow")
for i in comp[0:10]:
    company=i.text
    company_name.append(company)
print(company_name)
print(len(company_name))  
time.sleep(10)

experience=[]
exp=driver.find_elements(By.CLASS_NAME,"jobCard_jobCard_lists_item__YxRkV jobCard_jobIcon__3FB1t")
for i in exp[0:10]:
    expr=i.text
    experience.append(expr)
    
print(experience)
print(len(experience))
time.sleep(10)

df=pd.DataFrame({'Job Title':job_title,'Location':job_location,'Company':company_name,'Experience':experience})
df


# # QUES 3

# In[214]:


driver2=webdriver.Chrome()
driver2.get('https://www.flipkart.com/apple-iphone-11-black-64-gb/product-reviews/itm4e5041ba101fd?pid=MOBFWQ6BXGJCEYNY&lid=LSTMOBFWQ6BXGJCEYNYZXSHRJ&marketplace=FLIPKART')



# In[206]:


customer_stars=[]
start=0
end=10
for page in range(start,end):
    #rating=driver2.find_elements(By.CLASS_NAME,"XQDdHH Ga3i8K")
    rating=driver2.find_elements(By.XPATH,"//div[@class='XQDdHH Ga3i8K']")
    for i in rating[0:100] :
         rating=i.text
         customer_stars.append(rating)
    next_button=driver2.find_element(By.XPATH,"/html/body/div/div/div[3]/div/div/div[2]/div[13]/div/div/nav/a")
    next_button.click()

print(customer_stars)
print(len(customer_stars))


# In[212]:


#/html/body/div/div/div[3]/div/div/div[2]/div[13]/div/div/nav/a[11]/span
#/html/body/div/div/div[3]/div/div/div[2]/div[13]/div/div/nav/a
prod_review=[]
start=0
end=10
for page in range(start,end):
    details=driver2.find_elements(By.XPATH,"//p[@class='z9E0IG']")
    for i in details[0:100]:
        det=i.text
        prod_review.append(det)
    #next_button=driver2.find_element(By.XPATH,"//a[@class='_9QVEpD']/span")
    next_button=driver2.find_element(By.XPATH,"/html/body/div/div/div[3]/div/div/div[2]/div[13]/div/div/nav/a")
    next_button.click()    
print(prod_review)
print(len(prod_review))



# In[216]:


#/html/body/div/div/div[3]/div/div/div[2]/div[13]/div/div/nav/a[11]/span
#/html/body/div/div/div[3]/div/div/div[2]/div[13]/div/div/nav/a[12]/span
#/html/body/div/div/div[3]/div/div/div[2]/div[13]/div/div/nav/a[12]/span
#/html/body/div/div/div[3]/div/div/div[2]/div[13]/div/div/nav/a[11]/spanprod_review_complete=[]
#/html/body/div/div/div[3]/div/div/div[2]/div[13]/div/div/nav/a[11]/span
prod_review_complete=[]
start=0
end=10
for page in range(start,end):
    details2=driver2.find_elements(By.XPATH,"//div[@class='ZmyHeo']/div/div")
#print(details2[1].text)
    for i in details2[0:100]:
        det2=i.text
        prod_review_complete.append(det2)
    next_button=driver2.find_element(By.XPATH,"/html/body/div/div/div[3]/div/div/div[2]/div[13]/div/div/nav/a")
    next_button.click()
print(prod_review_complete)
print(len(prod_review_complete))


# In[217]:


df=pd.DataFrame({'Product rating':customer_stars,'Review':prod_review,'Complete Review':prod_review_complete})
df


# # Ques 4

# In[163]:


driver3=webdriver.Chrome()
driver3.get('https://www.flipkart.com/search?q=sneakers&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off')








# In[154]:


#//div[@class='syl9yP']
#/html/body/div/div/div[3]/div[1]/div[2]/div[12]/div/div/nav/a[11]/span
product_brand=[]
start=0
end=3
for page in range(start,end):
    #brand=driver3.find_elements(By.CLASS_NAME,"syl9yP")
    brand=driver3.find_elements(By.XPATH,"//div[@class='syl9yP']")
    print(brand[1].text)
    for i in brand[0:34] :
        brand=i.text
        product_brand.append(brand)
    next_button=driver3.find_element(By.XPATH,"/html/body/div/div/div[3]/div[1]/div[2]/div[12]/div/div/nav")
    next_button.click()
    
print(product_brand)
print(len(product_brand))


# In[165]:


#//div[@class='hCKiGj']/div[2]/a
prod_details=[]
start=0
end=3
for page in range(start,end):
    details=driver3.find_elements(By.CLASS_NAME,"hCKiGj")
#details=driver3.find_elements(By.XPATH,"//div[@class='hCKiGj']/div[2]/a")
    print(details[0].text)
    for i in details[0:100]:
        det=i.text
        prod_details.append(det)
    next_button=driver3.find_element(By.XPATH,"/html/body/div/div/div[3]/div[1]/div[2]/div[12]/div/div/nav")
    next_button.click()
    
print(prod_details)
print(len(prod_details))


# In[171]:


#/html/body/div/div/div[3]/div[1]/div[2]/div[2]/div/div[1]/div/div/a[2]/div/div[1]
prices=[]
start=0
end=3
for page in range(start,end):
    amount=driver3.find_elements(By.CLASS_NAME,"+tlBoD")
    #amount=driver3.find_elements(By.XPATH,"a[@class='+tlBoD']/div/div[1]")
    print(amount[0].text)
    for i in amount[0:100]:
         pr=i.text
         prices.append(pr)
    next_button=driver3.find_element(By.XPATH,"/html/body/div/div/div[3]/div[1]/div[2]/div[12]/div/div/nav")
    next_button.click()
print(prices)
print(len(prices))  
#time.sleep(10)


# In[ ]:


df=pd.DataFrame({'Brand Name':prod_brand,'Description':prod_details,'Price':prices})
df


# # Ques 5

# In[123]:


driver4=webdriver.Chrome()
driver4.get('https://www.amazon.in/s?k=LAPTOP&rh=n%3A976392031%2Cp_n_feature_thirteen_browse-bin%3A12598163031&dc&ds=v1%3AdxjvMhZRkV1fqD5tq1tlISsOilJaocJjn8aphRxI%2F0Q&crid=3L6XV3TID3DYN&qid=1725280650&rnid=12598141031&sprefix=laptop%2Caps%2C255&ref=sr_nr_p_n_feature_thirteen_browse-bin_8')



    
    
    


# In[126]:


#/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[3]/div/div/span/div/div/div/div[2]/div/div/div[1]/h2/a/span
#/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[4]/div/div/span/div/div/div/div[2]/div/div/div[1]/h2/a/span
product_brand=[]

#brand=driver4.find_elements(By.CLASS_NAME,"a-size-medium a-color-base a-text-normal")
#brand=driver4.find_elements(By.XPATH,"/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[3]/div/div/span/div/div/div/div[2]/div/div/div[1]/h2/a/span")
brand=driver4.find_elements(By.XPATH,"//span[@class='a-size-medium a-color-base a-text-normal']")
#brand=driver4.find_elements(By.XPATH,"/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]")
#print(brand)
for i in brand[0:10]:
     brand=i.text
     #print(brand)
     product_brand.append(brand)
    

print(product_brand)
print(len(product_brand))


# In[137]:


#/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[4]/div/div/span/div/div/div/div[2]/div/div/div[2]/div/span[1]/span/a/i[1]/span
#/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[3]/div/div/span/div/div/div/div[2]/div/div/div[2]/div[1]/span[1]/span/a/i[1]/span
#//span[@class='a-icon-alt']
#//i[@class='a-icon a-icon-star-small a-star-small-4 aok-align-bottom']/span
#//i[@class='a-icon a-icon-star-small a-star-small-4']/span
prod_rating=[]
#ratings=driver4.find_elements(By.CLASS_NAME,"a-icon-alt")
ratings=driver4.find_elements(By.CLASS_NAME,"a-icon a-icon-star-small a-star-small-4 aok-align-bottom")

#ratings=driver4.find_elements(By.XPATH,"//i[@class='a-icon-star-small']/span")
#ratings=driver4.find_elements(By.XPATH,"/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[1]/div/div/div[1]/div/div[2]/div[2]/div/div/div/div/a[2]/div/i/span")
print(ratings)
#print(ratings[0].text)
for i in ratings[0:10]:
        rate=i.text
        prod_rating.append(rate)
        
print(prod_rating)



    


# In[48]:


prices=[]
amount=driver4.find_elements(By.CLASS_NAME,"a-price-whole")
for i in amount[0:10]:
    pr=i.text
    prices.append(pr)
        
print(prices)
print(len(prices))  
#time.sleep(10)





# In[ ]:


df=pd.DataFrame({'Brand Name':prod_brand,'Product Ratings':prod_rating,'Price':prices})
df


# # Ques6

# In[86]:


driver6=webdriver.Chrome()
driver6.get('https://www.azquotes.com/top_quotes.html')
#Quote,Author,Type of Quote


# In[92]:


title=[]
start=0
end=10
for page in range(start,end):
    #title_tag=driver6.find_elements(By.CLASS_NAME,"title")
    title_tag=driver6.find_elements(By.XPATH,"//a[@class='title']")
    #title_tag=driver6.find_elements(By.XPATH,"/html/body/div[1]/div[2]/div/div/div/div[1]/div/ul/li[1]/div/p/a[2]")
    for i in title_tag:
        tit=i.text
        title.append(tit)
    next_button=driver6.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div[1]/div/div[4]/li[12]/a')
    next_button.click()
        
#print(title_tag)
#print(title)
print(title)
print(len(title))  


# In[93]:


author=[]
start=0
end=10
for page in range(start,end):
    author_tag=driver6.find_elements(By.CLASS_NAME,"author")
    #author_tag=driver6.find_elements(By.XPATH,"//div[@class='author']/a")
    #author_tag=driver6.find_elements(By.XPATH,"/html/body/div[1]/div[2]/div/div/div/div[1]/div/ul/li[1]/div/div[1]/a")
    for i in author_tag:
        auth=i.text
        author.append(auth)
    next_button=driver6.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div[1]/div/div[4]/li[12]/a')
    next_button.click()
print(author)
print(len(author))  


# In[94]:


quote_type=[]
start=0
end=10
for page in range(start,end):
    quote_tag=driver6.find_elements(By.CLASS_NAME,"tags")
    #quote_tag=driver6.find_elements(By.XPATH,"//div[@class='tags']/a")
    #quote_tag=driver6.find_elements(By.XPATH,"/html/body/div[1]/div[2]/div/div/div/div[1]/div/ul/li[1]/div/div[2]/div[1]")
    for i in quote_tag:
        type2=i.text
        quote_type.append(type2)
    next_button=driver6.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div[1]/div/div[4]/li[12]/a')
    next_button.click()
print(quote_type)
print(len(quote_type))


# In[95]:


df=pd.DataFrame({'Title':title,'Author':author,'Quote type':quote_type})
df


# # Ques 7

# In[96]:


driver7=webdriver.Chrome()
driver7.get('https://www.jagranjosh.com/general-knowledge/list-ofall-prime-ministers-of-india-1473165149-1')


# In[102]:


prime_minister=[]
#prime_minister_tag=driver7.find_elements(By.XPATH,"//div[@class='TableData']/table/tbody/tr[2]/td[2]/a")
prime_minister_tag=driver7.find_elements(By.CLASS_NAME,"TableData")
#prime_minister_tag=driver7.find_elements(By.XPATH,"/html/body/div[1]/main/div[1]/div[1]/article/div[4]/div[9]/div[1]/table/tbody/tr[2]/td[2]/a")
print(prime_minister_tag[0].text)
for i in prime_minister_tag:
        auth=i.text
        prime_minister.append(auth)
    
        
print(len(prime_minister))
#print(prime_minister)


# # Ques 8

# In[103]:


driver8=webdriver.Chrome()
driver8.get('https://www.motor1.com/features/308149/most-expensive-new-cars-ever/')


# In[111]:


#/html/body/div[9]/div[7]/div[2]/div[1]/div[2]/div[2]/h3[4]
#/html/body/div[9]/div[7]/div[2]/div[1]/div[2]/div[2]/h3[4]/text()
#/html/body/div[9]/div[7]/div[2]/div[1]/div[2]/div[2]/h3[7]/text()
car_name=[]
car_name_tag=driver8.find_elements(By.XPATH,"/html/body/div[9]/div[7]/div[2]/div[1]/div[2]/div[2]/h3")
print(car_name_tag[0].text)
for i in car_name_tag[0:50]:
        auth=i.text
        car_name.append(auth)
    
        
print(len(car_name))
print(car_name)


# In[121]:


#/html/body/div[9]/div[7]/div[2]/div[1]/div[2]/div[2]/p[8]/strong
#/html/body/div[9]/div[7]/div[2]/div[1]/div[2]/div[2]/p[10]/strong
#/html/body/div[9]/div[7]/div[2]/div[1]/div[2]/div[2]/p[14]/strong
price=[]
price_tag=driver8.find_elements(By.XPATH,"/html/body/div[9]/div[7]/div[2]/div[1]/div[2]/div[2]/p[14]")
print(price_tag[0].text)
for i in price_tag:
    auth=i.text
    price.append(auth)
    
        
print(len(price))
print(price)


# In[ ]:




