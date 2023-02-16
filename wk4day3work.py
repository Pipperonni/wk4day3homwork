num = [3,1,5,2,4,7,9,6,8]

def sort_decorator(*args):
    def inner(func):
        if len(func) == 1: 
            return func

        mid = len(func) // 2
        left_half = func[:mid]
        right_half = func[mid:]

        inner(left_half)
        inner(right_half)

        i = 0 
        j = 0 
        k = 0 

        while i < len(left_half) and j < len(right_half):
            if left_half[i] > right_half[j]:
                func[k] = right_half[j]
                j += 1
            else:
                func[k] = left_half[i]
                i += 1
            k += 1
        
        while i < len(left_half):
            func[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            func[k] = right_half[j]
            j += 1
            k += 1
        return func
    return inner

@sort_decorator
def take_list(a_list):
    return 

class Node:

    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

class LinkedList:

    def __init__(self, head=None):
        self.head = head
    
    def insert_before(self, value, target_value=None):
        new_node = Node(value)
        if isinstance(value, list):
            for val in value: 
                new_node = Node(val)
                if not target_value:
                    if self.head:
                        new_node.next_node = self.head
                    self.head = new_node
                    
                else:
                    current_node = self.head
                    previous_node = None
                    
                    while current_node:
                        if current_node.value == target_value:
                            previous_node.next_node = new_node
                            new_node.next_node = current_node
                            break
                        
                        previous_node = current_node
                        current_node = current_node.next_node
                    
        elif not target_value:
            if self.head:
                new_node.next_node = self.head
            self.head = new_node
                
        else:
            current_node = self.head
            previous_node = None
            
            while current_node:
                if current_node.value == target_value:
                    previous_node.next_node = new_node
                    new_node.next_node = current_node
                    break
                
                previous_node = current_node
                current_node = current_node.next_node    
        return new_node.value

    def remove(self, value):
        current_node = self.head
        previous_node = None
        
        while current_node:
            if current_node.value == value:
                if not previous_node:
                    self.head = current_node.next_node
                else:    
                    previous_node.next_node = current_node.next_node
                break

            previous_node = current_node
            current_node = current_node.next_node
                

    def sum_num(self):
        current_node = self.head
        sum = 0
        while current_node:
            sum += current_node.value
            current_node = current_node.next_node
        return sum

    def insert_after(self, value, target_value=None):
        new_node = Node(value)
        if isinstance(value, list):
            for val in value: 
                new_node = Node(val)
                if not target_value:
                    if self.head:
                        current_node = self.head
                        
                        while current_node.next_node:
                            current_node = current_node.next_node
                        current_node.next_node = new_node
                    
                    else:
                        self.head = new_node

                else:
                    current_node = self.head
                    
                    while current_node:
                        if current_node.value == target_value:
                            new_node.next_node = current_node.next_node
                            current_node.next_node = new_node
                            
                            break
                        
                        current_node = current_node.next_node
        
        elif not target_value:
            if self.head:
                current_node = self.head
                
                while current_node.next_node:
                    current_node = current_node.next_node
                current_node.next_node = new_node
            
            else:
                self.head = new_node

        else:
            current_node = self.head
            
            while current_node:
                if current_node.value == target_value:
                    new_node.next_node = current_node.next_node
                    current_node.next_node = new_node
                    
                    break
                
                current_node = current_node.next_node

    def contains(self, value):
        
        current_node = self.head

        while current_node:
            if current_node.value == value:
                return True
            current_node = current_node.next_node

        return False

    def print_nodes(self):
        curreent_node = self.head
        while curreent_node:
            print(curreent_node.value, end=" -> ")

            curreent_node = curreent_node.next_node
        
        print("None")

my_list = LinkedList()
my_list.insert_after(take_list(num))
# my_list.insert_before(3,3)
my_list.print_nodes()
