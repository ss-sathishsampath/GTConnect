# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 15:03:04 2019
Project Name: GTConnect
CS 6675 Advanced Internet Computing, College of Computing, Georgia Institute of Technology
@Professor & Project Guide: Dr. Ling Liu(lingliu@cc.gatech.edu)
@authors: Sathish Sampath, Jenita Lydia Jebasingh(jenita.lydia17@gmail.com), Sai Tadikonda(saitadikonda001@gmail.com), Sreyas Sriram(sreyas28@gmail.com)
"""

from math import sin, cos, sqrt, atan2, radians
import datetime

from datetime import timedelta


ads = {}

def check_ads(lat1,lon1, ads, user,user_ads):
    # approximate radius of earth in km
    R = 6373.0
    
    result1 = []
    result2 = []
    result3 = []
    result = []
    ads_selected = []
    lat1 = radians(lat1) #location['lat'])
    lon1 = radians(lon1) #location['long'])
    today = datetime.datetime.now()
    

    
    for each in ads:
#        print(ads[each]['end_date'])
        ad_end = datetime.datetime(ads[each]['end_date'].year, ads[each]['end_date'].month, ads[each]['end_date'].day)
        end = ad_end + timedelta(1)
        if((today > ads[each]['start_date']) and (today < end) and each not in user_ads[user]):
            
            distance = 0
            lat2 = radians(ads[each]['lat'])
            lon2 = radians(ads[each]['long'])
                    
            dlon = lon2 - lon1
            dlat = lat2 - lat1
            
            a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
            c = 2 * atan2(sqrt(a), sqrt(1 - a))
            
            distance = R * c
#            print(distance)
            
            
            if ads[each]['type'] == 1:
                if distance < 0.051:
                    result1.append(ads[each]['text'])
                    ads_selected.append(each)
            elif ads[each]['type'] == 2:
                if distance < 0.1:
                    result2.append(ads[each]['text'])
                    ads_selected.append(each)      
            else:
                if distance < 0.151:
                    result3.append(ads[each]['text'])
                    ads_selected.append(each)
                
 
    result = result2 + result3 + result1
            
    return result, ads_selected
      
        