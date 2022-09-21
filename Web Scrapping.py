#!/usr/bin/env python
# coding: utf-8

# In[3]:


#import modules
import lxml
from bs4 import BeautifulSoup as bs
import pandas as pd
pd.set_option('display.max_colwidth', 500)
import time
import requests
import random
import urllib3
urllib3.disable_warnings()
import html5lib


# In[4]:


page = requests.get("https://www.tengizchevroil.com/")
page


# In[5]:


page_azh=requests.get("https://azh.kz/ru", verify=False).text
page_azh


# In[6]:


soup = bs(page_azh, "html.parser")
print(soup) 


# In[ ]:


#выбрать данные только по просмотрам тем, касающихся ТШО 


# In[17]:


soup.find_all(class_='title')


# In[11]:


quotes = [i.text for i in soup.find_all(class_='title')]
quotes


# In[ ]:


#сбор просмотров данных каждые 15 минут???


# In[13]:


df = pd.DataFrame()
df['title'] = quotes


# In[ ]:


#визуализировать рост


# In[ ]:





# In[13]:


page_tengri=requests.get("https://tengrinews.kz/", verify=False).text
page_azh


# In[14]:


soup = bs(page_tengri, "html.parser")
print(soup) 


# In[8]:


page_zakon=requests.get("https://www.zakon.kz/", verify=False).text
page_zakon


# In[9]:


soup = bs(page_zakon, "html.parser")
print(soup) 

