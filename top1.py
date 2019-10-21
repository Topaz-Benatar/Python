# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 13:19:53 2019

@author: ADMIN
"""
#Topaz Ben Atar

def InputDict():
    dic= {}
    for num in range(3):
        key= input("Enter a string ")
        value= int(input("Enter an integer number "))
        dic[key]=value
    return (dic)


def KeyInDict(dic1):
    key= input ("Enter a string ")
    if key in dic1:
        print ("YES!")
    else:
        print ("NO!")
       

dic1= InputDict()
KeyInDict(dic1)