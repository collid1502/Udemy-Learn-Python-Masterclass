##########################################
##          Working with Pandas         ##
##########################################

'''
PANDAS is one of the most popular Python packages for Data Manipulation tasks.
It is a very powerful and versatile package which makes data cleaning and wrangling much easier and pleasant.
The Pandas library has a great contribution to the python community and it makes python as one of the top programming language for 
data science and analytics. It has become first choice of data analysts and scientists for data analysis and manipulation.


What is pandas package?

Pandas package has many functions which are the essence for data handling and manipulation. 
In short, it can perform the following tasks for you -

Create a structured data set similar to R's data frame and Excel spreadsheet.
Reading data from various sources such as CSV, TXT, XLSX, SQL database, R etc.
Selecting particular rows or columns from data set
Arranging data in ascending or descending order
Filtering data based on some conditions
Summarizing data by classification variable
Reshape data into wide or long format
Time series analysis
Merging and concatenating two datasets
Iterate over the rows of dataset
Writing or Exporting data in CSV or Excel format

'''

# Important Pandas Functions 

'''
Extract Column Names	          df.columns
Select first 2 rows	              df.iloc[:2]
Select first 2 columns	          df.iloc[:,:2]
Select columns by name	          df.loc[:,["col1","col2"]]
Select random no. of rows	      df.sample(n = 10)
Select fraction of random rows	  df.sample(frac = 0.2)
Rename the variables	          df.rename( )
Selecting a column as index	      df.set_index( )
Removing rows or columns	      df.drop( )
Sorting values	                  df.sort_values( )
Grouping variables	              df.groupby( )
Filtering	                      df.query( )
Finding the missing values	      df.isnull( )
Dropping the missing values	      df.dropna( )
Removing the duplicates	          df.drop_duplicates( )
Creating dummies	              pd.get_dummies( )
Ranking	                          df.rank( )
Cumulative sum	                  df.cumsum( )
Quantiles	                      df.quantile( )
Selecting numeric variables	            df.select_dtypes( )
Concatenating two dataframes	        pd.concat()
Merging on basis of common variable   	pd.merge( )
'''

##############################################################################################


'''
You need to import or load the Pandas library first in order to use it. By "Importing a library", 
it means loading it into the memory and then you can use it. 
Run the following code to import pandas library:
'''

import pandas as pd 
import numpy as np 

'''
The "pd" is an alias or abbreviation which will be used as a shortcut to access or call pandas functions. 
To access the functions from pandas library, you just need to type pd.function instead of  pandas.function 
every time you need to apply it
'''

'''
-----------------------------------------------------------------------------------------------------------------------
'''

## Importing a Dataset 

income = pd.read_csv("C:\\Users\\Dan\\Desktop\\Work\\Python\\Python Projects\\Learning_Python1\\Dummy Data\\income.csv")


## Get Variable Names 
# by using income.columns , you can fetch all the variable names from the data frame 
income.columns 

# we can use the column indexes (which in python, start at zero) to only pull certain names. 
# For example, if we want the first 4 column names, we can do:
income.columns[0:4]   # you state the number you want to start at, then the number AFTER you want to go up to, so for 3, we select 4 etc.


'''
Knowing the Variables Types

you can use the <dataFrameName>.dtypes command to extract the information of types of variables stored in the data frame 
'''
income.dtypes 

'''
In the output printed to the console, object means string or char variables & int64 means numeric variables (without decimal places)

To see the variable type of one variable (for example State) instead of all the variables, you can use:
'''
income['State'].dtypes 

'''
The answer returned is dtype('O') - 'O' refers to object aka the type of variable 
'''
##########################################################################################################################

'''
Changing Data Types

Y2008 is an integer. Suppose we want to convert it to a float (numeric var with decimals). We can do:
'''
income.Y2008 = income.Y2008.astype(float) 
income.dtypes 
'''
Results now show Y2008 as float64 
'''
#########################################################################################################################

