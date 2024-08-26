#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install selenium')


# In[3]:


from selenium import webdriver
from selenium.webdriver.common.by import By
import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import time


# In[31]:


driver=webdriver.Chrome()
driver.get('https://www.Shine.com')


# In[33]:


designation=driver.find_element(By.ID, "id_q")
designation.send_keys('Data Analyst')
location=driver.find_element(By.ID, "id_loc")
location.send_keys('Bangalore')
search=driver.find_element(By.CLASS_NAME," btn btn-secondary undefined")
search.click()
job_title=[]
job_tag=driver.find_elements(By.XPATH,"//strong[@jobCard_pReplaceH2__xWmHg]/a/]")
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


# In[36]:


driver2=webdriver.Chrome()
driver2.get('https://www.flipkart.com')

product=driver.find_element(By.CLASS_NAME,"Pke_EE")
product.send_keys('Sunglasses')

search=driver.find_element(By.CLASS_NAME,"MJG8Up")
search.click()

product_brand=[]
start=0
end=3
for page in range(start,end):
    brand=driver.find_elements(By.CLASS_NAME,"syl9yP")
    for i in brand[0:100] :
         brand=i.text
         product_brand.append(brand)
    
next_button=driver.find_element(By.XPATH,"/html/body/div/div/div[3]/div[1]/div[2]/div[12]/div/div/nav/a[12]/span")
next_button.click()
    
    
#print(product_brand)
print(len(product_brand))
time.sleep(10)

prod_details=[]
start=0
end=3
for page in range(start,end):
    details=driver.find_elements(By.CLASS_NAME,"WKTcLC")
    for i in details[0:100]:
        det=i.text
        prod_details.append(det)

next_button=driver.find_element(By.XPATH,"/html/body/div/div/div[3]/div[1]/div[2]/div[12]/div/div/nav/a[12]/span")
next_button.click()
    
#print(job_location)
print(len(prod_details))

time.sleep(10)

prices=[]
start=0
end=3
for page in range(start,end):
    amount=driver.find_elements(By.CLASS_NAME,"hl05eU")
    for i in amount[0:100]:
         pr=i.text
         prices.append(pr)
        
next_button=driver.find_element(By.XPATH,"/html/body/div/div/div[3]/div[1]/div[2]/div[12]/div/div/nav/a[12]/span")
next_button.click()
print(len(prices))  
time.sleep(10)



df=pd.DataFrame({'Brand Name':prod_brand,'Description':prod_details,'Price':prices})
df


# In[ ]:




