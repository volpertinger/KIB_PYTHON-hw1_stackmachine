# copyright Merzlov Nikolay merzlovnik@mail.ru

import main

main.StackMachine([2, 3, "+", 4, "*", 2, "/", 6, "%", 1, "-", 3, "==", "println", "print", "print"]).run()
main.StackMachine([2, "cast_str", "println", 2.3, "cast_int", "println"]).run()
