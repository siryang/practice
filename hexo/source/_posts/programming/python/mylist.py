class LinkNode:
    def __init__(self, value):
        self.value = value;
        self.next = None;

class LinkList:
    def __init__(self, values):
        self.head = None;
        self.last = None;
        for v in values:
            self.append(v);
            
    def append(self, value):
        if (self.head == None):
            self.head = LinkNode(value);
            self.last = self.head;
        else:
            self.last.next = LinkNode(value);
            self.last = self.last.next;

    def travesal(self):
        p = self.head;
        while p != None:
            print(p.value)
            p = p.next;
            pass

def main():
    list = LinkList([1,2,3,4,5]);
    list.append(6);
    list.travesal();

if __name__ == '__main__':
    main()