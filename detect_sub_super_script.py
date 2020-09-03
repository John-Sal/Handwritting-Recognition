#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 25 14:26:37 2020

@author: john
"""

import numpy as np
import cv2

def detect_sub_super_script(rects):
    
    inf = []
    char = []
    for rect in rects:
        point_1 = (rect[0], rect[1])
        point_2 = (rect[0] + rect[2], rect[1] + rect[3])
        midpoint = (int(rect[0] + rect[2]/2), int(rect[1] + rect[3]/2))
        inf.append(point_1)
        inf.append(point_2)
        inf.append(midpoint)
        char.append(inf)
        inf = []
    
    char = sorted(char,key=getKey(char))
    print(char)
    char_ind_1 = 0
    output_char = []
    for e in range(len(char)):
        output_char.append(0)
    
    while char_ind_1 < len(char):
        
        if char_ind_1 < len(char) -2:
            char_1 = char[char_ind_1]
            char_2 = char[char_ind_1 + 1]
            char_3 = char[char_ind_1 + 2]
            
            char_1_midpoint_y = char_1[2][1]
            char_1_top_y = char_1[0][1]
            char_1_bottom_y = char_1[1][1]
            
            char_2_bottom_y = char_2[1][1]
            char_2_top_y = char_2[0][1]
            
            char_3_bottom_y = char_3[1][1]
            char_3_top_y = char_3[0][1]
            
            if char_2_bottom_y < char_1_midpoint_y and char_2_top_y < char_1_top_y:
                output_char[char_ind_1] = "N"
                char_ind_1 += 1
                output_char[char_ind_1] = "SP"
                char_ind_1 += 1
                
                if char_3_bottom_y < char_1_midpoint_y and char_3_top_y < char_1_top_y:
                    output_char[char_ind_1] = "SP"
                    char_ind_1 += 1
                
            
                elif char_3_top_y > char_1_midpoint_y and char_3_bottom_y > char_1_bottom_y:
                    output_char[char_ind_1] = "SB"
                    char_ind_1 += 1
                
            elif char_2_top_y > char_1_midpoint_y and char_2_bottom_y > char_1_bottom_y:
                output_char[char_ind_1] = "N"
                char_ind_1 += 1
                output_char[char_ind_1] = "SB"
                char_ind_1 += 1
                
                if char_3_bottom_y < char_1_midpoint_y and char_3_top_y < char_1_top_y:
                    output_char[char_ind_1] = "SP"
                    char_ind_1 += 1
                
            
                elif char_3_top_y > char_1_midpoint_y and char_3_bottom_y > char_1_bottom_y:
                    output_char[char_ind_1] = "SB"
                    char_ind_1 += 1
            
            else:
                output_char[char_ind_1] = "N"
                char_ind_1 += 1
                
                
        if char_ind_1 == len(char) - 2:
            
            char_1 = char[char_ind_1]
            char_2 = char[char_ind_1 + 1]
            
            char_1_midpoint_y = char_1[2][1]
            char_1_top_y = char_1[0][1]
            char_1_bottom_y = char_1[1][1]
            
            char_2_bottom_y = char_2[1][1]
            char_2_top_y = char_2[0][1]
            
            if char_2_bottom_y < char_1_midpoint_y and char_2_top_y < char_1_top_y:
                output_char[char_ind_1] = "N"
                char_ind_1 += 1
                output_char[char_ind_1] = "SP"
                char_ind_1 += 1
            
            elif char_2_top_y > char_1_midpoint_y and char_2_bottom_y > char_1_bottom_y:
                output_char[char_ind_1] = "N"
                char_ind_1 += 1
                output_char[char_ind_1] = "SB"
                char_ind_1 += 1
                
        if char_ind_1 == len(char) - 1:
            output_char.append("N")
            break
        
                
                
    
    return output_char


def getKey (listA):
    outputlist=[]
    #print(type(listA))
    for i in range (len(listA)-1):
        #print (listA[i])
        #print('This is the length of the list',len(listA[i]))
        #print('This is the of the contents of the list',listA[i][0][0])
        outputlist.append(listA[i][0][0])
    

k_letters = [(590, 75, 169, 116), (943, 57, 154, 141), (146, 50, 167, 132), (1137, 12, 156, 47), (324, 5, 197, 79)]
detect_sub_super_script(k_letters)