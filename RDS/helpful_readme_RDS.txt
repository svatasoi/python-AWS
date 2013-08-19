RDS via Python
by: Sorin Vatasoiu Jr (sorin.vatasoiu@gmail.com)

Things you need to have before using this python class for AWS RDS:
1. AWS account
2. The Python package MySQLdb
3. Install MySQL Client (somewhat optional, but very useful to get started). It's also cool to see data put in through the Python Driver and see it live on the MySQL client.
4. Setup an RDS DB on AWS from the management console.
5. Note the endpoint, username, password, and DB name of your newly created RDS

Steps for using this class:
6. Open the baseDBClass.py in IDLE
7. Run the script (shortcut is F5)
8. In the Python Shell:

>>> db = mydbClass(<endpoint/host> "my-mysql-db.cvhvigzoraji.us-east-1.rds.amazonaws.com", <username>, <password>, <dbname>)

9. If step (8) worked fine, you can connect to your DB! Now, you should try connecting to via the MySQL Client. In the terminal/command prompt:

$ mysql -u<username> -p<password> -h <endpoint of aws rds>

OR

$ mysql -uusername -ppassword -h my-mysql-db.cvhvigzoraji.us-east-1.rds.amazonaws.com -P 3306

10. In the MySQL Client, after connecting with the above commands, you can run normal SQL commands, like SELECT, INSERT, CREATE TABLE, etc.

11. In the Python shell, type in 'db.' and then press Ctrl-Space (autocompletion) and experiment with the different functions.

12. When you instantiate a new mydbClass object in Python, it finds all the associated tables and autopopulates the column data for each table. 
