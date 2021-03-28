# copyright Merzlov Nikolay merzlovnik@mail.ru

import StackMachine as SM
import unittest


class TestStackMachine(unittest.TestCase):

    def test_arithmetic(self):
        test_machine = SM.StackMachine(
            [2, 3, "+", 4, "*", 2, "/", 6, "%", 1, "-", 3, "=="])
        test_machine.run()
        self.assertTrue(test_machine.top_of_stack)

    def test_cast(self):
        test_machine = SM.StackMachine([2, "cast_str"])
        test_machine.run()
        self.assertEqual(test_machine.top_of_stack, "2")

        test_machine = SM.StackMachine(['"2"', "cast_int"])
        test_machine.run()
        self.assertEqual(test_machine.top_of_stack, 2)

    def test_drop(self):
        test_machine = SM.StackMachine([1, '"2"', "drop"])
        test_machine.run()
        self.assertEqual(test_machine.top_of_stack, 1)

    def test_dup(self):
        test_machine = SM.StackMachine([1, "dup", "+"])
        test_machine.run()
        self.assertEqual(test_machine.top_of_stack, 2)

    def test_if(self):
        test_machine = SM.StackMachine([1, '"False"', '"True"', "if"])
        test_machine.run()
        self.assertEqual(test_machine.top_of_stack, "True")

        test_machine = SM.StackMachine([0, '"False"', '"True"', "if"])
        test_machine.run()
        self.assertEqual(test_machine.top_of_stack, 'False')

    def test_jump(self):
        test_machine = SM.StackMachine([10, 7, "jmp", 0, "*", 0, "*", 1, "*"])
        test_machine.run()
        self.assertEqual(test_machine.top_of_stack, 10)

    def test_swap(self):
        test_machine = SM.StackMachine([1, 0, "swap", "-"])
        test_machine.run()
        self.assertEqual(test_machine.top_of_stack, -1)

    def test_call_return(self):
        test_machine = SM.StackMachine([4, "jmp", 50, "return", 2, "call", 2, "*"])
        test_machine.run()
        self.assertEqual(test_machine.top_of_stack, 100)

    def test_load_store(self):
        test_machine = SM.StackMachine([1, '"a"', "store", 0, '"a"', "load", "-"])
        test_machine.run()
        self.assertEqual(test_machine.top_of_stack, -1)


if __name__ == '__main__':
    unittest.main()

exit(101)

code = SM.C.compile_file('code.txt')
SM.StackMachine(code).run()
