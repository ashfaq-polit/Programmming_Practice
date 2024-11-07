#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(Ashfaq)s
"""
####Understanding from https://www.youtube.com/watch?v=tWnHbSHwNmA 
     
def backtrack(i, curstr, digits, digitToChar, res):
 
    if len(curstr) == len(digits):
        res.append(curstr)
        return
    curDigit = digits[i]
    letters = digitToChar[curDigit]
    for letter in letters:
        curstr += letter
        backtrack(i + 1, curstr, digits, digitToChar, res)
        curstr = curstr[:-1]
    # return res


def letter_Combination(digits):
    digitToChar = {"2" : "abc",
                   "3" : "def",
                   "4" : "ghi",
                   "5" : "jkl",
                   "6" : "mno",
                   "7" : "pqrs",
                   "8" : "tuv",
                   "9" : "wxyz"}

    res =  []
    if digits == "": 
        return res
    
    # def backtrack(i, curstr):
    #     if len(curstr) == lenD:
    #         res.append(curstr)
    #     else:
    #         curDigit = digits[i]
    #         letters = digitToChar[curDigit]
    #         for letter in letters:
    #             backtrack(i + 1, curstr + letter)
            
    # if digits:
    #     backtrack(0, "")
    
    # return res
    i = 0
    curstr = ""
    # if digits:
    backtrack(i, curstr, digits, digitToChar, res)    
    return res

    
digits = "23"    
letter_Combination(digits)




