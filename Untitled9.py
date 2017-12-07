
# coding: utf-8

# In[ ]:


import pandas as pd
data = pd.read_csv('blackfriday6 2.csv')
data
text = []
for i in range(1762):
    text.append(data.content[i])
k=[]
black = data

for i in range(len(text)):
    try:
        if 'http' in text[i]:
            k.append(1)
        else:
            k.append(0)
    except TypeError:
        k.append("Unreadable")
black['Link_in_tweet'] = k
k1=[]

for i in range(len(text)):
    try:
        if '#' in text[i]:
            k1.append(1)
        else:
            k1.append(0)
    except TypeError:
        k1.append("Unreadable")
black['hash_in_tweet']=k1

k2=[]
black = data

for i in range(len(text)):
    try:
        if '%' in text[i]:
            k2.append(1)
        else:
            k2.append(0)
    except TypeError:
        k2.append("Unreadable")

black['perc_in_tweet']=k2

k3=[]

for i in range(len(text)):
    try:
        k3.append(len(list(text[i])))
       
    except TypeError:
        k3.append("Unreadable")
        
print(k3)

black['num_char']=k3

k4=[]
black = data

for i in range(len(text)):
    try:
        if '@' in text[i]:
            k4.append(1)
        else:
            k4.append(0)
    except TypeError:
        k4.append("Unreadable")

black['engage']=k4



k5=[]
black = data

for i in range(len(text)):
    try:
        if '?' in text[i]:
            k5.append(1)
        else:
            k5.append(0)
    except TypeError:
        k5.append("Unreadable")

black['question']=k5

k6=[]
black = data

for i in range(len(text)):
    try:
        if '$' in text[i]:
            k6.append(1)
        else:
            k6.append(0)
    except TypeError:
        k6.append("Unreadable")

black['inc_price']=k6

black.to_csv('blackfriday10.csv')


