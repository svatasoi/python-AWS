def retrieveAll():
    from baseSDBclass import SimpleDB
    sdb = SimpleDB()
    domain = sdb.activeDomain #first domain
    
    q = domain.select("select * from %s" % domain.name)
    i = 1
    for e in q:
        print '{0:2d}: {1:s}: {2:s}'.format(i,repr(e.name),repr(e))
        i += 1

if __name__ == '__main__':
    retrieveAll()
