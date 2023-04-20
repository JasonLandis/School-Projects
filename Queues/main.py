import timeit

# used for storing patients in the patient_info.txt
class PatientNode:
        def __init__(self, data):
                self.data = data
                self.next = None

# creates linked list
class LinkedList:
        def __init__(self):
                self.head = None

        # method to search through linked list for specific value 'data'
        def search(self, data):
                node = self.head
                while node.next is not None:
                        if int(node.data[0]) == data:
                                return node.data
                        node = node.next

# used for storing priority information from priority.txt
class PriorityNode:        
        def __init__(self, data, priority):          
                self.data = data
                self.priority = priority
                self.next = None

# creates priority queue                
class PriorityQueue:    
        def __init__(self):             
                self.front = None
        
        # checks if queue is empty 
        def empty(self):
                return True if self.front == None else False

        # algorithm for storing info in order of priority
        def push(self, data, priority):
                if self.empty() == True:              
                        self.front = PriorityNode(data, priority)          
                        return
                        
                else:
                        if self.front.priority < priority:
                                newNode = PriorityNode(data, priority)
                                newNode.next = self.front
                                self.front = newNode
                                return
                                
                        else:
                                tempNode = self.front
                                while tempNode.next:
                                        if priority >= tempNode.next.priority:
                                                break                                        
                                        tempNode = tempNode.next                                
                                newNode = PriorityNode(data, priority)
                                newNode.next = tempNode.next
                                tempNode.next = newNode
                                return

        # method to return front value from queue
        def pop(self):
                if self.empty() == True:
                        return True                
                else:
                        data = self.front
                        self.front = self.front.next
                        return data.data

def main():
        time = []
        time2 = []

        # opens priority.txt and stores it in queue
        priorFile = open('priority.txt')
        queue = PriorityQueue()       
        for x in priorFile:
                key, data = x.split(',')
                try:
                        start = timeit.default_timer()
                        queue.push(data, int(key))
                        time.append(timeit.default_timer() - start)
                except:
                        continue       
        priorFile.close()

        # opens patient_info.txt and stores it in link
        patientFile = open('patient_info.txt')
        link = LinkedList()
        for x in patientFile:
                info = x.strip().split(',')
                value = PatientNode(info)
                if link.head is None:
                        link.head = value
                else:
                        value.next = link.head
                        link.head = value
        patientFile.close()

        # outputs information and times each search algoritm
        count = 20
        while not queue.empty():                
                value = queue.pop()
                start = timeit.default_timer()
                data = link.search(int(value))
                time2.append(timeit.default_timer() - start)
                print(f"Patient ID: {str(value).strip()}\tPriority: {count}")
                print(f"Full Name: {data[1]}")
                print(f"Contact Number: {data[2]}\n")
                print(f"------------------------------------\n")
                count -= 1
        
        # averages time for sort and search and displays result in nanoseconds
        time = sum(time) / len(time)
        time2 = sum(time2) / len(time2)
        result = time * 1000000000
        result2 = time2 * 1000000000
        print(f"Average time for sort: {result} nanoseconds")
        print(f"Average time for search: {result2} nanoseconds\n")

main()