# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 18:57:10 2018

@author: Leila
"""


#%%    

from product_quality import recalculate_quality, Product
    
def test_recalculate_cheese():
    manchego = Product("cheese",3)
    recalculate_quality(manchego)
    assert manchego.quality == 1
    
def test_recalculate_potato():
    fries = Product("potato",5)
    recalculate_quality(fries)
    assert fries.quality == 4.5

def test_recalculate_teammember():
    hannah = Product("teammember",1)
    recalculate_quality(hannah)
    assert hannah.quality == -2
    
def test_recalculate_fish():
    salmon = Product("fish",1.5)
    recalculate_quality(salmon)
    assert salmon.quality == -1.5



