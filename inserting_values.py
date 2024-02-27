# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 09:03:50 2023

@author: user
"""

##INSERTTING VALUES IN THE TABLE

import psycopg2 as pg2
conn=pg2.connect(database='Testme',user='postgres' ,password='root')
cur=conn.cursor()

#inserting values
cur.execute("INSERT INTO courses(course_name,course_instructor,topic)values ('Introduction to chatgpt','Sayali','Theory')")
cur.execute("INSERT INTO courses(course_name,course_instructor,topic)values ('Introduction to sql','Shweta','R')")
cur.execute("INSERT INTO courses(course_name,course_instructor,topic)values ('Introduction to python','Gangi','R')")
cur.execute("INSERT INTO courses(course_name,course_instructor,topic)values ('Introduction to NLP','Aniket','Python')")
cur.execute("INSERT INTO courses(course_name,course_instructor,topic)values ('Introduction to DS','Satyam','Theory')")

conn.commit()
cur.close()


######################################################
#Using Postgersql in python (with psycopg2)
import psycopg2 as pg2
#create a connection with postgresql
#password
conn=pg2.connect(database='Testme',user='postgres',password='root')
#Establish connection and start cursor to be ready to qury
curr=conn.cursor()
cur.execute('SELECT * FROM courses;')
rows=cur.fetchall()
conn.commit()
conn.close()
for row in rows:
    print(row)

