import the queue library
fron queue import
import the tine library to use the sleep function
import time
#initialize the variables and the queue
printDocument = " "
printQueueSize = 9
printQueueMaxSize = 7
printQueue Queue(printQueueMaxSize)
#print a message with the size of the queue
def printQueueSizeMessage():
printQueueSize = printQueue.qsize() if printQueueSize == 0:
print ("There are no documents waiting for printing.")
elif printQueueSize == 1:
print ("There is 1 document waiting for printing.")
else:
print ("There are", printQueueSize, documents waiting for printing.
#add a document to print the queue
def addDocument(document):
printQueueSize = printQueue.qsize()
if printQueueSize= printQueueMaxSize: print("!!", document, was not sent to print queue.")
print("The print queue is full.")
print()
return
printQueue.put(document)
time.sleep(0.5) 
print(document, "sent to print queue.")
printQueueSizeMessage()
#print a document from the print queue
def printDocument():
printQueueSize = printQueue.qsize()
if printQueueSize == 0:
print("!! The print queue is empty.")
print()
return
printDocument printQueue.get()
time.sleep(1) # wait one second
print("OK", printDocument," is printed.")
printQueueSizeMessage()
#Start of program
print()
#the main program
#send documents to the print queue for printing
addDocument("Document A")
addDocument("Document B")
addDocument("Document C")
addDocument("Document D")
addDocument("Document E")
addDocument("Document F") addDocument("Document G")
printDocument()
addDocument("Document H")
printDocument()
addDocument("Document I")
printDocument()
addDocument("Document J")
addDocument("Document K")
printDocument()
printDocument()
printDocument nt()
printDocumen ument()
printDocument()
printDocument()
printDocument()
printDocument(