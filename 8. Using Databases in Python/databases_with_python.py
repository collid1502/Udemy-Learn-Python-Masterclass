"""
Introduction to using SQLite within Python 


Similar to what was done in the`.sh` file in the directory, we will now look at the same concepts
but by using Python
"""

import sqlite3  # should come as a standard package with Python3 

# create a connecton to a database that exists, or if it doesnt, create it 
db = sqlite3.connect("customers.sqlite") 

# create a table and insert some values into it 
db.execute("CREATE TABLE IF NOT EXISTS customer_details (name TEXT, phone INTEGER, email TEXT)") 

insert_data = """
INSERT INTO customer_details(name, phone, email) 
VALUES 
('Dan', 7969809550, 'Dan2collins@hotmail.co.uk'),
('Jackie', 7969809667, 'jackie.sams92@hotmail.co.uk'),
('Mitch', 7969809683, 'mitch_pr@hotmail.co.uk')
;
"""
db.execute(insert_data)

#------------------------------------------------------------------------------------
# use a cursor to execute queries 
cursor = db.cursor() 
cursor.execute("SELECT * FROM customer_details") 
for row in cursor:
    print(row) 

cursor.close() 


# we could also use the `fetchall` method to collect all rows from cursor object 
#print(cursor.fetchall()) 

# close db connection 
db.close() 