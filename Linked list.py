
class Node(object):
    def __init__(self,data=None):
        self._datavalue = data
        self._addvalue = None

    def check_node(self,node):
        if node.datavalue:
            return True
        else:
            return False


class SingleLinkedList(object):
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
        new_node.addvalue = self.head 
        self.head = new_node

    def end_insert(self, data):
        new_node = Node(data)
        temp_node = self.head
        while temp_node.addvalue :
            temp_node = temp_node.addvalue
        temp_node.addvalue = new_node

    def mid_insert(self, data,node):
        new_node = Node(data)
        temp_node = self.head
        while temp_node.addvalue != node:
            temp_node = temp_node.addvalue
        temp_node = temp_node.addvalue
        new_node.addvalue = temp_node.addvalue
        temp_node.addvalue = new_node

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

    def insert_at(self, data , index):
        temp_node = self.head
        counter = 0 
        while counter != index - 1:
            counter += 1
            temp_node = temp_node.addvalue 
        self.mid_insert(data , temp_node)

    def delete(self, data):
        if not self.index_of(data):
            self.head = self.head.addvalue 

        else:
            target_node = self._search_node(data)
            prev_node_index = self.index_of(data) - 1
            prev_node = self._search_index(prev_node_index)
            prev_node.addvalue = target_node.addvalue
            target_node.addvalue = None
    def update_index(self, index , data):
        update_node = self._search_node(index)
        update_node.datavalue = data

    def update_data(self,old_data,new_data):
        update_node = self._search_node(old_data)
        update_node.datavalue = new_data



       




