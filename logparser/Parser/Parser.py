import re
import sys

emptyField = '-'

# Ordinals in the array from each log's entry

ipCol = 9
userAgentCol = 10
urlReqCol = 5
urlParamsCol = 6
dateCol = 0
timeCol = 1

class Parser:
    def __init__(self, filename):
        self.fileName = filename

    def parseLogFile(self,  pattern):
        self.cleanStuff()
        lines = []
        try:
            if pattern.length() == 0:
                #let's catch every line that does'nt start with #
                pattern = '^[^#]'
            input = open(self.fileName)
            lines = input.readlines()
            input.close()
 
            for line in lines:
                match = re.search(str(pattern),  line,  re.I)
                if match:
                    tokens = line.split(' ')
                    ip = tokens[ipCol]
                    userAgent = tokens[userAgentCol]
                    urlReq = tokens[urlReqCol]
                    if tokens[urlParamsCol] != emptyField:
                        urlReq+='?'+tokens[urlParamsCol]
                    dateTime = tokens[dateCol] + ' ' + tokens[timeCol]
                    logEntry = W3SVCLogEntry(ip, userAgent, urlReq, dateTime)
                    
                    if not self.parsedRecords.has_key(ip):
                        self.parsedRecords[ip] = {}
                        
                    if not self.parsedRecords[ip].has_key(userAgent):
                        self.parsedRecords[ip][userAgent] = []
                    
                    self.parsedRecords[ip][userAgent].append(logEntry)
        except IOError,  exc:
            self.lastError = 'IOError: ' + str(exc)       
        except IndexError,  exc:
            self.lastError = 'IndexError: ' + str(exc)
        except:
            if self.lastError == '':
                self.lastError = 'Unexpected error: ' + str(sys.exc_info()[1])
                print "Unexpected error:", sys.exc_info()[0]
            pass
         

    def cleanStuff(self):
        self.parsedRecords = {}
        self.lastError = ''
        

class W3SVCLogEntry:
    def __init__(self,  ip,  userAgent,  urlReq,  dateTime):
        self.ip = ip
        self.userAgent = userAgent
        self.urlReq = urlReq
        self.dateTime = dateTime
