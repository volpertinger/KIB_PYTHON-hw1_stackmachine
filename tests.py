# copyright Merzlov Nikolay merzlovnik@mail.ru

import StackMachine as sm
import StackMachineCompilator as smc
import unittest


class Test(unittest.TestCase):

    def test_bool(self):
        test_machine = sm.StackMachine(
            [2, 3, "and"])
        test_machine.run()
        self.assertTrue(test_machine.top_of_stack)

        test_machine = sm.StackMachine(
            [2, 0, "or"])
        test_machine.run()
        self.assertTrue(test_machine.top_of_stack)

        test_machine = sm.StackMachine(
            [1, 1, "xor"])
        test_machine.run()
        self.assertFalse(test_machine.top_of_stack)

        test_machine = sm.StackMachine(
            [1, "not"])
        test_machine.run()
        self.assertFalse(test_machine.top_of_stack)

    def test_arithmetic(self):
        test_machine = sm.StackMachine(
            [2, 3, "+", 4, "*", 2, "/", 6, "%", 1, "-", 3, "=="])
        test_machine.run()
        self.assertTrue(test_machine.top_of_stack)

        test_machine = sm.StackMachine(
            [2, 3, "+", 4, "*", 2, "/", 6, "%", 1, "-", 5, ">"])
        test_machine.run()
        self.assertTrue(test_machine.top_of_stack)

        test_machine = sm.StackMachine(
            [-2, "abs"])
        test_machine.run()
        self.assertEqual(test_machine.top_of_stack, 2)

        test_machine = sm.StackMachine(
            [2, "negate"])
        test_machine.run()
        self.assertEqual(test_machine.top_of_stack, -2)

    def test_cast(self):
        test_machine = sm.StackMachine([2, "cast_str"])
        test_machine.run()
        self.assertEqual(test_machine.top_of_stack, "2")

        test_machine = sm.StackMachine(['"2"', "cast_int"])
        test_machine.run()
        self.assertEqual(test_machine.top_of_stack, 2)

    def test_drop(self):
        test_machine = sm.StackMachine([1, '"2"', "drop"])
        test_machine.run()
        self.assertEqual(test_machine.top_of_stack, 1)

    def test_dup(self):
        test_machine = sm.StackMachine([1, "dup", "+"])
        test_machine.run()
        self.assertEqual(test_machine.top_of_stack, 2)

    def test_if(self):
        test_machine = sm.StackMachine([1, '"False"', '"True"', "if"])
        test_machine.run()
        self.assertEqual(test_machine.top_of_stack, "True")

        test_machine = sm.StackMachine([0, '"False"', '"True"', "if"])
        test_machine.run()
        self.assertEqual(test_machine.top_of_stack, 'False')

    def test_jump(self):
        test_machine = sm.StackMachine([10, 7, "jmp", 0, "*", 0, "*", 1, "*"])
        test_machine.run()
        self.assertEqual(test_machine.top_of_stack, 10)

    def test_swap(self):
        test_machine = sm.StackMachine([1, 0, "swap", "-"])
        test_machine.run()
        self.assertEqual(test_machine.top_of_stack, -1)

    def test_call_return(self):
        test_machine = sm.StackMachine([4, "jmp", 50, "return", 2, "call", 2, "*"])
        test_machine.run()
        self.assertEqual(test_machine.top_of_stack, 100)

    def test_load_store(self):
        test_machine = sm.StackMachine([1, '"a"', "store", 0, '"a"', "load", "-"])
        test_machine.run()
        self.assertEqual(test_machine.top_of_stack, -1)

    def test_compilation(self):
        self.assertEqual(
            ['"Give me $a"', 41, 'call', '"a"', 'store', '"Give me $b"', 41, 'call', '"b"', 'store', '"Give me $c"', 41,
             'call',
             '"c"', 'store', '"Give me $x"', 41, 'call', '"x"', 'store', '"a"', 'load', '"x"', 'load', '*', '"b"',
             'load', '+',
             '"x"', 'load', '*', '"c"', 'load', '+', 'dup', 'println', 'stack', 'exit', 'dup', '*', 'return', 'print',
             'read',
             'cast_int', 'return'], smc.compile_file('example_code.txt')
        )


if __name__ == '__main__':
    unittest.main()
