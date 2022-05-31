import sqlite3  # should come as a standard package with Python3 

# create a connecton to a database that exists, or if it doesnt, create it 
db = sqlite3.connect("customers.sqlite") 

update_cursor = db.cursor() 

#--------------------------------------------------------------------------------------
"""
SQL injection is where, when we attempt to parametrise queries, someone could pass extra statements into the paramter to cause unwatned behaviour, 
like so:

    email = 'Mitch_PR@Yahoo.com; drop table customer_details'

which could drop our table from the application (permissions pending)
"""

email = 'Mitch_PR@Yahoo.com'
name = 'Mitch' 
update_sql = "UPDATE customer_details SET email = '{}' WHERE name = '{}'".format(email, name) 


"""
Luckily the SQLite python module has a protection against this, provided we dont do string interpolation like above, 
and instead do placeholders. This is because the placeholders are scanned at runtime for "extra statements" attempting to be 
executed etc. 
like so: 
"""

update_sql = "UPDATE customer_details SET email = ? WHERE name = ?"   # by using the ? placeholder, we sub in value safely 

new_email = 'Mitch_PR@Yahoo.com'
name = 'Micth' 
update_cursor.execute(update_sql, (new_email, name)) 

#--------------------------------------------------------------------------------------

print("{} rows updated".format(update_cursor.rowcount)) 

# use commit connection property on cursor, to commit the updates 
update_cursor.connection.commit() 

# close cursor 
update_cursor.close() 

db.close() 




