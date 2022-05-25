#!/usr/bin/env python
# coding: utf-8

# In[8]:


from bs4 import BeautifulSoup
import requests
import json


# In[5]:


# base_url = 'https://lihkg.com'
# uri = '/category/1'
# res = requests.get(base_url + uri)

url = 'https://lihkg.com/api_v2/thread/latest?cat_id=1&page=1&count=60&type=now'
res =requests.get(url)


# In[14]:


data = json.loads(res.text)
data


# In[18]:


for i in data['response']['items']:
    print(i['title'])
    for j in range(1, i['total_page'] + 1):
        print('https://lihkg.com/thread/' + i['thread_id'] + '/page/' + str(j))

