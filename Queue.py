class Queue:
    def __init__(self):
        #Stack one
        self.stack1 = []
        self.stack2 = []
        # Dequeue or remove items from the queue

    def deQueue(self):

        # if first stack is empty
        if len(self.stack1) == 0:
            print("Q is Empty")

        # Return top of self.s1
        x = self.stack1[-1]
        self.stack1.pop()
        return x
    #Enqueue means adding the elements into the queue
    def enQueue(self, item):

        # pop elements from one stack to stack2
        while len(self.stack1) != 0:
            self.stack2.append(self.stack1[-1])
            self.stack1.pop()

        # Push item into self stack 1
        self.stack1.append(item)

        # Push the elements back into stack 1
        while len(self.stack2) != 0:
            self.stack1.append(self.stack2[-1])
            self.stack2.pop()



# Driver code
if __name__ == '__main__':
    queue = Queue()
    #Insert the elements
    queue.enQueue(0)
    queue.enQueue(10)
    queue.enQueue(10)
    #Delete the elements or dequeue while printing them out.
    print(queue.deQueue())
    print(queue.deQueue())
    print(queue.deQueue())