class Queue:
    
    def __init__(self, lists = None):
        self.lists = [] if lists == None else lists
    
    def enqueue(self, item):
        self.lists.append(item)
    
    def dequeue(self):
        return self.lists.pop(0) if not self.isEmpty() else -1

    def isEmpty(self):
        return self.lists == []
    
    def size(self):
        return len(self.lists)

    def __str__(self):
        if self.size() > 0:
            return str(self.lists)
        else:
            return 'Empty'