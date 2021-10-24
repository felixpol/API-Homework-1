#!/usr/bin/env python
# coding: utf-8

# # WeatherPy
# ----
# 
# #### Note
# * Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.

# In[1]:


# Dependencies and Setup
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import requests
import time
from scipy.stats import linregress

# Import API key
from api_keys import 8ace8fcc35015bdcc7709ec2ef16f68f

# Incorporated citipy to determine city based on latitude and longitude
from citipy import citipy

# Output File (CSV)
output_data_file = "output_data/cities.csv"

# Range of latitudes and longitudes
lat_range = (-90, 90)
lng_range = (-180, 180)


# ## Generate Cities List

# In[2]:


# List for holding lat_lngs and cities
lat_lngs = []
cities = []

# Create a set of random lat and lng combinations
lats = np.random.uniform(lat_range[0], lat_range[1], size=1500)
lngs = np.random.uniform(lng_range[0], lng_range[1], size=1500)
lat_lngs = zip(lats, lngs)

# Identify nearest city for each lat, lng combination
for lat_lng in lat_lngs:
    city = citipy.nearest_city(lat_lng[0], lat_lng[1]).city_name
    
    # If the city is unique, then add it to a our cities list
    if city not in cities:
        cities.append(city)

# Print the city count to confirm sufficient count
len(cities)


# ### Perform API Calls
# * Perform a weather check on each city using a series of successive API calls.
# * Include a print log of each city as it'sbeing processed (with the city number and city name).
# 

# In[13]:





# ### Convert Raw Data to DataFrame
# * Export the city data into a .csv.
# * Display the DataFrame

# In[4]:


# Convert array of JSONs into Pandas DataFrame
output_data_file = pd.DataFrame(city_data)

# Export the City_Data into a csv
output_data_file.to_csv("WeatherPy.csv",encoding="utf-8",index=False)


# Show Record Count
output_data_file.count()


# In[16]:


# weather_data_df would go here I just had trouble making it 


# ## Inspect the data and remove the cities where the humidity > 100%.
# ----
# Skip this step if there are no cities that have humidity > 100%. 

# In[6]:





# In[17]:


#  Get the indices of cities that have humidity over 100%.


# In[19]:


# Make a new DataFrame equal to the city data to drop all humidity outliers by index.
# Passing "inplace=False" will make a copy of the city_data DataFrame, which we call "clean_city_data".


# In[ ]:





# ## Plotting the Data
# * Use proper labeling of the plots using plot titles (including date of analysis) and axes labels.
# * Save the plotted figures as .pngs.

# ## Latitude vs. Temperature Plot

# In[10]:


plt.scatter_LT(weather_data["Lat"], weather_data["Max Temp"], color = "Blue")
plt.ylabel("Max Temperature (F)")
plt.xlabel("Latitude")
plt.title(City Latitude vs Max Temperature (04/01/20)


# ## Latitude vs. Humidity Plot

# In[11]:


plt.scatter_LH(weather_data["Lat"], weather_data["Humidity"], color = "Blue")
plt.ylabel("Humidity (%)")
plt.xlabel("Latitude")
plt.title(City Latitude vs. Humidity (04/01/20))


# ## Latitude vs. Cloudiness Plot

# In[12]:


plt.scatter_LC(weather_data["Lat"], weather_data["Cloudiness"], color = "Blue")
plt.ylabel("Cloudiness")
plt.xlabel("Latitude")
plt.title(City Latitude vs. Cloudiness (04/01/20))


# ## Latitude vs. Wind Speed Plot

# In[13]:


plt.scatter_LW(weather_data["Lat"], weather_data["Wind Speed"], color = "Blue")
plt.ylabel("Wind Speed")
plt.xlabel("Latitude")
plt.title(City Latitude vs. Windspeed (04/01/20))


# ## Linear Regression

# In[24]:


#Figure out how to pull certain regions to compare


# ####  Northern Hemisphere - Max Temp vs. Latitude Linear Regression

# In[25]:


y_values = weather_data["Max Temp"]
x_values = weather_data["Latitude"]
(slope, intercept, rvalue, pvalue, stderr) = linregress(x_values, y_values)
regress_values = x_values * slope + intercept
line_eq = "y = " + str(round(slope,2)) + "x + " + str(round(intercept,2))
plt.scatter(x_values,y_values)
plt.plot(x_values,regress_values,"r-")
plt.annotate(line_eq,(6,10),fontsize=15,color="red")
plt.xlabel("Latitude")
plt.ylabel("Max Temp")


# ####  Southern Hemisphere - Max Temp vs. Latitude Linear Regression

# In[26]:


y_values = weather_data["Max Temp"]
x_values = weather_data["Latitude"]
(slope, intercept, rvalue, pvalue, stderr) = linregress(x_values, y_values)
regress_values = x_values * slope + intercept
line_eq = "y = " + str(round(slope,2)) + "x + " + str(round(intercept,2))
plt.scatter(x_values,y_values)
plt.plot(x_values,regress_values,"r-")
plt.annotate(line_eq,(6,10),fontsize=15,color="red")
plt.xlabel("Latitude")
plt.ylabel("Max Temp")


# ####  Northern Hemisphere - Humidity (%) vs. Latitude Linear Regression

# In[27]:


y_values = weather_data["Max Temp"]
x_values = weather_data["Latitude"]
(slope, intercept, rvalue, pvalue, stderr) = linregress(x_values, y_values)
regress_values = x_values * slope + intercept
line_eq = "y = " + str(round(slope,2)) + "x + " + str(round(intercept,2))
plt.scatter(x_values,y_values)
plt.plot(x_values,regress_values,"r-")
plt.annotate(line_eq,(6,10),fontsize=15,color="red")
plt.xlabel("Latitude")
plt.ylabel("Max Temp")


# ####  Southern Hemisphere - Humidity (%) vs. Latitude Linear Regression

# In[28]:


y_values = weather_data["Max Temp"]
x_values = weather_data["Latitude"]
(slope, intercept, rvalue, pvalue, stderr) = linregress(x_values, y_values)
regress_values = x_values * slope + intercept
line_eq = "y = " + str(round(slope,2)) + "x + " + str(round(intercept,2))
plt.scatter(x_values,y_values)
plt.plot(x_values,regress_values,"r-")
plt.annotate(line_eq,(6,10),fontsize=15,color="red")
plt.xlabel("Latitude")
plt.ylabel("Max Temp")


# ####  Northern Hemisphere - Cloudiness (%) vs. Latitude Linear Regression

# In[29]:


y_values = weather_data["Max Temp"]
x_values = weather_data["Latitude"]
(slope, intercept, rvalue, pvalue, stderr) = linregress(x_values, y_values)
regress_values = x_values * slope + intercept
line_eq = "y = " + str(round(slope,2)) + "x + " + str(round(intercept,2))
plt.scatter(x_values,y_values)
plt.plot(x_values,regress_values,"r-")
plt.annotate(line_eq,(6,10),fontsize=15,color="red")
plt.xlabel("Latitude")
plt.ylabel("Max Temp")


# ####  Southern Hemisphere - Cloudiness (%) vs. Latitude Linear Regression

# In[30]:


y_values = weather_data["Max Temp"]
x_values = weather_data["Latitude"]
(slope, intercept, rvalue, pvalue, stderr) = linregress(x_values, y_values)
regress_values = x_values * slope + intercept
line_eq = "y = " + str(round(slope,2)) + "x + " + str(round(intercept,2))
plt.scatter(x_values,y_values)
plt.plot(x_values,regress_values,"r-")
plt.annotate(line_eq,(6,10),fontsize=15,color="red")
plt.xlabel("Latitude")
plt.ylabel("Max Temp")


# ####  Northern Hemisphere - Wind Speed (mph) vs. Latitude Linear Regression

# In[31]:


y_values = weather_data["Max Temp"]
x_values = weather_data["Latitude"]
(slope, intercept, rvalue, pvalue, stderr) = linregress(x_values, y_values)
regress_values = x_values * slope + intercept
line_eq = "y = " + str(round(slope,2)) + "x + " + str(round(intercept,2))
plt.scatter(x_values,y_values)
plt.plot(x_values,regress_values,"r-")
plt.annotate(line_eq,(6,10),fontsize=15,color="red")
plt.xlabel("Latitude")
plt.ylabel("Max Temp")


# ####  Southern Hemisphere - Wind Speed (mph) vs. Latitude Linear Regression

# In[32]:


y_values = weather_data["Max Temp"]
x_values = weather_data["Latitude"]
(slope, intercept, rvalue, pvalue, stderr) = linregress(x_values, y_values)
regress_values = x_values * slope + intercept
line_eq = "y = " + str(round(slope,2)) + "x + " + str(round(intercept,2))
plt.scatter(x_values,y_values)
plt.plot(x_values,regress_values,"r-")
plt.annotate(line_eq,(6,10),fontsize=15,color="red")
plt.xlabel("Latitude")
plt.ylabel("Max Temp")


# In[ ]:




