# copyright Merzlov Nikolay merzlovnik@mail.ru

import sys


class StackMachine:
    def __init__(self, code):
        self.data_stack = []  # main stack for operations
        self.return_stack = []  # instruction numbers for returning back
        self.instruction_pointer = 0  # current instruction number
        self.code = code  # instructions and operands
        self.top_of_stack = None  # top of data stack
        self.heap = {}  # dictionary with variables
        self.instruction_map = {'*': self.mul,
                                '%': self.mod,
                                '+': self.add,
                                '-': self.sub,
                                '/': self.div,
                                '==': self.eq,
                                '>': self.grt,
                                'println': self.println,
                                'print': self.print,
                                'cast_int': self.cast_int,
                                'cast_str': self.cast_str,
                                'drop': self.drop,
                                'dup': self.dup,
                                'if': self.if_clause,
                                'jmp': self.jmp,
                                'stack': self.stack,
                                'swap': self.swap,
                                'read': self.read,
                                'read_int': self.read_int,
                                'call': self.call,
                                'return': self.return_back,
                                'exit': self.exit,
                                'store': self.store,
                                'load': self.load
                                }  # dictionary for commands

    def pop(self):
        return self.data_stack.pop()
        # return self.data_stack[-1]

    def push(self, value):
        self.data_stack.append(value)

    def instruction(self, command):
        # if command is operation
        if command in self.instruction_map:
            self.instruction_map[command]()
        # if command is number
        elif isinstance(command, int) or isinstance(command, float):
            self.push(command)
        # if command is string for something
        elif isinstance(command, str) and command[0] == command[-1] == '"':
            self.push(command[1:-1])  # push without ""
        else:
            raise RuntimeError("Unknown command: '%s'" % command)

    def run(self):
        while self.instruction_pointer < len(self.code):
            command = self.code[self.instruction_pointer]
            self.instruction_pointer += 1
            self.instruction(command)
            if len(self.data_stack) > 0:
                self.top_of_stack = self.data_stack[-1]
            else:
                self.top_of_stack = None

    def mul(self):
        self.push(self.pop() * self.pop())

    def mod(self):
        rhs = self.pop()
        self.push(self.pop() % rhs)

    def add(self):
        self.push(self.pop() + self.pop())

    def sub(self):
        rhs = self.pop()
        self.push(self.pop() - rhs)

    def div(self):
        rhs = self.pop()
        self.push(self.pop() / rhs)

    def eq(self):
        self.push(self.pop() == self.pop())

    def grt(self):
        self.push(self.pop() > self.pop())

    def println(self):
        print(self.top_of_stack)

    def print(self):
        print(self.top_of_stack, end=" ")

    def cast_int(self):
        self.push(int(self.pop()))

    def cast_str(self):
        self.push(str(self.pop()))

    def drop(self):
        if len(self.data_stack) > 0:
            self.data_stack.pop()
        else:
            raise RuntimeError("Stack is empty!")

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

    def jmp(self):
        jump_address = self.pop()
        if isinstance(jump_address, int) and 0 <= jump_address < len(self.code):
            self.instruction_pointer = jump_address
        else:
            raise RuntimeError("JMP address must be a valid integer.")

    def stack(self):
        print("Data stack: ", self.data_stack)
        print("Instruction pointer: ", self.instruction_pointer)
        print("Return stack: ", self.return_stack)
        print("Heap: ", self.heap)

    def swap(self):
        top_old = self.top_of_stack
        self.pop()
        top_new = self.data_stack[-1]
        self.pop()
        self.push(top_old)
        self.push(top_new)

    def read(self):
        self.push(input())

    def read_int(self):
        self.push(int(input()))

    def call(self):
        self.return_stack.append(self.instruction_pointer)
        self.jmp()

    def return_back(self):
        self.instruction_pointer = self.return_stack.pop()

    def exit(self):
        sys.exit(0)

    def store(self):
        self.heap.update({self.pop(): self.pop()})

    def load(self):
        self.push(self.heap[self.pop()])
