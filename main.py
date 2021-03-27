# copyright Merzlov Nikolay merzlovnik@mail.ruS

class StackMachine:
    def __init__(self, code):
        self.data_stack = []  # main stack for operations
        self.return_stack = []  # helping procedures
        self.instruction_pointer = 0  # current instruction number
        self.code = code  # instructions and operands
        self.top_of_stack = None  # top of data stack
        self.heap_map = {'*': self.mul,
                         '%': self.mod,
                         '+': self.add,
                         '-': self.sub,
                         '/': self.div,
                         '==': self.eq,
                         'println': self.println,
                         'print': self.print}  # dictionary for commands

    def pop(self):
        return self.data_stack.pop()

    def push(self, value):
        self.data_stack.append(value)

    def heap(self, command):
        # if command is operation
        if command in self.heap_map:
            self.heap_map[command]()
        # if command is number
        elif isinstance(command, int) or isinstance(command, float):
            self.push(command)
        # if command is word-operation
        elif isinstance(command, str) and command[0] == command[-1] == '"':
            self.push(command[1:-1])
        else:
            raise RuntimeError("Unknown command: '%s'" % command)

    def run(self):
        while self.instruction_pointer < len(self.code):
            command = self.code[self.instruction_pointer]
            self.instruction_pointer += 1
            self.heap(command)
            self.top_of_stack = self.data_stack[-1]

    def mul(self):
        self.push(self.pop() * self.pop())

    def mod(self):
        tmp = self.pop()
        self.push(self.pop() % tmp)

    def add(self):
        self.push(self.pop() + self.pop())

    def sub(self):
        tmp = self.pop()
        self.push(self.pop() - tmp)

    def div(self):
        tmp = self.pop()
        self.push(self.pop() / tmp)

    def eq(self):
        self.push(self.pop() == self.pop())

    def println(self):
        print(self.top_of_stack)

    def print(self):
        print(self.top_of_stack, end=" ")
