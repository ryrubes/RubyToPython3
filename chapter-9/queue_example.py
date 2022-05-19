

Document1 = "This is the first document"
Document2 = "This is the second document"
Document3 = "This is the thrid document"

all_documents = [Document1, Document2, Document3]
queueee = []  

def queue():
    for doc in all_documents:
        queueee.append(Document1)
        queueee.append(Document2)
        queueee.append(Document3)

        dequeue = queueee.pop(0)
        dequeue = queueee.pop(0)

        print(queueee)

queue()


    
    
    





