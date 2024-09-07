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


# # Question 1

# In[359]:


driver=webdriver.Chrome()
driver.get('https://www.naukri.com')


# In[360]:


designation=driver.find_element(By.CLASS_NAME, "suggestor-input ")
designation.send_keys('Data Scientist')
search=driver.find_element(By.CLASS_NAME,"qsbSubmit")
search.click()



# In[361]:


search_sal=driver.find_element(By.XPATH,"/html/body/div/div/main/div[1]/div[1]/div/div/div[2]/div[5]/div[2]/div[2]/label/i")
search_sal.click()


# In[362]:


search_loc=driver.find_element(By.XPATH,"/html/body/div/div/main/div[1]/div[1]/div/div/div[2]/div[5]/div[2]/div[3]/label/i")
search_loc.click()


# In[367]:


job_title=[]
job_tag=driver.find_elements(By.XPATH,"//div [@class=' row1']/a")
#job_tag=driver.find_elements(By.XPATH,"/html/body/div/div/main/div[1]/div[2]/div[2]/div/div[1]/div/div[1]/a")
for i in job_tag[0:10]:
    title=i.text
    job_title.append(title)
    
print(job_title)
print(len(job_title))


# In[365]:


#//div [@class=' row1']/a/
job_title=[]
job_tag=driver.find_elements(By.XPATH,"//div [@class=' row1']/a")
#job_tag=driver.find_elements(By.XPATH,"/html/body/div/div/main/div[1]/div[2]/div[2]/div/div[1]/div/div[1]/a")
for i in job_tag[0:10]:
    title=i.text
    job_title.append(title)
    
#print(job_title)
#print(len(job_title))
#//span[@class='locWdth']
job_location=[]
#loc=driver.find_elements(By.CLASS_NAME,"locWdth")
loc=driver.find_elements(By.XPATH,"//span[@class='locWdth']")
for i in loc[0:10]:
    location=i.text
    job_location.append(location)
    
#print(job_location)
#print(len(job_location))
#//span[@class=' comp-name mw-25']
#  //div[@class=' row2']
company_name=[]
#comp=driver.find_elements(By.CLASS_NAME," comp-name mw-25")
#comp=driver.find_elements(By.XPATH,"//span[@class=' comp-dtls-wrap']")
comp=driver.find_elements(By.XPATH,"//div[@class=' row2']/span/a[1]")

for i in comp[0:10]:
    company=i.text
    company_name.append(company)
#print(company_name)
#print(len(company_name))  
experience=[]
#exp=driver.find_elements(By.CLASS_NAME,"expwdth")
exp=driver.find_elements(By.XPATH,"//span[@class='exp-wrap']/span/span")
for i in exp[0:10]:
    expr=i.text
    experience.append(expr)
    
#print(experience)
#print(len(experience))
time.sleep(10)
df=pd.DataFrame({'Job Title':job_title,'Location':job_location,'company_name':company_name,'Experience':experience})
df


# # QUES 2

# In[414]:


driver2=webdriver.Chrome()
driver2.get('https://www.Shine.com')
#driver2.get('https://www.shine.com/job-search/data-scientist-jobs-in-bangalore?q=data-scientist&loc=Bangalore')


# In[ ]:


#designation=driver2.find_element(By.NAME, "id_q")
#designation=driver2.find_element(By.XPATH,"/html/body/div/div[4]/div/div[2]/div[2]/div/form/div/div[1]/ul/li[1]/div/label")
#designation.send_keys('Data Analyst')

#location=driver2.find_element(By.ID, "id_loc")
#location.send_keys('Bangalore')

#search=driver.find_element(By.CLASS_NAME," btn btn-secondary undefined")
#search.click()


# In[412]:


job_title=[]
#job_tag=driver2.find_elements(By.XPATH,"//strong[@class='jobCard_pReplaceH2__xWmHg']/a/]")
job=driver2.find_elements(By.CLASS_NAME,'jobCard_pReplaceH2__xWmHg')

