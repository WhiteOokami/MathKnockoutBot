from selenium import webdriver;
from selenium.webdriver.edge.options import Options
from multiprocessing import Queue
from selenium.webdriver.common.keys import Keys # import special key
import time
import sys
from datetime import datetime
import os
import tkinter as tk
from PIL import Image
import pytesseract
from PIL import ImageGrab
import re
import pyautogui
from pyautogui import *
import functools 
import threading

#image = ImageGrab.grab(bbox=(1600,800,1750, 870))
#image.show()
pyautogui.PAUSE = 0
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
options = webdriver.ChromeOptions()
options.add_argument("headless")
chromedriver = "C:\\Users\\alany\\Downloads\\Python Stuff\\chromedriver.exe"
browser = webdriver.Chrome(executable_path=chromedriver,options=options)

browser.get("https://toolkit.site/24point/")

#card1,card2,card2,card4 = ""
#def getForumula(card1,card2,card3,card4):
#    c1 = browser.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/input[1]")
#    c1.send_keys(Keys.BACKSPACE)
#    c1.send_keys(Keys.BACKSPACE)
#    c2 = browser.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/input[2]")
#    c2.send_keys(Keys.BACKSPACE)
#    c2.send_keys(Keys.BACKSPACE)
#    c3 = browser.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/input[3]")
#    c3.send_keys(Keys.BACKSPACE)
#    c3.send_keys(Keys.BACKSPACE)
#    c4 = browser.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/input[4]")
#    c4.send_keys(Keys.BACKSPACE)
#    c4.send_keys(Keys.BACKSPACE)
#    c1.send_keys(card1)
#    c2.send_keys(card2)
#    c3.send_keys(card3)
#    c4.send_keys(card4)
#    element = browser.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/button[2]")
#    element.click()
#   # time.sleep(0.5)
#    solution = browser.find_element_by_xpath("/html/body/div[1]/div/div/textarea")
#    print(solution.text.split()[0])
#    return solution.text.split()[0]


from itertools import permutations
 
def solve(my_list):
     # Randomly arrange a list of 4 integers
    result = [c for c in permutations(my_list, 4)]
 
    symbols = ["+", "-", "*", "/"]
 
    list2 = [] # Calculate the list of 24 permutations and combinations
 
    flag = False
 
    for one, two, three, four in result:
        for s1 in symbols:
            for s2 in symbols:
                for s3 in symbols:
                    if s1 + s2 + s3 == "+++" or s1 + s2 + s3 == "***":
                        express = ["{0}{1}{2}{3}{4}{5}{6}".format(one, s1, two, s2, three, s3, four)] # When adding or multiplying , The brackets have no meaning.
                    else:
                        express = ["(({0}{1}{2}){3}{4}){5}{6}".format(one, s1, two, s2, three, s3, four),
                                   "({0}{1}{2}){3}({4}{5}{6})".format(one, s1, two, s2, three, s3, four),
                                   "(({0}{1}({2}{3}{4})){5}{6})".format(one, s1, two, s2, three, s3, four),
                                   "{0}{1}(({2}{3}{4}){5}{6})".format(one, s1, two, s2, three, s3, four),
                                   "{0}{1}({2}{3}({4}{5}{6}))".format(one, s1, two, s2, three, s3, four)]
 
                    for e in express:
                        try:
                            if eval(e) == 24:
                                list2.append(e)
                                flag = True
                        except ZeroDivisionError:
                            pass

    print(list2[0])
    return list2[0]

def replace_chars(text):
    list_of_numbers = re.findall(r'\d+', text)
    result_number = ''.join(list_of_numbers)
    return result_number

#image.save('sc.png')
#img1 = Image.open("card1.jpg")
num1 = num2 = num3 = num4 = ""
#def getCard1():
#    while True:
#        global num1
#        num1 = replace_chars(pytesseract.image_to_string(ImageGrab.grab(bbox=(1330,800,1500, 870)), config='--psm 6'))

