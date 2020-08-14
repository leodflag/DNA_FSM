# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 00:11:47 2019

@author: leodflag
"""
import numpy as np

# 字元轉座標
def conversion_coordinates(s):
    if s == "A":
        x = 0
    elif s == "T":
        x = 1
    elif s == "G":
        x = 2
    elif s == "C":
        x = 3
    else:
        x = -1
    return x

# 找開始矩陣
def find_start_array(r, c):
    startArray = np.array([
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ])
    return startArray[r][c]

# 找結束矩陣
def find_end_array(r, c):
    endArray = np.array([
        [1, 0, 1, 0],
        [1, 0, 1, 0],
        [1, 0, 0, 0],
        [0, 0, 0, 0]
    ])
    return endArray[r][c]

# 找基因組
def three_gene(gene_string,start,end):
    str_len=len(gene_string[start:end-2])
    if str_len%3==0:
        print(gene_string[start:end-2])
    elif str_len%3 ==1:
        print(gene_string[start:end-3])
    elif str_len%3 ==2:
        print(gene_string[start:end-4])
    else:
        print("")

inputStr = input("Enter a Chromosome string: ")  # 輸入染色體字串
index = 0  # 字元的指標
now_start = 0  # 開始狀態
now_end = 0  # 結束狀態
A_three_word = 0  # 開始的字元數
T_three_word = 0  # 結束的字元數
S_E = 0  # 有頭有尾的狀況
START = 0  # 開始的位置
END = 0  # 結束的位置
while index < len(inputStr):
    if START == 0:
        # (遇到字元A或開始狀態開啟)開始字數未滿3，找開始矩陣
        if (inputStr[index] == "A" or now_start == 1) and A_three_word < 3:
            c = conversion_coordinates(inputStr[index])  # 字母對照成數字，用來找直行
            if inputStr[index] == "A":  # 遇到字元是A時
                now_start = 1  # 開始狀態開啟
                A_three_word = 1  # 紀錄開始字元數
                r = 0  # 字元A要從第一橫列開始找
            else:
                now_start = find_start_array(r, c)  # 找開始矩陣，確認開始狀態是否開啟
                if now_start == 1:  # 開始狀態開啟
                    r = c  # 將直行的數字給橫列，對應字元移動的順序
                    A_three_word += 1  # 開始字元數 +1
        elif A_three_word == 3:  # 找到開始基因碼3碼了
            START = index  # 紀錄 開始位置
            A_three_word = 0  # 開始字元數歸零
            now_start = 0  # 開始狀態歸零
        else:
            print("")
    elif START != 0:  # 開始位置有紀錄才開始找結束基因碼
        # (遇到字元T或結束狀態開啟)結束字數未滿3，找結束矩陣
        if (inputStr[index] == "T" or now_end == 1) and T_three_word < 3:
            c = conversion_coordinates(inputStr[index])
            if inputStr[index] == "T":  # 遇到字元是T時
                now_end = 1  # 結束狀態開啟
                T_three_word = 1  # 紀錄結束字元數
                r = 1  # 字元A要從第二橫列開始找
            else:
                now_end = find_end_array(r, c)  # 找結束矩陣，確認結束狀態是否開啟
                if now_end == 1:  # 結束狀態開啟
                    r = c  # 將直行的數字給橫列，對應字元移動的順序
                    T_three_word += 1  # 結束字元數 +1
                if T_three_word == 3:  # 找到結束基因碼3碼了
                    S_E += 1  # 頭尾都有
                    END = index  # 紀錄 結束位置
                    T_three_word = 0  # 結束字元數歸零
                    now_end = 0  # 結束狀態歸零
                    three_gene(inputStr,START,END)# 印出基因碼
                    START = 0  # 開始的位置歸零
                    END = 0   # 結束的位置歸零
    else:
        print("")
    index += 1
# 除了有頭有尾以外的情況都找不到
if S_E == 0:
    print("no gene is found")
