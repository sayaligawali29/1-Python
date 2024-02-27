# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 09:02:29 2023

@author: user
"""
#by using regex package
import re
sentence5="sharat twitted ,Wittnessing 70th republic day India from Rajpath new Delhi,Mesmorizing performance by Indian Army"
re.sub(r'([^\s\w]|_)+', ' ',sentence5).split()
'''o/p"
['sharat',
 'twitted',
 'Wittnessing',
 '70th',
 'republic',
 'day',
 'India',
 'from',
 'Rajpath',
 'new',
 'Delhi',
 'Mesmorizing',
 'performance',
 'by',
 'Indian',
 'Army']'''
#extracting n-grams
#n-gram can be extracted using three technique
#1.custom defined function
#2.nltk
#3.TextBlob
###############################################
#extractinf n-gram using custom defined function

import re
def n_gram_extractor(input_str, n):
    tokens=re.sub(r'([^\s\w]|_)+', ' ',input_str).split()
    for i in range(len(tokens)-n+1):
        print(tokens[i:i+n])
n_gram_extractor("The cute Little boy is playing with kitten",2)
'''o/p:
    ['The', 'cute']
    ['cute', 'Little']
    ['Little', 'boy']
    ['boy', 'is']
    ['is', 'playing']
    ['playing', 'with']
    ['with', 'kitten']'''
n_gram_extractor("The cute Little boy is playing with kitten",3)
'''o/p:
    ['The', 'cute', 'Little']
    ['cute', 'Little', 'boy']
    ['Little', 'boy', 'is']
    ['boy', 'is', 'playing']
    ['is', 'playing', 'with']
    ['playing', 'with', 'kitten']'''
    
#################################################
import nltk
from nltk import ngrams
#extraction n-grams with nltk
list(ngrams("The cute Little boy is playing with kitten".split(),2))
'''o/p:
    ['The', 'cute']
    ['cute', 'Little']
    ['Little', 'boy']
    ['boy', 'is']
    ['is', 'playing']
    ['playing', 'with']
    ['with', 'kitten']'''
list(ngrams("The cute Little boy is playing with kitten".split(),3))
'''o/p:
    ['The', 'cute', 'Little']
    ['cute', 'Little', 'boy']
    ['Little', 'boy', 'is']
    ['boy', 'is', 'playing']
    ['is', 'playing', 'with']
    ['playing', 'with', 'kitten']'''
###################################
from textblob import TextBlob
blob=TextBlob("The cute little boy is playing with kitten.")
blob.ngrams(n=2)
blob.ngrams(n=3)
'''o:p:
    [WordList(['The', 'cute']),
     WordList(['cute', 'little']),
     WordList(['little', 'boy']),
     WordList(['boy', 'is']),
     WordList(['is', 'playing']),
     WordList(['playing', 'with']),
     WordList(['with', 'kitten'])]'''
################################################
##Tokenization using Keras
sentence5
from keras.preprocessing.text import text_to_word_sequence
text_to_word_sequence(sentence5)
'''o/p:
    ['sharat',
     'twitted',
     'wittnessing',
     '70th',
     'republic',
     'day',
     'india',
     'from',
     'rajpath',
     'new',
     'delhi',
     'mesmorizing',
     'performance',
     'by',
     'indian',
     'army']'''
#############################################
from textblob import TextBlob
blob=TextBlob(sentence5)
blob.words
'''o/p:
    WordList(['sharat', 'twitted', 'Wittnessing', 
              '70th', 'republic', 'day', 'India', 
              'from', 'Rajpath', 'new', 'Delhi', 
              'Mesmorizing', 'performance', 'by',
              'Indian', 'Army'])'''
###############################################
##Types of tokenizer
#1.Tweet tokenizer
from nltk.tokenize import TweetTokenizer
tweet_tokenizer=TweetTokenizer()
tweet_tokenizer.tokenize(sentence5)
'''o/p:
    ['sharat',
     'twitted',
     ',',
     'Wittnessing',
     '70th',
     'republic',
     'day',
     'India',
     'from',
     'Rajpath',
     'new',
     'Delhi',
     ',',
     'Mesmorizing',
     'performance',
     'by',
     'Indian',
     'Army']'''
#########################################
#Multi-Word_Expression
from nltk.tokenize import MWETokenizer
sentence5
mwe_tokenizer=MWETokenizer([('republic','day')])
mwe_tokenizer.tokenize(sentence5.split())
mwe_tokenizer.tokenizer.tokenize(sentence5.replace('i',' ').split())
'''o/p:
    ['sharat',
     'twitted',
     ',Wittnessing',
     '70th',
     'republic_day',
     'India',
     'from',
     'Rajpath',
     'new',
     'Delhi,Mesmorizing',
     'performance',
     'by',
     'Indian',
     'Army']'''
##################################
#Regular Expression Tokenizer
from nltk.tokenize import RegexpTokenizer
reg_tokenizer=RegexpTokenizer('\w+\|\$[\d\.]+|\S+')
reg_tokenizer.tokenize(sentence5)
'''o/p:
    ['sharat',
     'twitted',
     ',Wittnessing',
     '70th',
     'republic',
     'day',
     'India',
     'from',
     'Rajpath',
     'new',
     'Delhi,Mesmorizing',
     'performance',
     'by',
     'Indian',
     'Army']'''
################################
#white space tokenizer
from nltk.tokenize import WhitespaceTokenizer
wh_tokenizer=WhitespaceTokenizer()
wh_tokenizer.tokenize(sentence5)
'''o/p:
    ['sharat',
     'twitted',
     ',Wittnessing',
     '70th',
     'republic',
     'day',
     'India',
     'from',
     'Rajpath',
     'new',
     'Delhi,Mesmorizing',
     'performance',
     'by',
     'Indian',
     'Army']'''
####################################
from nltk.tokenize import WordPunctTokenizer
wp_tokenizer=WordPunctTokenizer()
wp_tokenizer.tokenize(sentence5)

'''o/p:
    ['sharat',
     'twitted',
     ',',
     'Wittnessing',
     '70th',
     'republic',
     'day',
     'India',
     'from',
     'Rajpath',
     'new',
     'Delhi',
     ',',
     'Mesmorizing',
     'performance',
     'by',
     'Indian',
     'Army']'''
################################
sentence6="I love playing cricket.Cricket player practices hard in their inning"
from nltk.stem import RegexpStemmer
regex_stemmer=RegexpStemmer('ing$')
' '.join(regex_stemmer.stem(wd) for wd in sentence6.split())
'''o/p:
    'I love play cricket.Cricket player practices hard in their inn'''
#######################################
sentence7="Before eating , it would be nice to sanitize your hand with a sanitizer"
from nltk.stem.porter import PorterStemmer
ps_stemmer=PorterStemmer()
words=sentence7.split()
" ".join([ps_stemmer.stem(wd) for wd in words])
'''o/p:
    'befor eat , it would be nice to sanit your hand with a sanit'''
###########################################
#Lemmatization
import nltk
from nltk.stem import WordNetLemmatizer
from nltk import word_tokenize
nltk.download('wordnet')
lemmatizer=WordNetLemmatizer()
sentence8="The codes executed today are far better than what we excute"
words=word_tokenize(sentence8)
" ".join([lemmatizer.lemmatize(word) for word in words])
#####################################
#Singularize and pluralization
from textblob import TextBlob 
sentence9=TextBlob("She sells seashells on the seashore")
words=sentence9.words
#we want to make[2] i.e seashells in sigular form
sentence9.words[2].singularize()
#o/p:'seashell'
#we want word 5 i.e seashore in plural form
sentence9.words[5].pluralize()
#o\p:'seashores'
##############################################
#language translation from spanish to English
from textblob import TextBlob
en_blob=TextBlob(u'muy bien')
en_blob.translate(from_lang='es',to='en')
#o/p:TextBlob("very good")
########################################################
#custom stopwords removal
from nltk import word_tokenize
sentence9="She sells seashells on the seashore"
custom_stop_word_list=['she','on','the','am','is']
words=word_tokenize(sentence9)
" ".join([word for word in words if word.lower() not in custom_stop_word_list])
#o/p:'sells seashells seashore'
# select words which are not in defined list
#######################################################
#extracting general feature from raw text
#number of words
#detect presence of wh words
#polarity
#subjectivity
#langauage identification
###################################################
#To identify the number of words
import pandas as pd
df=pd.DataFrame([['The vaccine for covid-19 will be announced on 1st August'],['Do you know how much expectations the world population is having from this research?'],['The risk of virus will come to end on 31st July']])
df.columns=['text']
df
''' o/p:text
0  The vaccine for covid-19 will be announced on ...
1  Do you know how much expectations the world po...
2    The risk of virus will come to end on 31st July'''
#################################################
#Now let us measure the number of words
from textblob import TextBlob
df['number_of_words']=df['text'].apply(lambda x:len(TextBlob(x).words))
df['number_of_words']
'''
o/p:
    0    10
    1    14
    2    11
'''
######################################
#detect presence of words wh
wh_words=set(['why','who','which','what','where','when','how'])
df['is_wh_words_present']=df['text'].apply(lambda x:True if len(set(TextBlob(str(x)).words).intersection(wh_words))>0 else False)
df['is_wh_words_present']
'''
o/p:
    0    False
    1     True
    2    False
    '''
##########################################
##polarity of the sentence
df['polarity']=df['text'].apply(lambda x:TextBlob(str(x)).sentiment.polarity)
df['polarity']
'''o/p:
    0    0.0
    1    0.2
    2    0.0
'''
sentence10="I like this example very much"
pol=TextBlob(sentence10).sentiment.polarity
pol
#0.26
sentence10="THis is fantastic example and I like it very much"
pol=TextBlob(sentence10).sentiment.polarity
pol
# 0.33
sentence10="This was helpful example but I would have prefer another"
pol=TextBlob(sentence10).sentiment.polarity
pol
#0.0
sentence10="This is my personal opinion that is was helpful example but I would prefer another one"
pol=TextBlob(sentence10).sentiment.polarity
pol
#0.0
#################################################
#subjectivity of the dataframe df and check whether there is 
df['subjectivity']=df['text'].apply(lambda x:TextBlob(str(x)).sentiment.polarity)
df['subjectivity']
'''o/p:
    0    0.0
    1    0.2
    2    0.0'''
##############################################
#to find language of the sentence this part of code will get http error
df['language']=df['text'].apply(lambda x:TextBlob(str(x)).detect_language())
#############################################
#bag of words
# this BoW converts unstructured data to structured form
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
corpus=['At least seven isean pharma companies are working to develop vaccine against the corona virus','The deadly virus that has  already infected more than 14 million globally','Bharat biotech is the among the domastic pharma firm the working on the corona virus vaccine in India']
bag_of_word_model=CountVectorizer()
print(bag_of_word_model.fit_transform(corpus).todense())

bag_of_word_df=pd.DataFrame(bag_of_word_model.fit_transform(corpus).todense())
#this will create datframe
bag_of_word_df.columns=sorted(bag_of_word_model.vocabulary_)
bag_of_word_df.head()
'''o/p:
    0   0        1        0      0    1   1  ...     0    1   1        1      1        1
    1   1        0        1      0    0   0  ...     1    1   0        0      1        0
    2   0        0        0      1    0   0  ...     0    4   0        1      1        1'''
###############################################
#bag of words model small
bag_of_word_model_small=CountVectorizer(max_features=5)
bag_of_word_df_small=pd.DataFrame(bag_of_word_model_small.fit_transform(corpus).todense())
bag_of_word_df_small.columns=sorted(bag_of_word_model_small.vocabulary_)
bag_of_word_df.head()
###############################################