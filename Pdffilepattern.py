# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 03:04:22 2023

@author: user
"""
#install...... pip install PyPDF2 on terminal
#exract pdf file

from PyPDF2 import PdfFileReader

#importing or extarcting pdf file content

from PyPDF2 import PdfReader

#creating a pdf reader object
reader=PdfReader('c:/1-Python/python_tutorial.pdf')

#printing numbers of pages in pdf file
print(len(reader.pages))

#getting a specific page from the pdf file
page=reader.pages[10]

#extracting text from pages
text=page.extract_text()
print(text)


#######################################################
import re
texts='''Hi: I have a problem  with my order number 412889912'''
patterns='order* [^\d]+(\d*)'
matchee=re.findall(patterns,texts)
matchee
#Output ['412889912']

#######################################################
import re
chat1='''Hi: Hello, I am having issue with my order #412889912'''
patterns='order* [^\d]+(\d*)'
matchee=re.findall(patterns,chat1)
matchee
#Output ['412889912']

#########################################################
chat2='''Hi:My order 412889912 is having an issue,I was charged 300$
when '''
patterns='order[^\d]*(\d*)'
matchee=re.findall(patterns,chat2)
matchee
#Output  ['412889912']

##########################################################
def get_pattern_match(pattern,text):
    matches=re.findall(pattern,text)
    if matches:
        return matches[0]
get_pattern_match('order[^\d]*(\d*)',chat1)
#Output  ['412889912']

#######################################################
#Retrieve email id and phone
chat1='Hi:you ask lots of questions 12345678912,abc@xyz.com'
chat2='Hi:here it is:(123)-567-8912,abc@xyz.com'
chat3='Hi:yes,phone:12345678912 email:abc@xyz.com'
get_pattern_match('[a-zA-Z0-9_]*@[a-z]*\.[a-zA-Z0-9]*',chat1)
get_pattern_match('[a-zA-Z0-9_]*@[a-z]*\.[a-zA-Z0-9]*',chat2)
