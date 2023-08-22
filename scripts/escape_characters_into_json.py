# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 14:57:01 2023

@author: avery
"""

import re                                   # for regular expressions
import os                                   # to look up operating system-based info
import string                               # to do fancy things with strings
import glob                                 # to locate a specific file type
from pathlib import Path                    # to access files in other directories   
import pandas as pd                         # to sort and organize data
import nltk                                 # to access stop words
from collections import Counter             # for word counts
from nltk.corpus import stopwords           # import set of stop words
from nltk.tokenize import word_tokenize     # lets us tokenize
import csv                                  # lets us read and write CSVs
import json



dirpath = r'C:\Users\avery\Desktop\VRT_seed_articles' # get file path for corpora (you can change this)




file_type = ".txt" # if your data is not in a plain text format, you can change this
filenames = []  # this variable will hold the locations of each file

 # this for loop will run through folders and subfolders looking for a specific file type
for root, dirs, files in os.walk(dirpath, topdown=False):
   # look through all the files in the given directory
   for name in files:
       if (root + os.sep + name).endswith(file_type):
           filenames.append(os.path.join(root, name))
   # look through all the directories
   for name in dirs:
       if (root + os.sep + name).endswith(file_type):
           filenames.append(os.path.join(root, name))

number = 1   

for filename in filenames:
    with open(filename, encoding='utf-8') as afile:
        text = afile.read()
        text = text.replace(os.linesep, "\n")
        date = filename[-20:-10]
        ident = "white_supremacy_newspapers_" + str(number)
        number = number + 1
        lcn = filename[-31:-21]
        dic = {'id':ident, "series": "white_supremacy_newspapers", 'lcn': lcn, "date": date, 'text':text}
        new_filename = str(filename[:-4]).replace(r"C:\Users\avery\Desktop\VRT_seed_articles","") + '.json'
        new_filename = os.path.basename(os.path.normpath(new_filename))
        with open(new_filename, 'w', encoding='utf-8') as f:
            json.dump(dic, f, ensure_ascii=False, indent=4)