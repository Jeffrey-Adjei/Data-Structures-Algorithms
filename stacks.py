# stack = LIFO data structure
# stores objects into a 'vertical tower'

class Stack:
    def __init__(self):
        self.stack = []
       
    def push(self, element):
        self.stack.append(element)
        print(f"You just added {element} to your stack: ", self.stack)

    def pop(self):
        if self.isEmpty():
            return "The stack is empty!"
        else:
            print(f"{self.stack.pop()} has been removed from the top of your stack")
                   
    def peek(self):
        print(f"{self.stack[-1]} is at the top of your stack")

    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    def size(self):
         print(len(self.stack))


mystack = Stack()
mystack.push("Jujutsu Kaisen")
mystack.push("Bleach")
mystack.push("Naruto")
mystack.push("One Piece")
mystack.push("Jojos Bizzare Adventure")
mystack.pop()
mystack.peek()
print(mystack.isEmpty())
mystack.size()
