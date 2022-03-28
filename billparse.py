class billparse:    
    billText = ""
    space = 0
    stopgap = 0
    billArr = []
    statusArr = []
    completeBillArr = []
    def __init__(self, billText):
        self.billText = billText
        self.billText = billText[2:] #INCLUSIVE
        self.space = 0
        self.stopgap = 0
        self.billArr = []
        self.statusArr = []
        self.completeBillArr = []
    def parseBills(self):
        for i in range(len(self.billText)):
            self.bill = ""
            self.status = ""
            if self.billText[0:2].decode('ascii') == "LC":
                self.billArr.append(self.billText[0:14])
                self.statusArr.append(self.billText[15:])
                break
            if (self.billText[i] == 32):
                self.space += 1
            if i + 1 < len(self.billText):
                if self.billText[i] >= 48 and self.billText[i] <= 57 and self.billText[i + 1] > 57:
                    if self.space - 1 == len(self.billArr):
                        self.bill = self.billText[self.stopgap:i + 1]
                        if len(self.bill) > 0:
                            self.billArr.append(self.bill)
                            self.stopgap = i + 1
            if i + 3 < len(self.billText):
                if self.billText[i:i+3].decode('ascii') == "/21" and not(self.billText[i + 3] == 59):
                    self.status = self.billText[self.stopgap: i + 3]
                    self.statusArr.append(self.status)
                    self.stopgap = i + 3
            if i == (len(self.billText) - 1):
                self.status = self.billText[self.stopgap: i + 3]
                self.statusArr.append(self.status)
        if len(self.billArr) == 0:
            for i in range(len(self.billText)):
                if i > 0:
                    if self.billText[i] >= 65 and self.billText[i - 1] >= 48 and self.billText[i - 1] <= 57:
                        self.billArr.append(self.billText[0:i])
                        self.statusArr.append(self.billText[i:])
        for self.bill in range(len(self.billArr)):
            self.billObject = {
                'billID' : self.billArr[self.bill],
                'status' : self.statusArr[self.bill]
            }
            self.completeBillArr.append(self.billObject)
    def getBills(self):
        return self.completeBillArr
    def getBillId(self, i):
        return self.completeBillArr[i]['billID'].decode('ascii')
    def getStatus(self, i):
        return self.completeBillArr[i]['status'].decode('ascii')
    def getNumBills(self):
        return len(self.completeBillArr)