for i in job[0:10]:
    title=i.text
    job_title.append(title)
    
print(job_title)
print(len(job_title))


# In[406]:


job_location=[]
#loc=driver.find_elements(By.XPATH,"/html/body/div[1]/div[2]/div[4]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]']")
#loc=driver2.find_elements(By.CLASS_NAME,'jobCard_locationIcon__zrWt2')

loc=driver2.find_elements(By.XPATH,"//div[@class='jobCard_jobCard_lists_item__YxRkV jobCard_locationIcon__zrWt2']")
#print(loc[0].text)
for i in loc[0:10]:
    location=i.text.replace('+','').replace('\n','').strip("0123456789")
    job_location.append(location)
    
print(job_location)
print(len(job_location))


# In[407]:


company_name=[]
comp=driver2.find_elements(By.CLASS_NAME,"jobCard_jobCard_cName__mYnow")
for i in comp[0:10]:
    company=i.text
    company_name.append(company)
print(company_name)
print(len(company_name))  


# In[410]:


experience=[]
#exp=driver2.find_elements(By.CLASS_NAME,"jobCard_jobCard_lists_item__YxRkV jobCard_jobIcon__3FB1t")
exp=driver2.find_elements(By.XPATH,"//div[@class=' jobCard_jobCard_lists_item__YxRkV jobCard_jobIcon__3FB1t']")
for i in exp[0:10]:
    expr=i.text
    experience.append(expr)
    
print(experience)
print(len(experience))


# In[413]:


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

# In[498]:


driver3=webdriver.Chrome()
driver3.get('https://www.flipkart.com')


# In[499]:


sneaker=driver3.find_element(By.XPATH,"//input[@class='Pke_EE']")
sneaker.send_keys('Sneakers')
sneaker.click()
search=driver3.find_element(By.XPATH,"//button[@class='_2iLD__']")
search.click()


# In[507]:


#//div[@class='syl9yP']
#/html/body/div/div/div[3]/div[1]/div[2]/div[12]/div/div/nav/a[11]/span
product_brand=[]
start=0
end=3
for page in range(start,end):
    #brand=driver3.find_elements(By.CLASS_NAME,"syl9yP")
    brand=driver3.find_elements(By.XPATH,"//div[@class='syl9yP']")
    
    for i in brand[0:40] :
        brand=i.text
        product_brand.append(brand)
    next_button=driver3.find_element(By.XPATH,"/html/body/div/div/div[3]/div[1]/div[2]/div[12]/div/div/nav")
    next_button.click()
    time.sleep(10)
print(product_brand)
print(len(product_brand))


# In[505]:


product_brand=[]
product_details=[]
product_price=[]
start=0
end=3
for page in range(start,end):
    #elements =driver4.find_elements(By.CLASS_NAME, "hCKiGj")
    for i in range(0,100):
        brand=driver3.find_elements(By.XPATH,"//div[@class='syl9yP']").text
        details=driver3.find_elements(By.CLASS_NAME,"WKTcLC").text
        price = element.find_element(By.CLASS_NAME, "Nx9bqj").text
        product_brand.append(brand)
        product_price.append(price)
        product_details.append(details)
        i=i+1
    next_button=driver3.find_element(By.XPATH,"/html/body/div/div/div[3]/div[1]/div[2]/div[12]/div/div/nav")
    next_button.click()
    time.sleep(10)
#print(product_brand)
print(len(product_brand))
print(len(product_price))
print(len(product_details))


# In[501]:


#//div[@class='hCKiGj']/div[2]/a
prod_details=[]
start=0
end=3
for page in range(start,end):
    details=driver3.find_elements(By.CLASS_NAME,"WKTcLC")
#details=driver3.find_elements(By.XPATH,"//div[@class='hCKiGj']/div[2]/a")
    #print(details[0].text)
    for i in details[0:100]:
        det=i.text
        prod_details.append(det)
    next_button=driver3.find_element(By.XPATH,"/html/body/div/div/div[3]/div[1]/div[2]/div[12]/div/div/nav")
    next_button.click()
    
