# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 11:42:01 2018

@author: Leila
"""

#%%

import requests

def add_contact(name,phone):
    
    url = "http://127.0.0.1:5000/add_contact/" + name + "/" + phone
    
    response = requests.get(url).json()
    
    return response

add_contact("pepe","911")

#%%

def get_contact(name):
    
    url = "http://127.0.0.1:5000/get_contact/" + name 
    
    response = requests.get(url).json()
    
    return response

get_contact("hannah")

#%%

def delete_contact(name):
    
    url = "http://127.0.0.1:5000/delete_contact/" + name 
    
    response = requests.get(url).json()
    
    return response

delete_contact("hannah")

#%%

def update_contact(name,phone):
    
    url = "http://127.0.0.1:5000/update_contact/" + name + "/" + phone
    
    response = requests.get(url).json()
    
    return response

update_contact("javi","514")

#%%