'''
View the dimensions or "shape" of the data 
'''
income.shape

'''
Output is (51, 16)
51 is the number of rows & 16 is the number of columns 

you can also use shape[0] to see the number of rows (simialr to nrow() in R) and shape[1] for number of columns (similar to ncol() in R) 
'''
income.shape[0]
income.shape[1]

#########################################################################################################################

'''
To view only some of the rows 

by default, head() shows the first 5 rows of data. If we want to see a specific number of rows we can mention it in the parenthesis.
similarly, tail() function shows the last 5 rows by default 
'''
income.head(10) # first 10 rows 
income.tail(10) # last 10 rows 

'''
Alternatively, any of the following could also be used to fetch the first 5 rows, for example
'''
income[0:5]
income.iloc[0:5]

#########################################################################################################################

'''
Define Categorical variables

like factors() in R, we can include categorical variables in Python using "category" dtype 
'''
s = pd.Series([1,2,3,1,2], dtype="category") 
s   # Prints Dataset to Console 

#########################################################################################################################

'''
Extract Unique / Distinct Values 

The unique() function shows the unique levels or categories in a dataset 
'''
income.Index.unique() 

# The nunique() shows the number of unique values 
income.Index.nunique()   # prints 19 - as there are 19 unique Index fields within Income file 

#########################################################################################################################

'''
Generate a Cross Tab 

pd.crosstab() is used to create a bivariate frequency dist. 
Here the bivariate freq distribution is between "Index" and "State" columns
'''
pd.crosstab(income.Index, income.State) 

#########################################################################################################################

'''
Creating a Frequency Distribution 

income.Index selects the "Index" column of the dataset and value_counts() creates a frequency distribution. 
By default ascending=False >>> i.e. it will show the 'Index' which has the Max Frequency at the Top row 
'''
income.Index.value_counts(ascending=False) 

#########################################################################################################################

'''
Drawing Samples

income.sample() is used to draw a random sample from the dataset containing all the columns.
Here, n=5 depicts we need 5 columns and frac=0.1 tells Python that we need 10% of the data as a sample 
'''
income.sample(n=5) 
income.sample(frac=0.1) 


#########################################################################################################################

'''
Selecting only a few columns/variables 

There are multiple ways you can select a particular column/variable. Bothe the following lines of code select "State" from the 
income data frame 
'''
income["State"] 
income.State 

## To select multiple columns by name, you can use 
income[["Index","State","Y2008"]]   # etc etc

## To select only specific columns and rows, we use either loc[] or iloc[] functions.
## The index or columns passed to the function to be selected, are passed as lists.
## "Index":"Y2008" denotes that all the columns from Index to Y2008 (within the dataset) are to be selected 

## SYNTAX =>   df.loc[row_index, column_index] 

# Examples
income.loc[:,["Index","State","Y2008"]] 

income.loc[0:2, ["Index","State","Y2008"]]   # This selects rows with Index label 0 to 2 & then columns stated 

income.loc[:, "Index":"Y2008"]   # Selects consecutive columns between those specified - so you'll see Y2006, Y2007 etc 

#########################################################################################################################

'''
Difference between loc & iloc 

loc considers rows (or columns) with particular labels from the index. 
Whereas iloc considers rows (or columns) at particular positions in the index  

loc is label based, which means you have to specify rows & columns based on their labels
iloc is integer index based, so you have to specify rows & columns by their integer index 
'''

# Create a dummy data frame 
x = pd.DataFrame({"var1" : np.arange(1,20,2)}, index=[9,8,7,6,10,1,2,3,4,5]) 
x 

# so, using loc 
x.loc[:3]    # This prints each rows up until index 3 is reached. In the x dataset, only index 4 & 5 exist after 3, so they are left out

# Using iloc 
 x.iloc[:3]   # prints the first 3 rows (according to index) 

#########################################################################################################################

'''
Renaming Variables 


'''












