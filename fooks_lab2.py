#!/usr/bin/env python
# coding: utf-8

# In[2]:


import glob
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point, LineString, Polygon
from rasterstats import zonal_stats


# In[3]:


glob.glob('/Users/phoebe.fooks/Documents/programming/week2/data/*/*')


# In[4]:


d1coords = open('/Users/phoebe.fooks/Documents/programming/week2/data/districts/district01.txt', 'r')
x,y = zip(*[l.split() for l in d1coords])
d1coords.close()

d1xcoords = list(x)
d1ycoords = list(y)

d1xcoords.pop(0)
d1ycoords.pop(0)

d1x = list(map(float, d1xcoords))
d1y = list(map(float, d1ycoords))

d1xy = list(zip(d1x, d1y))
district01 = Polygon(d1xy)
district01


# In[5]:


d5coords = open('/Users/phoebe.fooks/Documents/programming/week2/data/districts/district05.txt', 'r')
x,y = zip(*[l.split() for l in d5coords])
d5coords.close()

d5xcoords = list(x)
d5ycoords = list(y)

d5xcoords.pop(0)
d5ycoords.pop(0)

d5x = list(map(float, d5xcoords))
d5y = list(map(float, d5ycoords))

d5xy = list(zip(d5x, d5y))
district05 = Polygon(d5xy)
district05


# In[6]:


d6coords = open('/Users/phoebe.fooks/Documents/programming/week2/data/districts/district06.txt', 'r')
x,y = zip(*[l.split() for l in d6coords])
d6coords.close()

d6xcoords = list(x)
d6ycoords = list(y)

d6xcoords.pop(0)
d6ycoords.pop(0)

d6x = list(map(float, d6xcoords))
d6y = list(map(float, d6ycoords))

d6xy = list(zip(d6x, d6y))
district06 = Polygon(d6xy)
district06


# In[7]:


len(d1xy)


# In[8]:


len(d5xy)


# In[9]:


len(d6xy)


# In[10]:


gdf_data = {'district': ['01', '05', '06'],
           'num_coords': [1847, 566, 1223],
           'geography':[district01, district05, district06]}


# In[11]:


gdf = pd.DataFrame(gdf_data)


# In[12]:


gdf


# In[13]:


glob.glob('/Users/phoebe.fooks/Documents/programming/week2/data/*/*')


# In[15]:


lu2004 = open('/Users/phoebe.fooks/Documents/programming/week2/data\\agriculture\\GLOBCOVER_2004_lab2.tif', 'r')


# In[14]:


d012004 = zonal_stats(district01, '/Users/phoebe.fooks/Documents/programming/week2/data\\agriculture\\GLOBCOVER_2004_lab2.tif')
d012009 = zonal_stats(district01, '/Users/phoebe.fooks/Documents/programming/week2/data\\agriculture\\GLOBCOVER_2009_lab2.tif')
d052004 = zonal_stats(district05, '/Users/phoebe.fooks/Documents/programming/week2/data\\agriculture\\GLOBCOVER_2004_lab2.tif')
d052009 = zonal_stats(district05, '/Users/phoebe.fooks/Documents/programming/week2/data\\agriculture\\GLOBCOVER_2009_lab2.tif')
d062004 = zonal_stats(district06, '/Users/phoebe.fooks/Documents/programming/week2/data\\agriculture\\GLOBCOVER_2004_lab2.tif')
d062009 = zonal_stats(district06, '/Users/phoebe.fooks/Documents/programming/week2/data\\agriculture\\GLOBCOVER_2009_lab2.tif')


# In[15]:


print(d012004)
print(d012009)
print(d052004)
print(d052009)
print(d062004)
print(d062009)


# In[36]:


d14 = d012004[0]
d19 = d012009[0]
d54 = d052004[0]
d59 = d052009[0]
d64 = d062004[0]
d69 = d062009[0]


# In[41]:


d14m = d14["mean"]*100
d19m = d19["mean"]*100
d54m = d54["mean"]*100
d59m = d54["mean"]*100
d64m = d69["mean"]*100
d69m = d64["mean"]*100


# In[45]:


percentlist = [d14m, d19m, d54m, d59m, d64m, d69m]


# In[46]:


print(percentlist)


# In[ ]:




