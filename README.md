# MySQL Table Mapping To Python Automation

During my Data Management course at Howest University, we learned the ins and outs of the Data Manupilation Language. Translated: CRUD. Translated: Create Read Update Delete.

However, to access your database, and be able to execute these queries from your serivce (like a website), an exact replica of each database table had to be created. The emphasis here lies on exact. The main 3 parameters are:  
    - Datatype  
    - Limits  
    - Where are nulls allowed?  

This sounds very straight forward, but we have to keep in mind that datatypes in MySQL are not exact matches of datatypes in Python.

Take for instance CHAR (50), or VARCHAR (50), or DECIMAL (8,2), or tinyint, smallint, mediumint, … The list goes on. These have to be processed and validated carefully in the setter function of each property, which mirrors one column of one table.    

When your database has a lot of tables, which have a lot of columns, this can rapidly turn into a lot of work. On top of that, there is also a very high risk to commit human-errors. Both of these I thought could be avoided rather easily.  

All of this manual labor is eliminated by this script.  
All of the generated code is included in this repo: ./sql/anyfolder_python
