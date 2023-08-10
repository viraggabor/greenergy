# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 12:36:27 2023

@author: fonok
"""

from green import foo

def test_foo_1():
    assert foo('csülköspacal') == 'CSÜLKÖSPACAL'
    
def test_foo_2():
    assert foo('abcDEF') == 'ABCdef'
    
def test_foo_3():
    assert foo('kannÁsBOR') == 'KANNáSbor'
    
def test_foo_4():
    assert foo('@kukaC') == '@KUKAc'
    