#inheritance
class teacher:
    def setid(self,id):
        self.id=id
    def getid(self):
        return self.id
    def setname(self,name):
        self.name=name
    def getname(self):
        return self.name
    def setaddress(self,addr):
        self.addr=addr
    def getaddress(self):
        return self.addr
    def setsal(self,sal):
        self.sal=sal
    def getsal(self):
        return self.sal
m=teacher()
m.setsal(2000)
m.setid(100)
m.setname('dataenginner')
m.setaddress('avd 6th floor banyan tree')
print(m.getid() ,m.getaddress(),m.getsal(),m.getname())
