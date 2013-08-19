import os, sys, getopt

def getItem(name):
    from baseSDBclass import SimpleDB
    sdb = SimpleDB()
    
    #gets from first domain in list
    item = sdb.activeDomain.get_item(name)
    print item
    return item

def getArgs(argv):
    itemName = ''
    try:
        opts, args = getopt.getopt(argv,"hn:")
    except getopt.GetoptError:
        print 'getItem.py -n <item name>'
        sys.exit(2)
    if len(opts) == 0:
        from sdbGetAll import retrieveAll
        print "Getting All Rows..."
        retrieveAll()
        sys.exit()
    for opt, arg in opts:
        if opt == '-h':
            print 'getItem.py -n <item name>'
            sys.exit()
        elif opt == '-n':
            itemName = arg
    return itemName

if __name__ == '__main__':
    itemName = getArgs(sys.argv[1:])
    print(itemName)
    getItem(itemName)
