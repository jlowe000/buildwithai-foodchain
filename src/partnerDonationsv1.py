import pandas as pd
import csv,io
import math

import requests
import json
import pprint
import random
import datetime
from datetime import timedelta
from datetime import datetime

from geopy.geocoders import Nominatim
#from collections import OrderedDict
#import geocoder
import collections

from faker import Factory
fake = Factory.create('en_AU')

print('Food Simple')
df_foodsimple = pd.read_csv (r'foodsimple.csv')
FoodSimple_Catalog=len(df_foodsimple)
print (df_foodsimple)
print (FoodSimple_Catalog)

print('Food Fridge')
df_foodfridge = pd.read_csv (r'foodfridge.csv')
FoodFridge_Catalog=len(df_foodfridge)
print (df_foodfridge)
print (FoodFridge_Catalog)

print('Food Shelf')
df_foodshelf = pd.read_csv (r'foodshelf.csv')
FoodShelf_Catalog=len(df_foodshelf)
print (df_foodshelf)
print (FoodShelf_Catalog)

# 3 SuperMkts acting as Donors
# for 90 Days
# look at using 3 separate Food Data Sets

# foodsimple - every day food - all 12 items
# foodfridge - choose daily from 452 items
# foodshelf - choose weekly from 229 items

# Supermarkets/Partners = ['FoodieLand','LoMarket','Grocertown'] 

# normal to low to high to low to normal 
# Jason Lowe Index Factor
# JLOF_INDEX = [5, 3, 1, 8, 9, 1, 2, 3, 5]

# Qty randomize between 20-30

# Daily Simple Order Donations

# Daily fridge Order Donations
# 20 Random DailyItems 
# Qty 20-30

# Weekly Shelf Order Donations
# WeeklyItems
# Divide by 7 to check
# 
# each order to have 20 random items
# # 

StartDate = "1/10/2021"
orderStartDate = datetime.strptime(StartDate, "%m/%d/%Y")
              
# open orderItems file for writing

orderHdr = {'OrderId': [],
        'PartnerId': [],
        'OrderTotal': [],
        'OrderDate': [],
        'PartnerName': [],
        'PartnerGeoLat': [],
        'PartnerGeoLon': []
        }
        
orderItems = {'OrderId': [],
        'OrderItemId': [],
        'ProductType': [],
        'ProductItem': [],
        'ProductPeriod': [],
        'ProductDetails': [],
        'ProductStorage': [],
        'Quantity': []
        }
        
Partners = ['FoodieLand','LoMarket','Grocertown']
        
g_lat=-27.467990
g_lon=153.028090
# Lat, Lon for 261 Quuen St, Brisbane

PartnerGroup = 3
Period = 90 #days 
Start_OrderID=20050
Start_CustomerID=190050
Low_Item_No=20
High_Item_No=30
# Jason Lowe Index Factor to create some peaks and lowes 
JLOF_INDEX = [5, 3, 1, 8, 9, 1, 2, 3, 5, 4, 3, 2, 6, 8, 9]

orderId = Start_OrderID