print(prod_details)
print(len(prod_details))


# In[533]:


#/html/body/div/div/div[3]/div[1]/div[2]/div[2]/div/div[1]/div/div/a[2]/div/div[1]
price_list=[]
prices=[]
start=0
end=3
for page in range(start,end):
    amount=driver3.find_elements(By.CLASS_NAME,"Nx9bqj")
    #amount=driver3.find_elements(By.CLASS_NAME,"hl05eU")
     #amount=driver3.find_elements(By.XPATH,'//a[@class="+tlBoD"]/div/div')
    for i in amount[0:100]:
         pr=i.text
         prices.append(pr)
    next_button=driver3.find_element(By.XPATH,"/html/body/div/div/div[3]/div[1]/div[2]/div[12]/div/div/nav")
    next_button.click()
    price_list=prices[0:120]
#print(prices)
#print(len(prices))  
#time.sleep(10)
print(price_list)
print(len(price_list))


# In[535]:


df=pd.DataFrame({'Brand Name':product_brand[:100],'Description':prod_details[:100],'Price':price_list[0:100]})
df


# # Ques 5

# In[463]:


driver4=webdriver.Chrome()
#driver4.get('https://www.amazon.in/s?k=LAPTOP&rh=n%3A976392031%2Cp_n_feature_thirteen_browse-bin%3A12598163031&dc&ds=v1%3AdxjvMhZRkV1fqD5tq1tlISsOilJaocJjn8aphRxI%2F0Q&crid=3L6XV3TID3DYN&qid=1725280650&rnid=12598141031&sprefix=laptop%2Caps%2C255&ref=sr_nr_p_n_feature_thirteen_browse-bin_8')

driver4.get('https://www.amazon.in')


# In[464]:


search=driver4.find_element(By.XPATH,'/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input')
search.send_keys('Laptop')

button3=driver4.find_element(By.ID,'nav-search-submit-button')
button3.click()

core7=driver4.find_element(By.XPATH,"//li[@id='p_n_feature_thirteen_browse-bin/12598163031']/span/a")
core7.click()



# In[466]:


product_brand=[]
brand=driver4.find_elements(By.XPATH,"//span[@class='a-size-medium a-color-base a-text-normal']")
for i in brand[0:10]:
    brand=i.text
    product_brand.append(brand)
print(product_brand)
print(len(product_brand))


# In[467]:


prod_rating=[]
#ratings=driver4.find_elements(By.CLASS_NAME,"a-icon-alt")
#ratings=driver4.find_elements(By.CLASS_NAME,"a-icon a-icon-star-small a-star-small-4 aok-align-bottom")
#ratings=driver4.find_elements(By.XPATH,"//div[@class='a-row a-size-small']")
#ratings=driver4.find_elements(By.XPATH,"i[@class='a-icon a-icon-star-small a-star-small-4 aok-align-bottom']/span")
#ratings=driver4.find_elements(By.XPATH,"//a[@class='a-popover-trigger a-declarative']")
ratings=driver4.find_elements(By.XPATH,"//div[@class='a-row a-size-small']/span/span/a/i/span")
#ratings=driver4.find_elements(By.XPATH,"//span[@class='a-icon-alt']")
#ratings=driver4.find_elements(By.XPATH,"//i[@class='a-icon-star-small']/span")
#ratings=driver4.find_elements(By.XPATH,"/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[1]/div/div/div[1]/div/div[2]/div[2]/div/div/div/div/a[2]/div/i/span")
#print(ratings[0].text)
#print(ratings[0].text)
for i in ratings[0:10]:
        rate=i.text
        prod_rating.append(rate)
        
print(prod_rating)



    


# In[468]:


prices=[]
amount=driver4.find_elements(By.CLASS_NAME,"a-price-whole")
for i in amount[0:10]:
    pr=i.text
    prices.append(pr)
        
print(prices)
print(len(prices))  
#time.sleep(10)





# In[469]:


df=pd.DataFrame({'Brand Name':product_brand,'Price':prices,'Ratings':prod_rating})
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

# In[308]:


driver7=webdriver.Chrome()
driver7.get('https://www.jagranjosh.com/general-knowledge/list-ofall-prime-ministers-of-india-1473165149-1')


# In[309]:


name=[]

name_tag=driver7.find_elements(By.XPATH,"//div[@class='TableData']/table/tbody/tr/td[2]")
print(name_tag[0].text)
for i in name_tag[1:19]:
        auth=i.text
        name.append(auth)
    
print(name)       
print(len(name))


# In[315]:


term_of_office=[]

term_tag=driver7.find_elements(By.XPATH,"//div[@class='TableData']/table/tbody/tr/td[6]")
#print(term_tag[0].text)
for i in term_tag[0:19]:
        auth=i.text
        term_of_office.append(auth)
    
print(term_of_office)       
print(len(term_of_office))


# In[312]:


remarks=[]

remarks_tag=driver7.find_elements(By.XPATH,"//div[@class='TableData']/table/tbody/tr/td[3]")
#print(term_tag[0].text)
for i in remarks_tag[1:19]:
        auth=i.text
        remarks.append(auth)
    
print(remarks)       
print(len(remarks))


# In[316]:


df=pd.DataFrame({'Name':name,'Term Of Office':term_of_office,'Remarks_Age When Assumed OFFICE':remarks})
print(df)


# # Ques 8

# In[292]:


driver8=webdriver.Chrome()
#driver8.get('https://www.motor1.com/features/308149/most-expensive-new-cars-ever/')
driver8.get('https://www.motor1.com')


# In[295]:


search=driver8.find_element(By.XPATH,"//input[@class='m1-search-panel-input m1-search-form-text']")
#search=driver8.find_element(By.ID, "search_input")
search.send_keys('50 most expensive cars')


# In[301]:


#/html/body/div[9]/div[2]/div/div/div[3]/div/div/div/form/button[1]/svg
#//button[@class='m1-search-panel-button m1-search-form-button-animate icon-search-svg']
#button=driver8.find_element(By.XPATH,'/html/body/div[9]/div[2]/div/div/div[3]/div/div/div/form/button[1]/svg')
button=driver8.find_element(By.XPATH,"//button[@class='m1-search-panel-button m1-search-form-button-animate icon-search-svg']")

#button=driver8.find_element(By.CLASS_NAME,'m1-search-panel-button m1-search-form-button-animate icon-search-svg')
button.click()


# In[303]:


button2=driver8.find_element(By.XPATH,"/html/body/div[9]/div[9]/div/div[1]/div/div/div[1]/div/div[1]/h3/a")
button2.click()


# In[304]:


car_name=[]
car_name_tag=driver8.find_elements(By.XPATH,"/html/body/div[9]/div[7]/div[2]/div[1]/div[2]/div[2]/h3")
#print(car_name_tag[0].text)
for i in car_name_tag[0:50]:
        auth=i.text
        car_name.append(auth)
    
        
print(len(car_name))
print(car_name)


# In[305]:


#/html/body/div[9]/div[7]/div[2]/div[1]/div[2]/div[2]/p[8]/strong
#/html/body/div[9]/div[7]/div[2]/div[1]/div[2]/div[2]/p[10]/strong
#/html/body/div[9]/div[7]/div[2]/div[1]/div[2]/div[2]/p[14]/strong
price=[]
price_tag=driver8.find_elements(By.CSS_SELECTOR,"div p strong")
#print(price_tag)
#print(price_tag[0].text)
for i in price_tag:
    auth=i.text.replace('Price','')
    price.append(auth)
    
        
print(len(price))
print(price)


# In[307]:


df=pd.DataFrame({'Car Name':car_name,'Price':price})
print(df)


# In[ ]:




