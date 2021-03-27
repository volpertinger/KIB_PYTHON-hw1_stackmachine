# copyright Merzlov Nikolay merzlovnik@mail.ru

import main

print("--arithmetic--")
main.StackMachine([2, 3, "+", 4, "*", 2, "/", 6, "%", 1, "println", "-", 3, "==", "print", "print", "println"]).run()
print("--cast--")
main.StackMachine([2, "cast_str", "println", 2.3, "cast_int", "println"]).run()
print("--dup, drop--")
main.StackMachine([2, "println", "dup", "+", "println", "drop", "println"]).run()
print("--if_clause__")
main.StackMachine([20, 0, 1, "if", "println"]).run()
main.StackMachine([0, 0, 1, "if", "println"]).run()
print("--jump--")
main.StackMachine([2, "jmp", 1, 1, "+", 10, "+", "println"]).run()
main.StackMachine([7, "jmp", 1, 1, "+", 10, "+", "println"]).run()
print("--stack--")
main.StackMachine([2, 3, "+", 4, "*", 2, "/", 6, "%", 1, "-", 3, "==", "stack"]).run()
print("--swap--")
main.StackMachine([2, 3, "swap", "-", "println"]).run()
# print("--read--")
# main.StackMachine(["read", "cast_int", 3, "+", "println"]).run()
print("--call, return--")
main.StackMachine([5, "jmp", '"some_call"', "println", "return", 2, "call", 1, 2, "+", "println"]).run()
