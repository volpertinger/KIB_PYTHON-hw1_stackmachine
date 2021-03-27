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
                         'print': self.print,
                         'cast_int': self.cast_int,
                         'cast_str': self.cast_str,
                         'drop': self.drop,
                         'dup': self.dup,
                         'if': self.if_clause
                         }  # dictionary for commands

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
            if len(self.data_stack) > 0:
                self.top_of_stack = self.data_stack[-1]
            else:
                self.top_of_stack = None

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

    def cast_int(self):
        self.push(int(self.pop()))

    def cast_str(self):
        self.push(str(self.pop()))

    def drop(self):
        self.pop()

    def dup(self):
        self.push(self.top_of_stack)

    def if_clause(self):
        true_clause = self.pop()
        false_clause = self.pop()
        condition_if = self.pop()
        if condition_if:
            self.push(true_clause)
        else:
            self.push(false_clause)
