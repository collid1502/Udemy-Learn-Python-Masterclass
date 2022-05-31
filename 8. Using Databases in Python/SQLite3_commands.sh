<< comment 
Introduction to using SQLite  


 Details 
---------
Note - SQLite will be installed in Ubuntu (Linux) 

done via:
    sudo apt install sqlite3

This installs the command line shell for sqlite3 
command `sqlite3` boots open Command lin shell
command `.quit` exits the command line shell
comment


# start shell with sqlite3 command 
sqlite3 

# use .help to find different commands & tips etc. 
.help 

# setting option to show column name 
.headers on 

# exit command line shell with 
.quit 

# -----------------------------------------------------------

# We can specify the name of a database on the command line like so (calling this example database `test`):
sqlite3 test.db 

# Note - the database will be stored actually as "one file", which is located here: C:\Users\Dan\test.db  
# have also set up a connection to this database witrhin DBeaver SQL tool 

# create a new table 
create table contacts(name text, phone integer, email text);

# insert some data to the table 
insert into contacts (name, phone, email) values('Dan', 7969809550, 'Dan2collins@hotmail.co.uk');

# check the data with a select statement 
select * from contacts; 

# let's insert some more data 
insert into contacts (name, phone, email) values('Jackie', 7969809667, 'jackie.sams92@hotmail.co.uk'); 

# insert data without all cols present - specifying cols to insert into, avoids errors  
insert into contacts (name, email) values('Mitch', 'mitch_pr@hotmail.co.uk'); 

# update Mitch's email address as it has changed
update contacts set email = 'mitchell_pr.hotmail.co.uk' where name = 'Mitch' ; 

# delete any person with the name Sarah from the table 
delete from conatcts where name = 'Sarah' ; 

# prints tables in db 
.tables 

# print schemas 
.schema 

#--------------------------------------------------------------------------------------------------------
# create another table, a simple design holding customer product info 
create table products(product_id INTEGER PRIMARY_KEY, product_name TEXT NOT NULL);

# insert some data 
insert into products (product_id, product_name) values(1, 'Office Chair');
insert into products (product_id, product_name) values(2, 'Printer');
insert into products (product_id, product_name) values(3, 'Laptop');
insert into products (product_id, product_name) values(4, 'Desktop');

#--------------------------------------------------------------------------------------------------------
# create another table which shows each customer name, with a product id they hold, and the count of how many products they have 
create table customer_products(customer_name TEXT, product_id INTEGER NOT NULL, product_count INTEGER NOT NULL);

# insert some data 
insert into customer_products (customer_name, product_id, product_count)
values
('Dan', 1, 1),
('Dan', 4, 1),
('Mitch', 3, 2),
('Mitch', 1, 1),
('Jackie', 2, 2)
;


# example join 
SELECT 
    a.name, a.phone, a.email, c.product_name, b.product_count
FROM
    contacts as a 
LEFT JOIN 
    customer_products as b 
ON 
a.name = b.customer_name
LEFT JOIN 
    products as c 
ON
b.product_id = c.product_id 
;


# lets take the above example, and create a "view". Call this view `customer_product_volumes` 
CREATE VIEW customer_product_volumes
AS SELECT a.name, c.product_name, b.product_count
FROM
    contacts as a 
LEFT JOIN 
    customer_products as b 
ON 
a.name = b.customer_name
LEFT JOIN 
    products as c 
ON
b.product_id = c.product_id 
;

# --------------------------------------------------------------------------------------
# exit command line 
.quit 

exit