#!/usr/bin/env python
# coding: utf-8

# In[3]:


#write a python program to display all the header tags from 'en.wikipedia.org/wiki/main_page'.
get_ipython().system('pip install bs4')
get_ipython().system('pip install html5lib')
get_ipython().system('pip install requests')


# In[4]:


from bs4 import BeautifulSoup
import requests


# In[17]:


url=requests.get('https://en.wikipedia.org/wiki/Main_Page')
soup=BeautifulSoup(url.text, 'html.parser')
story=soup.find_all(['h1','h2','h3'])
for i in story:
   print(i)


# In[ ]:




