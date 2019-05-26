#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')
import pandas
import seaborn


# # Load CVS file into memory

# In[2]:


data = pandas.read_csv('Desktop/uber-raw-data-apr14.csv')


# In[3]:


data.tail()


# #convert datetime and add some useful columns

# In[4]:


data['Date/Time'] = data['Date/Time'].map(pandas.to_datetime)


# In[5]:


data.tail()


# In[6]:


def get_dom(dt):
    return dt.day
data['dom'] = data['Date/Time'].map(get_dom)


# In[7]:


data.tail()


# In[8]:


def get_weekday(dt):
    return dt.weekday()
data['weekday'] = data['Date/Time'].map(get_weekday)

def get_hour(dt):
    return dt.hour
data['hour'] = data['Date/Time'].map(get_hour)
data.tail()


# Analysis

# Analys the DoM

# In[9]:


hist(data.dom, bins=30, rwidth=.8)
xlabel('Date of month')
ylabel('Frequency')
title('Frequency by DoM -Uber -April')


# In[10]:


for k,rows in data.groupby('dom'):
    print((k, len(rows)))


# In[11]:


for k,rows in data.groupby('dom'):
    print((k, rows))
    break


# In[12]:


def count_rows(rows):
    return len(rows)
by_date = data.groupby('dom').apply(count_rows)
by_date


# In[13]:


plot(by_date)


# In[14]:


by_date_sorted = by_date.sort_values()
by_date_sorted


# In[15]:


bar(range(1, 31), by_date_sorted)


# Analyze the hour

# In[16]:


hist(data.hour, bins=24, range=(.5, 24))


# Analys the weekday

# In[17]:


hist(data.weekday, bins=7, range = (-.5,6), rwidth=.8, color='green')
xticks(range(7), 'Mon Tue Wed Thu Fri Sat Sun'.split())


# Cross Analysis (Hour,Dow)

# In[18]:


data.groupby('hour weekday'.split()).apply(count_rows).unstack()


# Cross Analysis (hour, dow)

# In[19]:


by_cross = data.groupby('weekday hour'.split()).apply(count_rows).unstack()


# In[20]:


seaborn.heatmap(by_cross)


# By Lat and Lon

# In[21]:


hist(data['Lat'], bins=100, range = (40.5, 41))
("")


# In[22]:


hist(data['Lon'], bins=100, range = (-74.1, -73.9))
("")


# In[23]:


hist(data['Lon'], bins=100, range = (-74.1, -73.9), color='r', label = 'Longitude')
grid()
legend(loc='upper left')
twiny()
hist(data['Lat'], bins=100, range = (40.5, 41), color='g', label = 'Latitude')
legend(loc='best')
("")


# In[24]:


plot(data['Lat']) 


# In[25]:


plot(data['Lat'])
xlim(0,100)


# In[26]:


plot(data['Lat'], '*', ms=20, color= 'green')
xlim(0,100)


# In[27]:


plot(data['Lat'], '^', ms=20, color= 'green', label= 'Lat')
plot(data['Lon'], '^', ms=20, color= 'red', label= 'Lon')


# In[28]:


plot(data['Lon'], data['Lat'])


# In[29]:


plot(data['Lon'], data['Lat'], '.', ms=1, alpha=.5)


# In[30]:


figure(figsize=(20, 20))
plot(data['Lon'], data['Lat'], '.', ms=1, alpha=.5)
xlim(-74.2, -73.7)
ylim(40.7, 41)

