# May 2011 Dietz
# CIT 592
# key - first method lifted from prior projects

import random
import math
import copy
import HanoiKey32 


def int2baseTwo(x):
    """Converts x to base two as a list of integers in reverse order"""
    binNum = []
    while x // 2 != 0:
        bit = x & 1
        x = x // 2
        binNum.append(bit)
    binNum.append(x)
    return binNum
    #return HanoiKey.int2baseTwo(x)

def randLocationR(n):
    return HanoiKey.randLocationR(n)

def rollcall2List(R):
    return HanoiKey.rollcall2List(R)


def isLegalMove(L, a, b):
    return HanoiKey.isLegalMove(L, a, b)
    
def makeMove(L, a, b):
    return HanoiKey.makeMove(L, a, b)
    
def printList(L):
    return HanoiKey.printList(L)
                
def list2Rollcall(L):
    return HanoiKey.list2Rollcall(L)
    
def rollcall2SA(R):
    return HanoiKey.rollcall2SA(R)
    
def SA2rollcall(SA):
    return HanoiKey.SA2rollcall(SA)

def SA2TA(SA):
    return HanoiKey.SA2TA(SA)

def TA2SA(TA):
    return HanoiKey.TA2SA(TA)

def reduceTA(A, B):
    return HanoiKey.reduceTA(A, B)

def distTA(A_in, B_in):          
    return HanoiKey.distTA(A_in, B_in)
   
def play():
    HanoiKey.play()
    