for i in range(0,PartnerGroup,1):
    
    partner_name = Partners[i]
    newLatBit=float(random.randrange(-750,750,1)/10000.0000)
    newLonBit=float(random.randrange(-750,750,1)/10000.0000)
    newLat = g_lat +newLatBit
    newLon = g_lon +newLonBit

    orderFreq=random.randrange(12,30,1)
    duration=math.floor(Period/orderFreq)
    
    # for each day
    for j in range(1,Period,1) :
   
      orderId = orderId + 1;
      orderHdr['PartnerId'].append(Start_CustomerID+i)                 # autogen 
      orderHdr['OrderId'].append(orderId)                   # autogen 
      orderHdr['PartnerName'].append(partner_name) 
      orderHdr['OrderTotal'].append(str(2000))                   # autogen # autogen 
      orderHdr['OrderDate'].append(orderStartDate + timedelta(days=j))    
      orderHdr['PartnerGeoLat'].append(newLat)
      orderHdr['PartnerGeoLon'].append(newLon)
      
      local_OrderItemId = 1
      
      #Simple Daily Food
      for k in range(0,FoodSimple_Catalog-1,1):
        
        Food_Index=k
        local_Quantity=random.randrange(Low_Item_No,High_Item_No,1)
        # print (math.floor(j/7))
        local_Quantity=local_Quantity * JLOF_INDEX[math.floor(j/7)]
        
        orderItems['OrderId'].append(orderId)
        orderItems['OrderItemId'].append(str(local_OrderItemId))                
        orderItems['ProductType'].append(df_foodsimple.loc[Food_Index]["TYPE"])                
        orderItems['ProductItem'].append(df_foodsimple.loc[Food_Index]["ITEM"])                
        orderItems['ProductPeriod'].append(df_foodsimple.loc[Food_Index]["PERIOD"])    
        orderItems['ProductDetails'].append(df_foodsimple.loc[Food_Index]["DETAILS"])    
        orderItems['ProductStorage'].append(df_foodsimple.loc[Food_Index]["STORAGE"])      
        orderItems['Quantity'].append(local_Quantity)      
        local_OrderItemId=local_OrderItemId+1
 
      #Simple Daily Fridge Food
      orderItemNos=random.randrange(Low_Item_No,High_Item_No,1)     
      for k in range(1,orderItemNos,1):
        
        Food_Index=random.randrange(1,FoodFridge_Catalog,1)
        local_Quantity=random.randrange(Low_Item_No,High_Item_No,1)
        local_Quantity=local_Quantity * JLOF_INDEX[math.floor(j/7)]
        
        orderItems['OrderId'].append(orderId)
        orderItems['OrderItemId'].append(str(local_OrderItemId))               
        orderItems['ProductType'].append(df_foodfridge.loc[Food_Index]["TYPE"])                
        orderItems['ProductItem'].append(df_foodfridge.loc[Food_Index]["ITEM"])                
        orderItems['ProductPeriod'].append(df_foodfridge.loc[Food_Index]["PERIOD"])      
        orderItems['ProductDetails'].append(df_foodfridge.loc[Food_Index]["DETAILS"])  
        orderItems['ProductStorage'].append(df_foodfridge.loc[Food_Index]["STORAGE"])
        orderItems['Quantity'].append(local_Quantity)    
        local_OrderItemId=local_OrderItemId+1
 
      #Weekly Shelf Food
      orderItemNos=random.randrange(Low_Item_No,High_Item_No,1)     
      if (Period % 7 == 0) :
        for k in range(1,orderItemNos,1):
        
            Food_Index=random.randrange(1,FoodShelf_Catalog,1)
            local_Quantity=random.randrange(Low_Item_No,High_Item_No,1)
            local_Quantity=local_Quantity * JLOF_INDEX[math.floor(j/7)]
            
            orderItems['OrderId'].append(orderId)
            orderItems['OrderItemId'].append(str(local_OrderItemId))             
            orderItems['ProductType'].append(df_foodshelf.loc[Food_Index]["TYPE"])             
            orderItems['ProductItem'].append(df_foodshelf.loc[Food_Index]["ITEM"])             
            orderItems['ProductPeriod'].append(df_foodshelf.loc[Food_Index]["PERIOD"])      
            orderItems['ProductDetails'].append(df_foodshelf.loc[Food_Index]["DETAILS"])  
            orderItems['ProductStorage'].append(df_foodshelf.loc[Food_Index]["STORAGE"])
            orderItems['Quantity'].append(local_Quantity)    
            local_OrderItemId=local_OrderItemId+1
  
df_orderItems = pd.DataFrame(orderItems)
df_orderItems.to_csv (r'orderItemsDonations.csv', index = False, header=True)
print (df_orderItems)
 
df_orderHdr = pd.DataFrame(orderHdr)
df_orderHdr.to_csv (r'orderHeaderDonations.csv', index = False, header=True)
print (df_orderHdr)
