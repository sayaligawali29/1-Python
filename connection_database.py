# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 08:38:07 2023

@author: user
"""

import psycopg2 as pg2
#create a connection with postgresql
#'passord is whatever password u set we set passwars in postgersql

conn=pg2.connect(database='dvdrental',user='postgres',password='root')

#establish connection and start cursor to be ready to query
cur=conn.cursor()

#pass in a postgresql query as a string
cur.execute("SELECT * from payment")

#Return a tuple of first row as python objects
cur.fetchone()

#return N number of rows
cur.fetchmany(10)

#return all rows at once
cur.fetchall()

#to save and index results, assign it to a variable
data=cur.fetchmany(10)
#dont forget to close the connection
#killing the kernal or shutting down jupyter will also close it
conn.close()
conn=pg2.connect(database='Testme',user='postgres',password='root')
cur=conn.cursor()

#Execute a command: create courses table
cur.execute('''create table courses
            (course_id serial primary key,
             course_name varchar(50) unique not null,
             course_instructor varchar (100) not null,
             topic varchar(20) not null)''');
#Make the changes to database persistent
conn.commit()
#Close cursor and the communication with the database
cur.close
#######################################################
