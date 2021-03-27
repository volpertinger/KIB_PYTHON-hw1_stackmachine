# copyright Merzlov Nikolay merzlovnik@mail.ru

import main

print("--arithmetic--")
main.StackMachine([2, 3, "+", 4, "*", 2, "/", 6, "%", 1, "-", 3, "==", "print", "print", "println"]).run()
print("--cast--")
main.StackMachine([2, "cast_str", "println", 2.3, "cast_int", "println"]).run()
print("--dup, drop--")
main.StackMachine([2, "println", "dup", "+", "println", "drop", "println"]).run()
