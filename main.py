# copyright Merzlov Nikolay merzlovnik@mail.ru

import StackMachineCompilator
import StackMachine

a = StackMachineCompilator.compile_file('forthe-program_code.txt')
StackMachine.StackMachine(StackMachineCompilator.compile_file('forthe-program_code.txt')).run()
