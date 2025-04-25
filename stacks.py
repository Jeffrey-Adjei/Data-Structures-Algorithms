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
            return self.stack.pop()
                   
    def peek(self):
        print(f"{self.stack[0]} is at the top of your stack!")

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
mystack.push("Jojos Bizzare Adventures")
mystack.push("One Piece")
mystack.pop()
print(mystack.stack())
