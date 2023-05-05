class Node(object):
    def __init__(self,data=None):
        self._datavalue = data
        self._nextvalue = None
        self._prevvalue = None

    def check_node(self,node):
        if node.datavalue:
            return True
        else:
            return False


class DoubleLinkedList(object):
    def __init__(self,data):
        self._head = Node(data=data)
    def _search_node(self,data):
        temp_node = self.head
        if data:
            node=Node(data)
            while temp_node.datavalue:
                temp_node=temp_node.addvalue
                if temp_node.datavalue == node.datavalue:
                    print("Node Found:", temp_node)
                    return temp_node
                else:
                    return None
                
        else:
            return None
            
    def _search_index(self, index):
        temp_node = self.head
        for i in range(index):
            temp_node = temp_node.nextvalue
        return temp_node          

    def display(self):
        printing = self._head
        while printing:
            print(printing.datavalue)
            printing = printing.addvalue

    def beg_insert(self, data):
        new_node= Node(data)
        new_node.nextvalue = self.head
        self.head.prevvalue = new_node 
        self.head = new_node

    def end_insert(self, data):
        new_node = Node(data)
        temp_node = self.head
        while temp_node.nextvalue :
            temp_node = temp_node.addvalue
        new_node.prevalue =temp_node
        temp_node.nextvalue = new_node

    def mid_insert(self, data,node):
        new_node = Node(data)
        temp_node = self.head
        while temp_node.nextvalue != node:
            temp_node = temp_node.nextvalue
        temp_node = temp_node.nextvalue
        new_node.nextvalue = temp_node.nextvalue
        new_node.prevvalue = temp_node
        temp_node.nextvalue = new_node

    def index_of(self, data):
        temp_node = self.head
        index = 0 
        isnode = self._search_node(data)
        if isnode:
            while temp_node.datavalue != data:
                index += 1
                temp_node = temp_node._addvalue
            return index 
        else:
            return None






