class Node(object):
    def __init__(self,data=None):
        self._datavalue = data
        self._addvalue = None



class Stack(object):
    def __init__(self,firstnode):
        self.TOS = Node(data=firstnode)
        
    def push(self, data):
        new_node = Node(data)
        new_node.addvalue = self.TOS
        self.TOS = new_node

    def display(self):
        printing = self.TOS
        while printing:
            print(printing.datavalue)
            printing = printing.addvalue
            
    def pop(self):
        pop_value = self.TOS
        self.TOS = self.TOS.addvalue
        return pop_value.datavalue
        
    def _search_node(self,data):
        temp_node = self.TOS
        if temp_node.datavalue == data:
            return temp_node
        if data:
            while temp_node.datavalue:
                temp_node=temp_node.addvalue
                if temp_node.datavalue == data:
                    return temp_node
        return None
        
        
class Queue(object):
    def __init__(self, data):
        self.TOQ = Node(data=data)
        
    def add(self, data):
        new_node = Node(data)
        new_node.addvalue = self.TOQ
        self.TOQ = new_node

    def display(self):
        printing = self.TOS
        while printing:
            print(printing.datavalue)
            printing = printing.addvalue
            
    def get(self):
        get_value = self.TOQ
        while get_value.addvalue:
            prev_value = get_value
            get_value = get_value.addvalue
        prev_value.addvalue = None    
        return get_value.datavalue
        
    def _search_node(self,data):
        temp_node = self.TOQ
        if temp_node.datavalue == data:
            return temp_node
        if data:
            while temp_node.datavalue:
                temp_node=temp_node.addvalue
                if temp_node.datavalue == data:
                    return temp_node
        return None
        
        
    def search(self, data):
        temp_node = self.TOQ
        index = 0 
        isnode = self._search_node(data)
        if isnode:
            while temp_node.datavalue != data:
                index += 1
                temp_node = temp_node._addvalue
            return index 
        else:
            return None    
             
                 
        
                    

