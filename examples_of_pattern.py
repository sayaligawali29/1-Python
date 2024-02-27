import re

text='''Born	Elon Reeve Musk
June 28, 1971 (age 52)
Pretoria, Transvaal, South Africa
Education	University of Pennsylvania (BA, BS)
Title	
Founder, CEO, and chief engineer of SpaceX
CEO and product architect of Tesla, Inc.
Owner and CTO of Twitter
President of the Musk Foundation
Founder of the Boring Company, X Corp., and xAI
Co-founder of Neuralink, OpenAI, Zip2, and X.com (part of PayPal)
Spouses	
Justine Wilson
​
​(m. 2000; div. 2008)​
Talulah Riley
​
​(m. 2010; div. 2012)​
​
​(m. 2013; div. 2016)​
Partner	Grimes (2018–2021)[1]
Children	10[2]
Parents	
Errol Musk
Maye Musk
Family	Musk family'''

def get_pattern_match(pattern,text):
    matches=re.findall(pattern,text)
    if matches:
        return matches[0]

get_pattern_match(r'age (\d+)',text)
get_pattern_match(r'Born(.*)\n',text).strip()
get_pattern_match(r'Born.*\n(.*)\(age',text).strip()
get_pattern_match(r'\(age.*\n(.*)',text)



#######################################################
def extract_personal_information(text):
    age=get_pattern_match('age (\d+)',text)
    full_name=get_pattern_match('Born(.*)\n',text)
    birth_date=get_pattern_match('Born.*\n(.*)\(age',text)
    birth_place=get_pattern_match('\(age.*\n(.*)',text)
    return {
        'age':int(age),
        'name':full_name.strip(),
        'birth_date':birth_date.strip(),
        'birth_place':birth_place.strip()}
extract_personal_information(text)


############################################################
text='''Born  Mukesh Dhirubhai Ambani
19 April 1957 (age 66)
Aden, Colony of Aden
(present-day Yemen)[1][2]
Nationality	Indian
Alma mater	
St. Xavier's College, Mumbai
Institute of Chemical Technology (B.E.)
Occupation(s)	Chairman and MD, Reliance Industries
Spouse	Nita Ambani ​(m. 1985)​[3]
Children	3
Parents	
Dhirubhai Ambani (father)
Kokilaben Ambani (mother)
Relatives	Anil Ambani (brother)
Tina Ambani (sister-in-law)'''

def get_pattern_match(pattern,text):
    matches=re.findall(pattern,text)
    if matches:
        return matches[0]

get_pattern_match(r'age (\d+)',text)
get_pattern_match(r'Born(.*)\n',text).strip()
get_pattern_match(r'Born.*\n(.*)\(age',text).strip()
get_pattern_match(r'\(age.*\n(.*)',text)


###########################################################
def extract_personal_information(text):
    age=get_pattern_match('age (\d+)',text)
    full_name=get_pattern_match('Born(.*)\n',text)
    birth_date=get_pattern_match('Born.*\n(.*)\(age',text)
    birth_place=get_pattern_match('\(age.*\n(.*)',text)
    return {
        'age':int(age),
        'name':full_name.strip(),
        'birth_date':birth_date.strip(),
        'birth_place':birth_place.strip()}
extract_personal_information(text)


