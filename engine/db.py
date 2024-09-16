import csv
from genericpath import isfile
import sqlite3

con = sqlite3.connect("jarvis.db")
cursor = con.cursor()

# note:- We comment previous commands , to stop unwanted copies

#System commands ----------------------------------->
query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
cursor.execute(query)  

# #Onenote command
# query = "INSERT INTO sys_command VALUES (null,'one note', 'C:\\Program Files\\Microsoft Office\\root\\Office16\\ONENOTE.EXE')"
# cursor.execute(query)
# con.commit()


#Web Commands ------------------------------------->

query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), url VARCHAR(1000))"
cursor.execute(query)

#Canva command
# query = "INSERT INTO web_command VALUES (null,'canva', 'https://www.canva.com/en_in/')"
# cursor.execute(query)
# con.commit()

#Youtube command
# query = "INSERT INTO web_command VALUES (null,'youtube', 'https://www.youtube.com/')"
# cursor.execute(query)
# con.commit()


# testing module --------------------------------->
# app_name = "android studio"
# cursor.execute('SELECT path FROM sys_command WHERE name IN (?)', (app_name,))
# results = cursor.fetchall()
# print(results[0][0])


#Import contacts using google csv file -------------------------------->
# Create a table with the desired columns 
# cursor.execute('''CREATE TABLE IF NOT EXISTS contacts (id integer primary key, name VARCHAR(200), mobile_no VARCHAR(255), email VARCHAR(255) NULL)''')


# Specify the column indices you want to import (0-based index)
# Example: Importing the 1st and 3rd columns
# desired_columns_indices = [0, 18]

# # # Read data from CSV and insert into SQLite table for the desired columns
# with open('contacts.csv', 'r', encoding='utf-8') as csvfile:
#     csvreader = csv.reader(csvfile)
#     for row in csvreader:
#         selected_data = [row[i] for i in desired_columns_indices]
#         cursor.execute(''' INSERT INTO contacts (id, 'name', 'mobile_no') VALUES (null, ?, ?);''', tuple(selected_data))

# # Commit changes and close connection
# con.commit()
# con.close()


# Insert single contact  ---->
# query = "INSERT INTO contacts VALUES (null,'xyz', '1000000000', 'null')"
# cursor.execute(query)
# con.commit()


# To fetch  mobile no. from database ---> 
# query = 'buddy'
# query = query.strip().lower()

# cursor.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", ('%' + query + '%', query + '%'))
# results = cursor.fetchall()
# print(results[0][0])

