# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 16:26:29 2023

@author: user
"""
#######TEXT MINING################
sentence="we are Learning TextMining from Sanjivani AI"
#if we want to know position of learning
sentence.index("Learning")

##It will show learning is at position 7
#this is going to show character postion from 0 including

###########################
#we want to know postion TextMining word
sentence.split().index("TextMining")
##It will split the words in list and count the position
#if you want to see the list select sentence.split()
#it will show at 3
#############################
#suppose we want to print anu word in reverse order
sentence.split()[2][::-1]
#[start:end end:-1(start)] will start from -1,-2,-3
#learning will be printed as gninrael
########################################
sentence.split()[3][::-1]
#output  'gniniMtxeT'

####################################
#suppose we want to print first and last word of sentence
words=sentence.split()
first_word=words[0]
first_word
last_word=words[-1]
last_word
##now we want to concate the first and last word

concat_word=first_word+" "+last_word
concat_word

#############################
#we want to print even words from sentences
sentence.split()[::-2]

[words[i] for i in range(len(words)) if i%2==0]
#words having odd length will not be printed

###########
sentence
#now we want to display only AI
sentence[-3:]
##it will start from -3,-2,-1 i.e AI
#################
#suppose we wnat to reverse entire sentence
sentence[::-1]
# output:'IA inavijnaS morf gniniMtxeT gninraeL era ew'
#suppose we want to select each word and print in reversed order
words
print( " ".join(word[::-1] for word in words))
#o/p ew era gninraeL gniniMtxeT morf inavijnaS IA

############################################
#tokenization
import nltk
nltk.download('punkt')
from nltk import word_tokenize
words=word_tokenize("I am  reading NLP Fundamentals")
print(words)
#o/p:['I', 'am', 'reading', 'NLP', 'Fundamentals'] 

##############################################
#parts of speech tagging
nltk.download('averaged_perception_tagger')
nltk.pos_tag(words)
#######################################
#stop words from from NLTK library
from nltk.corpus import stopwords
stop_words=stopwords.words('English')
#you can have 179 stop words in variable explorer
print(stop_words)
sentence1="I am Learning NLP:It is one of the most popular library in python"
#first we will tokenize the sentence
sentence_words=word_tokenize(sentence1)
print(sentence_words)

#Now let us filter the sentence1 using stop_words
sentence_no_stops=" ".join([words for words in sentence_words if words not in stop_words ])
print(sentence_no_stops)
sentence1
#you can notice that am,is,of,the most popular,in are missing
##################################################
#suppose we want to replace words in string
sentence2="I visited My from IND on 14-02-19"
normalized_sentence=sentence2.replace("MY","Malaysia").replace("IND","India")
normalized_sentence=normalized_sentence.replace("-19","-2020")
print(normalized_sentence)
#o/p:I visited My from India on 14-02-2020
###########################################
#suppose we want auto correction in the sentence
#pip install autocorrect
from autocorrect import Speller
#declare the function Speller defined for english
spell=Speller(lang='en')
spell("Engilish")
#o/p: 'English'
####################################################
#suppose we want to correct whole sentence
sentence3="Ntural Languagee processsin deals withh the arrt of extracting sentiiments"
#let us first tokenize this sentence
sentence3=word_tokenize(sentence3)
corrected_sentence=" ".join([spell(word) for word in sentence3])
print(corrected_sentence)
#o/p:Natural Language processing deals with the art of extracting sentiments

###################################################
#Stemming
#used to remove ing,ed
stemmer=nltk.stem.PorterStemmer()
stemmer.stem("programming")
#o/p:'program'
stemmer.stem("programmed")
#o/p:'program'
stemmer.stem("Jumping")
#o/p:'jump'
stemmer.stem("Jumped")
#o/p:'jump'

######################################################
#lematizer
#mapping your words into dictionary form
nltk.download("wordnet")
from nltk.stem.wordnet import WordNetLemmatizer
lemmatizer=WordNetLemmatizer()
lemmatizer.lemmatize("programed")
lemmatizer.lemmatize("programs")
lemmatizer.lemmatize("battling")
lemmatizer.lemmatize("amazing")
############################
#chunking(shallow parsing)identifying named entities
nltk.download("maxent_ne_chunker")
nltk.download('averaged_perceptron_tagger')
nltk.download('words')
sentence4="We are learning NLP in python by SanjivaniAI "
#first we will tokenize
words=word_tokenize(sentence4)
words=nltk.pos_tag(words)
i=nltk.ne_chunk(words,binary=True)
[a for a in i if len(a)==1]
#o/p:[Tree('NE', [('NLP', 'NNP')]), Tree('NE', [('SanjivaniAI', 'NNP')])]
##################################################
#Sentence tokenization
from nltk.tokenize import sent_tokenize
sent=sent_tokenize("We are learning NLP in python. Delivered by sanjivaniAi. Do you know where it is located?It is in kopargaon")
sent
#o/p:['We are learning NLP in python.',
 #'Delivered by sanjivaniAi.',
 #'Do you know where it is located?It is in kopargaon']
################################
import nltk
from nltk.wsd import lesk
sentence1="keep your savings in the bank"
print(lesk(word_tokenize(sentence1),'bank'))
#o/p:Synset('saving_bank.n.02')
sentence2="It is so risky to drive over the bank of river"
print(lesk(word_tokenize(sentence2),'bank'))
#Synset('bank.v.07)
#synset('bank.n.07') a slope in the turn of a road or track
#the outside is higher than the inside in order to reduce the
#"bank" as multiple meaning.if you want to find exact meaning
#excute the following code
from nltk.corpus import wordnet as wn
from ss in wn.synsets('bank'):print(ss,ss.definition())