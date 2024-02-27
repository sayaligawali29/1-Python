

'''tokenization 
1)Word
2)Sentence'''

txt='Welcome to the new year 2023'
x=txt.split()
print(x)

#########################################################
'''Removing special character'''
#re.sub()method is used to remove special character
import re
def remove_special_characters(text):
    pat=r'[^a-zA-z0-9.,!?:;\"\'\s]'
    return re.sub(pat,'',text)#sub()substitute
remove_special_characters("007 Not Sure@ if this @ % was good")
#Output '007 Not Sure if this   was good'

####################################################
'''Removing Numbers'''
import re
def remove_special_characters(text):
    pat=r'[^a-zA-z.,!?:;\"\'\s]'
    return re.sub(pat,'',text)#sub()substitute
remove_special_characters("007 Not Sure@ if this @ % was good")
#output ' Not Sure if this   was good'

###########################################
txt='welcome:to the new year;2023!'
import re
x=re.split(r'(?:,/;/\s)\s*',txt)
print(x)
#Output ['welcom:to the new year;2023!']

#############################################################
'''Removing Punctuation'''

import string
text='welcome:to the new year;2023!'
def remove_punctuation(text):
    text=''.join([c for c in text if c not in string.punctuation])
    return text
remove_punctuation('Article:@First sentence of some,{important} article having lot of ~ punctuations.And another one;!')


###########################################################
#Stemming
#removing 'es,ed,ing
import nltk
def get_stem(text):
    stemmer=nltk.porter.PorterStemmer()
    text=' '.join([stemmer.stem(word) for word in text.split()])
    return text
get_stem("We are eating and swimming; we have eating and swimming;he eats and swims;he ate and swam")

#######################################################


'''
matching text at the start or end of string
'''
import re
filename='spam.txt'
filename.endswith('.txt')

###############################################################
area_name='6 th lane west Andheri'
area_name.endswith('west Andheri')

################################################
choices=('http:','ftp:')
url='http://www.python.org'
url.startswith(choices)
######################################################

#slicing of string

S='ABCDEFGH'
print(S[2:7])
#CDEFG
#note that the item at index 7 'H' is not  included
#################################################
#slicing with negative indexes
S='ABCDEFGH'
print(S[-7:-2])
#BCDEF
################################################
#slicing with positive and negative  indices
S='ABCDEFGH'
print(S[2:-5])
###########################################
#Specify step of slicing
#rturn 2nd item  between position  2 to 7
S='ABCDEFGH'
print(S[2:7:2])
#return 2nd item between 6 to 1
print(S[6:1:-2])
#######################################
#Slice first three character
print(S[:3])

###########################################
#slice last three characters
print(S[3:])
################################################
#reverse a string
print(S[::-1])
####################################################
#similar operation can be done  with slices
filename='spam.txt'
filename[-4:]=='.txt'

###################################################
url='http://www.python.org'
url[:5] == 'http:' or url[:6] == 'https:' or url[:4]=='ftp:'
###################################################

#to check the file extention
from fnmatch import fnmatch, fnmatchcase
names=['Dot1.csv', 'Dat2.csv', 'config.ini','foo.py']
[name for name in names if fnmatch(name,'Dat*.csv')]

##################################################
from fnmatch import fnmatch, fnmatchcase
names=['Andheri East','Parle East','Dadar West']
[name for name in names if fnmatch(name,'East.csv')]
##################################################

#you could  write list comprehension loke this
addresses = [
    '5412 N CLARK ST',
    '1060 W ADDISON ST',
    '1039 W GRANVILLE AVE',
    '2122 N CLARK ST',
    '4802 N BROADWAY',
    ]

from fnmatch import fnmatchcase
[addr for addr in addresses if fnmatchcase(addr,'* ST')]
text = 'yeah, but no, but yeah, but no, but yeah'
text='yeah'
text.startswith('yeah')
#True
text.endswith('no')
#False
#search for the location of the first occurance
text.find('no')
##################################################
text1='11/27/2012'
text2='Nov 27,2012'
import re
#simple matching:\d+ means match one or more
if re.match(r'\d+/\d+/\d',text1):
    print('yes')
else:
    print('no')
if re.match(r'\d+/\d+/\d',text2):
    print('yes')
else:
    print('no')
    
####################################################
datepat=re.compile(r'(\d+)/(\d+)/(\d+)')
if re.match(datepat,text1):
    print('yes')
else:
    print('no')
#yes
if re.match(datepat,text2):
    print('yes')
else:
    print('no')
#no
#######################################################
#searching and replacing text
text='yeah,but no,but yeah,but no,but yeah' 
text.replace('yeah','yep')
#'yep,but no,but yep,but no,but yep'
#######################################################
'''if you have date in form 11/27/2012 want to 
convert 2012-11-27'''
text='Today is 11/27/2012. PyCon starts 3/13/2013.'
import re
re.sub(r'(\d+)/(\d+)/(\d+)',r'\3-\1-\2',text)
#\3 3rd group,1st group
#Output  'Today is 2012-11-27. PyCon starts 2013-3-13.'
########################################################
#if you want to know how many substitution are made
#in text then
#you can use subn() method
newtext,n=datepat.subn(r'\3-\1-\2',text)
newtext
n
##################################################
text='UPPER PYTHON,Lower python,Mixed Python'
re.findall('python',text,flags=re.IGNORECASE)
#Output ['PYTHON', 'python', 'Python']
#to substitute
re.sub('python','snake',text,flags=re.IGNORECASE)
#Output 'UPPER snake,Lower snake,Mixed snakes

