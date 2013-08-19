import os, sys, getopt

def addComplexItem(itemName, keys, values):
    assert len(keys) == len(values)

    from baseSDBclass import SimpleDB
    sdb = SimpleDB()
    domain = sdb.activeDomain
    
    newItem = domain.new_item(itemName)
    for i in range(len(keys)):
        newItem[keys[i]] = values[i] 
    newItem.save()
    
    print("Succesfully Added " + itemName)

def getArgs(argv):
    itemName = ''
    keys = []
    values = []
    try:
        opts, args = getopt.getopt(argv,"hn:k:v:",["keys=","values="])
    except getopt.GetoptError:
        print 'addItem.py -n <item name> --keys=[key array] --values=[value array]  | no spaces please'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'addItem.py -n <item name> --keys=[key array] --values=[value array]  | no spaces please'
            sys.exit()
        elif opt == '-n':
            itemName = arg
        elif opt == "-k":
            keys = arg
        elif opt == "--keys":
            keys = arg[1:len(arg)-1].split(',')
        elif opt == "-v":
            values = arg
        elif opt == "--values":
            values = arg[1:len(arg)-1].split(',')
    return itemName, keys, values

if __name__ == '__main__':
    itemName, keys, values = getArgs(sys.argv[1:])
    print(itemName, keys, values)
    addComplexItem(itemName, keys, values)
