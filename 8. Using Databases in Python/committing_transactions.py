import sqlite3  # should come as a standard package with Python3 

# create a connecton to a database that exists, or if it doesnt, create it 
db = sqlite3.connect("customers.sqlite") 

# if we want to update a row in a table, we need to "commit" the update, otherwise it won't take effect 
update_cursor = db.cursor() 
update_sql = "UPDATE customer_details SET email = 'Mitch_PR@yahoo.com' WHERE name = 'Mitch'"

# you can use `.executescript()` to execute multiple statements separated by ; 
update_cursor.execute(update_sql) 
print("{} rows updated".format(update_cursor.rowcount)) 

# use commit connection property on cursor, to commit the updates 
update_cursor.connection.commit() 

# close cursor 
update_cursor.close() 

db.close() 