###################################################
''' The last example reveals a limitation that replacing
text wont match the case of the matched text.if you need to fix this, you might
have to use a support function,as in the following'''
import re
def matchcase(word):
    def replace(m):
        text=m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    return replace
text3=re.sub('python',matchcase('snake'),text,flags=re.IGNORECASE)
text3
#Output 'UPPER SNAKE,Lower snake,Mixed Snake'
##########################################################
'''You are trying to match a text pattern using regular expression
but it is identifying the longest possible mtches of a pattern instead
u would like to change it to find the shortest possible match
this problem often arises in patterns that try to match
text enclosed inside a pair of starting and ending delimiters
to illustrate consider this example'''
str_pat=re.compile(r'\"(.*)\"')
text1='computer says,"no."'
str_pat.findall(text1)
#output ['no.']
#However if we have text as below
text2='Computer says "no."Phone says "yes."'
str_pat.findall(text2)
#OUTPUT  ['no."Phone says "yes.']

################################################
#to remove the drawback
'''in this example the pattern r'\"(.*)\" is attempting
to match text enclosed inside quotes.however,the * operator
in a regular expression is greedy so matching is based on finding the longest possible
match'''
str_pat=re.compile(r'\"(.*?)\"') 
str_pat.findall(text2)
#Output ['no.', 'yes.']

##########################################
comment=re.compile(r'/\"*(.*?)\*/')
text1='/* this is a comment */'
comment.findall(text1)
#[' this is a comment ']

text2='''/*this is a 
multiline comment'''
comment.findall(text2)
#output []

####################################################
#to fix the problem ,you can add support for newlines
#for example:
comment = re.compile(r'/\*((?:.|\n)*?)\*/')
comment.findall(text2)

###############################
'''there is another option which addresses this problem the
re.compile() function accepts a flag ,re.DOTALL, which is use
ful here.it makes
the .in a regular expression match all characters ,including
'''
comment=re.compile(r'/\*(.*?)\*/',re.DOTALL)
comment.findall(text2)

####################################################
'''normalizing unicode text to standard representation
you are working with unicode strings,but need to make sure that all
of the string have the same underlying represenatation'''

s1= 'Spicy Jalape\u00f1o'
s2= 'Spicy Jalapen\u0303o'
print(s1)#Spicy Jalapeño
print(s2)#Spicy Jalapeño
s1==s2
#False

########################################################
##UNICODE
#UTF unicode transformation format
string1="apple"
string2="jeei125"
string3="12345"
string4="pre@12"
string1.encode(encoding='UTF-8',errors='strict')
string2.encode(encoding='UTF-8',errors='strict')
string3.encode(encoding='UTF-8',errors='strict')
string4.encode(encoding='UTF-8',errors='strict')

#########################################################


text='one 🐘 and three 🐋'
print(text)
print(len(text))
'''we encode the string into a bytes using the utf8 encoding
and print the bytes we count the number of bytes in this encoding type'''
e=text.encode('utf8')
print(e)
#b'one \xf0\x9f\x90\x98 and three \xf0\x9f\x90\x8b'
print(len(e))


########################################################
fname='data.txt'
with open(fname,mode='rb')as f:
    #by default it encodes in utf-8
    contents=f.read()
    print(type(contents))
    print(contents)
    print(contents.decode('utf8'))
#one 🐘 and three 🐋

####################################################
#for utf16
fname='data.txt'
with open(fname,mode='rb')as f:
    #by default it encodes in utf-8
    contents=f.read()
    print(type(contents))
    print(contents)
    print(contents.decode('utf16'))

################################################
#STRIPPING
#discard unwanted characters
#to remove whitespace
s='   hello world   \n'
s.strip()
#'hello world'

#left strip
s='   hello world  \n'
s.lstrip()
#'hello world  \n'

#right strip
s='   hello world  \n'
s.rstrip()
#'   hello world'

#########################
#character stripping
#this is only for uniform pattern
t='-------hello====='
t.lstrip('-')
#'hello====='

t='------hello====='
t.strip('-=')
#'hello'

############################################
s=' hello world   \n'
s=s.strip()
s
s.replace(' ','')
#'helloworld'

######################################################
import re
re.sub('\s+',' ',s)
#'hello world'

######################################################
#Aliging the text string
#Adjusting the text left or right
text='Hello World'
text.ljust(20)
#'Hello World  

text='Hello World'
text.rjust(20)
#'         Hello World'

text='Hello World'
text.center(20)
#'    Hello World     '

text.rjust(20,'=')
#'=========Hello World'

text.center(20,'*')
#'****Hello World*****'

###############################################
'''>for left
< for right
^ center'''
format(text,'>20')
#'         Hello World'

format(text,'<20')
#'Hello World         '

format(text,'^20')
# '    Hello World     '

####################################################
'''here you can add characters to fill the as above if you want
to include a format'''

format(text,'=>20s')
#'=========Hello World'

format(text,'*^20s')
# '****Hello World*****'

##########################################################
#These format codes can also be used in this format values
#: is used for starting and ending value
'{:>10s} {:>10s}'.format('Hello','World')
# '     Hello      World'

##########################################
'''one benefits of format() is that it is not specific to 
string making it more general purpose.for instance ,you can use it'''
x=1.2345
format(x,'>10')
x
format(x,'>10.2f')


####################################################
parts=['Is','Chicago','Not','Chicago?']
' '.join(parts)
#'Is Chicago Not Chicago?'
','.join(parts)
#'Is,Chicago,Not,Chicago?'
''.join(parts)
# 'IsChicagoNotChicago?'