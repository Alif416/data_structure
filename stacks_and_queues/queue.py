# Queque =====>>> FIFO(First In First Out)
#        =====>>>LIFO(Last In Firs Out)

class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self,item):
        self.queue.append(item)
        
    def dequeue(self):
        if len(self.queue) < 1:
            reutrn None
        return self.queue.pop(0)
    
    
