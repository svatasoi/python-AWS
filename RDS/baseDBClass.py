import MySQLdb

class mydbClass:
    def __init__(self, _host, _username, _password, _dbname):
        self.conn = MySQLdb.connect(host=_host, user=_username, passwd=_password, db=_dbname)
        self.dbname = _dbname
        self.tables = []
        self.table_names = []

        cursor = self.conn.cursor()
        cursor.execute("SHOW TABLES")
        table_names = cursor.fetchall()
        for (table_name,) in table_names:
            print(table_name)
            nt = self.newTable(table_name) 

    def newTable(self, _name):
        """Makes new instance of myTable with table name: _name"""
        if _name not in self.table_names:
            newT = myTable(_name, self)
            if newT.valid == False:
                print("Table DNE")
                return 0
            self.table_names.append(_name)
            self.tables.append(newT)
            print("New Table Added")
            return newT
        else:
            print("Table already recognized")
            return 0

    def __del__(self):
        self.conn.close()

#when specifying columns, don't include AUTO_INCREMENT ones
class myTable:
    def __init__(self, _name, _myDB):
        self.valid = True
        testCursor = _myDB.conn.cursor()
        testCursor.execute("SHOW TABLES LIKE '%s'" % _name)
        print("Checking if table is in db...")
        if len(testCursor.fetchall()) == 0:
            print("Table {} not found in the {} DB".format(_name, _myDB.dbname))
            self.valid = False
            return None

        self.conn = _myDB.conn
        self.name = _name
        self.colNames = []

        cursor = self.conn.cursor()

        cursor.execute("SHOW COLUMNS FROM %s WHERE EXTRA not like 'auto_increment'" % self.name)
        self.cols = cursor.fetchall()
        for c in self.cols:
            print(c)
            self.colNames.append(c[0])

        cursor.execute("DESCRIBE %s" % self.name)
        self.description = cursor.fetchall()

    #runs parameter command, a string, with arguments passed as the list 'args'        
    def runCommand(self, command, args = []):
        """
        args: command: SQL command as a string
              args: optional arguments to be put into command
        return: success/failure
        """
        try:
            cursor = self.conn.cursor()
            cursor.execute(command, args)
            cursor.close()
            self.conn.commit()
            print "Successful Command"
            return 1
        except:
            print "Failed Command"
            return 0

    #inserts the list args in to the table
    def insert(self, *args):
        """
        args: *args: data to insert, in order of columns.
            Run <table name>.describe() to see order
        return: NA
        """
        try:
            args = list(args)
            args = [self.name] + self.colNames + args
            args = tuple(args)
            paren = "(" + "%s, " * (len(self.cols)-1) + "%s)"
            argParen = "(" + "'%s', " * (len(self.cols)-1) + "'%s')"
            sqlCommandTxt = "INSERT INTO %s " + paren + " VALUES " + argParen
            sqlCommandTxt %= args
            print(sqlCommandTxt)
            self.runCommand(sqlCommandTxt)
            print "Successful Insert"
        except:
            print "Failed Insert"

    #returns all data in table  
    def getAllRows(self):
        """
        args: NA
        return: all data in table
        """
        try:
            return self.query("SELECT * FROM %s" % self.name)
        except:
            print "Failed Query"
            return 0

    #runs the query, a string, on the table with optional args list
    def query(self, query, args = []):
        try:
            cursor = self.conn.cursor()
            cursor.execute(query, args)
            print "Successful Query"
            r = cursor.fetchall()
            print "ID  FirstName  LastName    Age"
            print "______________________________"
            for e in r:
                print repr(e[0]).rjust(2), repr(e[1]).rjust(10),repr(e[2]).rjust(10),repr(e[3]).rjust(5)
            return r
        
        except:
            print "Failed Query"
            return 0

    def describe(self):
        for col in self.description:
            print(col)


