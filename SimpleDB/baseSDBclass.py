try:
    import boto
except:
    print("Boto import failed, google Python Boto, and install the package\n See https://github.com/boto/boto")

class SimpleDB:
    def __init__(self, key1 = "", key2 = ""):
        if key1 == "" and key2 == "":
            keyfile = open('keys.txt')
            key1 = (keyfile.readline()[:-1]).split(' ')[1]
            key2 = (keyfile.readline()[:-1]).split(' ')[1]
            keyfile.close()
        print(key1,key2)
        self.sdb = boto.connect_sdb(key1, key2)
        self.domains = self.sdb.get_all_domains()
        self.activeDomain = self.domains[0]

    def __del__(self):
        pass
