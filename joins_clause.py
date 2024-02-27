# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 09:05:29 2023

@author: user
"""
#GROUP BY
import psycopg2 as pg2
conn=pg2.connect(database='Testme',user='postgres',password='root')
cur=conn.cursor()

#GROUP BY 
cur.execute('SELECT course_instructor,count(*) from courses GROUP BY course_instructor')

#make the chaanges to changes to the database persistent 
conn.commit()
rows=cur.fetchall()
for row in rows:
    print(row)

#ORDER BY
import psycopg2 as pg2
conn=pg2.connect(database='Testme',user='postgres',password='root')
cur=conn.cursor()

#ORDER BY
cur.execute('SELECT * from courses ORDER BY course_instructor')

#make the chaanges to changes to the database persistent 
conn.commit()
rows=cur.fetchall()
for row in rows:
    print(row)
    
###########################################################
############################################################
##INNER JOINING
import psycopg2 as pg2
conn=pg2.connect(database='Testme',user='postgres',password='root')
cur=conn.cursor()

cur.execute('''create table course_admin
            (course_id serial primary key,
             course_duration varchar(50)not null,
             course_fees varchar (100) not null)''');
conn.commit()
cur.execute("INSERT INTO course_admin(course_id,course_duration,course_fees)values (1,'40days','3300')")
cur.execute("INSERT INTO course_admin(course_id,course_duration,course_fees)values (2,'50days','2300')")
cur.execute("INSERT INTO course_admin(course_id,course_duration,course_fees)values (3,'60days','4300')")
cur.execute("INSERT INTO course_admin(course_id,course_duration,course_fees)values (4,'70days','4000')")
conn.commit()
cur.close()
cur.execute('''Select * from courses INNER JOIN course_admin on courses.course_id=course_admin.course_id''')
conn.commit()
rows=cur.fetchall()
for row in rows:
    print(row)