#def getCard2():
#    while True:
#        global num2
#        num2 = replace_chars(pytesseract.image_to_string(ImageGrab.grab(bbox=(1500,800,1600, 870)), config='--psm 6'))

#def getCard3():
#    while True:
#        global num3
#        num3 = replace_chars(pytesseract.image_to_string(ImageGrab.grab(bbox=(1600,800,1750, 870)), config='--psm 6'))

#def getCard4():
#    while True:
#        global num4
#        num4 = replace_chars(pytesseract.image_to_string(ImageGrab.grab(bbox=(1750,800,1900, 870)), config='--psm 6'))

def getCards():
    num1 = replace_chars(pytesseract.image_to_string(ImageGrab.grab(bbox=(1330,800,1500, 870)), config='--psm 6'))
    if (num1 == ""):
        num1 = replace_chars(pytesseract.image_to_string(ImageGrab.grab(bbox=(1330,800,1500, 870)), config='--psm 6'))
    num2 = replace_chars(pytesseract.image_to_string(ImageGrab.grab(bbox=(1500,800,1600, 870)), config='--psm 6'))
    num3 = replace_chars(pytesseract.image_to_string(ImageGrab.grab(bbox=(1600,800,1750, 870)), config='--psm 6'))
    num4 = replace_chars(pytesseract.image_to_string(ImageGrab.grab(bbox=(1750,800,1900, 870)), config='--psm 6'))
    print(num1)
    print(num2)
    print(num3)
    print(num4)
    return (num1,num2,num3,num4)
cd1=cd2=cd3=cd4 = "0"
def press(item):
    global cd1,cd2,cd3,cd4
    if (item == '+'):
        pyautogui.click(x=1371,y=909)
    elif (item == '-'):
        pyautogui.click(x=1476,y=909)
    elif (item == '*'):
        pyautogui.click(x=1567,y=909)
    elif (item == '/'):
        pyautogui.click(x=1666,y=909)
    elif (item == '('):
        pyautogui.click(x=1757,y=909)
    elif (item == ')'):
        pyautogui.click(x=1851,y=909)
    elif (item == cd1):
        pyautogui.click(x=1400,y=832)
        cd1 = "0"
    elif (item == cd2):
        pyautogui.click(x=1545,y=832)
        cd2 = "0"
    elif (item == cd3):
        pyautogui.click(x=1692,y=832)
        cd3 = "0"
    elif (item == cd4):
        pyautogui.click(x=1834,y=832)
        cd4 = "0"
    elif (item == 'e'):
        pyautogui.click(x=1648,y=1002)
    elif (item == 's'):
        pyautogui.click(x=1603,y=521)
def split(word):
    return [char for char in word] 

j =0
choice = ''
while choice != 'y':
    choice = input("start? (y/n): ")

#threading.Thread(target=getCard1).start()
#threading.Thread(target=getCard2).start()
#threading.Thread(target=getCard3).start() 
#threading.Thread(target=getCard4).start()
time.sleep(1)
press('s')
while True:
    time.sleep(0.8)
    j+=1
    print("------"+str(j)+"-----")
    cards = getCards()
    cd1,cd2,cd3,cd4 = cards
    print(cards)
    formula = solve([int(n) for n in cards])
   # print(formula)
    
   #formula = getForumula(cards[0],cards[1],cards[2],cards[3])
    operations = ['-','+','*','/','(',')']
    nums = ['1','2','3','4','5','6','7','8','9','0']
    i = 0
    while i<len(formula):
        if (formula[i] in operations):
            press(formula[i])
            i+=1
        elif (formula[i] in nums):
            if (i<len(formula)-1):
                if (formula[i+1] in nums):
                    press(formula[i]+formula[i+1])
                    i+=2
                else:
                    press(formula[i])
                    i+=1
            else:
                press(formula[i])
                i+=1

    #time.sleep(2)
    press('e')

