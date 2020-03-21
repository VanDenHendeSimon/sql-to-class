During my Data Management course at Howest University, we learned the ins and outs of the Data Manupilation Language. Translated: CRUD. Translated: Create Read Update Delete.

However, to access your database, and be able to execute these queries from your serivce (like a website), an exact replica of each database table had to be created. The emphasis here lies on exact. The main 3 parameters are:  
    - Datatype  
    - Limits  
    - Where are nulls allowed?  

This sounds very straight forward, but we have to keep in mind that datatypes in MySQL are not exact matches of datatypes in Python.

Take for instance CHAR (50), or VARCHAR (50), or DECIMAL (8,2), or tinyint, smallint, mediumint, … The list goes on. These have to be processed and validated carefully in the setter function of each property, which mirrors one column of one table.
