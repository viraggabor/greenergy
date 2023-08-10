# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 12:30:24 2023

@author: fonok
"""

import requests


#function for the test and editing the string
def foo(v):
    new_line=''
    for i in v:
        if i.isupper():
            new_line=new_line+i.lower()
        elif i.islower():
            new_line=new_line+i.upper()
        else:
            new_line=new_line+i
            
    return new_line

if __name__ == "__main__":
    
    url='' #enter your url where program should expect the request
    url=input('Enter the URL where program should expect the request: ')
    
    try:
       req=requests.get(url)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)    
    
    req_json=req.json()
    req_json['string']=foo(req_json['string'])
    post_req=requests.post(url,data=req_json)


