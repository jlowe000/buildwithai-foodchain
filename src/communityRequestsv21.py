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


df_fe = pd.read_csv (r'foodexp.csv')   #read the csv file (put 'r' before the path string to address any special characters in the path, such as '\'). Don't forget to put the file name at the end of the path + ".csv"

# print (df_fe)
# print (len(df_fe))
# print("================")
# print (df_fe.iloc[1])
# print (df_fe.iloc[1,3])
# print("================")
# print (df_fe.iloc[20])
# print (df_fe.iloc[10,3])
# print("================")
# print (df_fe.loc[20]["ITEM"])

# print (df.loc[15-20,:])

# 
# communityRequests python program 
# collaborators: Jason Lowe and Franco Ucci 
#
# this is about representing Community of Conumers, who will be placing 
# Orders of Food, from 20 Consumers, 
# placing 4-10 Orders every month, over 3 months
# each order being 20 random items making up a hamper
#
# 20 consumers
# -- use faker names
# -- use geo ip address
# 
# start date for 3 months 
#  for 4-10 orders in a month 
# 
# each order to have 20 random items
# # 

StartDate = "1/10/2021"
orderStartDate = datetime.strptime(StartDate, "%m/%d/%Y")
              
# open orderItems file for writing

orderHdr = {'OrderId': ['50','51'],
        'CustomerId': ['90','91'],
        'OrderTotal': ['200','200'],
        'OrderDate': ['01/10/2021','01/10/2021'],
        'Location': ['AGA West','AGA South'],
        'CustomerName': ['Mary Smith','Sunil Brown'],
        'CustomerGeoLat': [-34.923321,-34.9333],
        'CustomerGeoLon': [138.602142 ,138.602142]
        }
        
orderItems = {'OrderId': ['50','51'],
        'OrderItemId': ['90','91'],
        'ProductType': ['DAIRY','DAIRY'],
        'ProductItem': ['Milk Box','Milk Choc'],
        'ProductPeriod': ['2 weeks','3 months'],
        'ProductDetails': ['opened','unopened'],
        'ProductStorage': ['Refrigeration','Freezer']        
        }
        
LocationSet = ['AGA HQ','AGA South','AGA East','AGA West', 'AGA North']
        
g_lat=-27.467990
g_lon=153.028090
# Lat, Lon for 261 Quuen St, Brisbane

Community = 20
Period = 90 #days 
Start_OrderID=50050
Start_CustomerID=90050
Low_Item_No=12
High_Item_No=20
Food_Catalog=len(df_fe)


for i in range(0,Community):
    
    person_name = fake.first_name() + ' '+ fake.last_name()
    newLatBit=float(random.randrange(-750,750,1)/10000.0000)
    newLonBit=float(random.randrange(-750,750,1)/10000.0000)
    newLat = g_lat +newLatBit
    newLon = g_lon +newLonBit

    orderFreq=random.randrange(12,30,1)
    duration=math.floor(Period/orderFreq)
    
    orderLocation=LocationSet[random.randint(0,4)]
    
    for j in range(0,orderFreq,1) :
   
      orderHdr['CustomerId'].append(Start_CustomerID+i)                 # autogen 
      orderHdr['OrderId'].append(Start_OrderID+j)                   # autogen 
      orderHdr['CustomerName'].append(person_name) 
      orderHdr['OrderTotal'].append(str(200))                   # autogen 
      orderHdr['Location'].append(orderLocation)                   # autogen 
      orderHdr['CustomerGeoLat'].append(newLat)
      orderHdr['CustomerGeoLon'].append(newLon)
      
      noDays= j*duration+random.randrange(0,duration-1,1)
      orderHdr['OrderDate'].append(orderStartDate + timedelta(days=noDays))

      orderItemNos=random.randrange(Low_Item_No,High_Item_No,1)
      for k in range(1,orderItemNos,1):
        
        Food_Index=random.randrange(1,Food_Catalog,1)
        orderItems['OrderId'].append(Start_OrderID+j)
        orderItems['OrderItemId'].append(str(k))                
        orderItems['ProductType'].append(df_fe.loc[Food_Index]["TYPE"])                
        orderItems['ProductItem'].append(df_fe.loc[Food_Index]["ITEM"])                
        orderItems['ProductPeriod'].append(df_fe.loc[Food_Index]["PERIOD"])                
        orderItems['ProductDetails'].append(df_fe.loc[Food_Index]["DETAILS"])                
        orderItems['ProductStorage'].append(df_fe.loc[Food_Index]["STORAGE"])      
 
df_orderItems = pd.DataFrame(orderItems)
df_orderItems.to_csv (r'orderItemsRequests.csv', index = False, header=True)
print (df_orderItems)
 
df_orderHdr = pd.DataFrame(orderHdr)
df_orderHdr.to_csv (r'orderHeaderRequests.csv', index = False, header=True)
print (df_orderHdr)
