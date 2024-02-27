########Natural Language Processing###################


#Install regex

import re
text='''
Elon musk's phone number is 9991116666, call him if you have any questions on dodgecoin. Tesla's revenue is 40 billion
Tesla's CFO number (999)-333-7777
 and tesla's revenue is 20 billion'''
pattern=r'\d\d\d\d\d\d\d\d\d\d'
matches=re.findall(pattern,text)
matches


text='''
Elon musk's phone number is 9991116666, call him if you have any questions on dodgecoin. Tesla's revenue is 40 billion
Tesla's CFO number (999)-333-7777
 and tesla's revenue is 20 billion'''
pattern=r'\d{10}'
matches=re.findall(pattern,text)
matches
#output  9991116666

text='''
Elon musk's phone number is 9991116666, call him if you have any questions on dodgecoin. Tesla's revenue is 40 billion
Tesla's CFO number (999)-333-7777
 and tesla's revenue is 20 billion'''
pattern=r'\(\d{3}\)-\d{3}-\d{4}'
matches=re.findall(pattern,text)
matches
#Output ['(999)-333-7777']


pattern=r'\(\d{3}\)-\d{3,4}'
matches=re.findall(pattern,text)
matches
#output  ['(999)-333']

pattern=r'\(\d{3}\)-\d{3}-\d{4}|\d{10}'
matches=re.findall(pattern,text)
matches
#Output ['9991116666', '(999)-333-7777']


#we want any character except; and - pattern will be [^;-]
text2='''A protracted; legal battle; over a 32-carat;
 Golconda diamond-'''
pattern='[^;-]'
matches=re.findall(pattern,text2)
matches


'''Google tesla company fillings
click on annual & Quarterly reports
apply filters
click on 10-Q
goto-Notes consolidated financial statements (unaudited)
Now we want to extract title
'''

text3='''Note 2 - Summary of Significant Accounting Policies
Unaudited Interim Financial Statements
The consolidated balance sheet as of September 30, 2022, the consolidated statements of operations, the consolidated statements of
comprehensive income, the consolidated statements of redeemable noncontrolling interests and equity for the three and nine months ended September
30, 2022 and 2021 and the consolidated statements of cash flows for the nine months ended September 30, 2022 and 2021, as well as other information
disclosed in the accompanying notes, are unaudited. The consolidated balance sheet as of December 31, 2021 was derived from the audited
consolidated financial statements as of that date. The interim consolidated financial statements and the accompanying notes should be read in
conjunction with the annual consolidated financial statements and the accompanying notes contained in our Annual Report on Form 10-K for the year
ended December 31, 2021.
The interim consolidated financial statements and the accompanying notes have been prepared on the same basis as the annual consolidated
financial statements and, in the opinion of management, reflect all adjustments, which include only normal recurring adjustments, necessary for a fair
statement of the results of operations for the periods presented. The consolidated results of operations for any interim period are not necessarily
indicative of the results to be expected for the full year or for any other future years or interim periods'''


pattern='Note \d – [^\n]+'
matches=re.findall(pattern,text3)
matches

#output['Note 2 – Summary of Significant Accounting Policies']

###################################################
pattern='Note \d - ([^\n]+)'
matches=re.findall(pattern,text3)
matches
#Output ['Summary of Significant Accounting Policies']



##########################################################

#quarters can be Q1,Q2,Q3, or Q4 not Q5 or Q6
#copy the content in string window
 
text4='''The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. FY2020 Q4 it was $3 billion. The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. FY2020 Q4 it was $3 billion.'''
pattern='FY\d{4} Q\d'
matches=re.findall(pattern,text4)
matches
#in the right bottom corner their is 
#option single character a,b, or c[abc]
#Output ['FY2021 Q1', 'FY2020 Q4', 'FY2021 Q1', 'FY2020 Q4']

#########################################################
'''OR'''
pattern='FY\d{4} Q[1234]'
matches=re.findall(pattern,text4)
matches
#same output

###########################################################

'''OR'''
'''By giving range'''
pattern='FY\d{4} Q[1-4]'
matches=re.findall(pattern,text4)
matches
#Same output

##########################################
pattern1='fy\d{4} Q[1-4]'
matches=re.findall(pattern,text4)
matches
#####################################################
''' Now we are getting ['FY2021 Q1']
In order to solve this issue ,re,IGNORECASE' '''
pattern1='FY\d{4} Q[1-4]|fy\d{4} Q[1-4]'
pattern1
matches=re.findall(pattern,text4)
matches
#output ['2021 Q1', '2020 Q4', '2021 Q1', '2020 Q4']

######################################################
'''Now let us assume we want only 2021 Q1 and 2020 Q4
then you can get extract through(...)'''
pattern='FY(\d{4} Q[1-4])'
matches=re.findall(pattern,text4,re.IGNORECASE)
matches

#Output ['2021 Q1', '2020 Q4', '2021 Q1', '2020 Q4']

######################################################

'''Now let us assume that we want to find financial number'''


text6='''The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. FY2020 Q4 it was $3 billion. The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. FY2020 Q4 it was $3 billion.'''

#we want $4.85 and $3
#simply $ can not be used as it is special symbol
#pl ref right bottom window
#even . character can not be used 
pattern='\$[0-9\.]+'
matched=re.findall(pattern,text6)
matched
#['$4.85', '$3']

#if we dont want $
pattern='\$([0-9\.]+)'
matched=re.findall(pattern,text6)
matched
#['4.85', '3', '4.85', '3']