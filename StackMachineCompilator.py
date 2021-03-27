# copyright Merzlov Nikolay merzlovnik@mail.ru

import tokenize


def compile_file(filename):
    instructions = ['*', '%', '+', '-', '/', '==', 'println', 'print', 'cast_int', 'cast_str', 'drop', 'dup', 'if',
                    'jmp', 'stack', 'swap', 'read', 'read_int', 'call', 'return', 'exit', 'store',
                    'load']  # stack for commands
    raw_code = []
    with tokenize.open(filename) as f:
        tokens = tokenize.generate_tokens(f.readline)
        f_comment = False  # for deleting comments from code
        for toknum, tokval, _, _, _ in tokens:
            if tokval == "//":
                f_comment = True
                continue
            if f_comment and tokval == "\n":
                f_comment = False
                continue
            if tokval == "\n" or tokval == "', '" or tokval == "":
                continue
            if toknum == tokenize.NUMBER and not f_comment:
                raw_code.append(int(tokval))
                continue
            elif not f_comment:
                raw_code.append(tokval)
        f.close()
        raw_code.append("exit")  # adding exit - command at the end of code

    main_code = []
    procedure_code = []

    procedure_depth = 0
    for element in raw_code:
        if element == ":":
            procedure_depth += 1
            procedure_code.append(element)
            continue
        if element == ";":
            procedure_depth -= 1
            procedure_code.append(element)
            continue
        if procedure_depth:
            if instructions.count(element) == 0 and element.find('"'):
                procedure_code.append("%address%")
            procedure_code.append(element)
        else:
            if instructions.count(element) == 0 and element.find('"'):
                main_code.append("%address%")
            main_code.append(element)
    # --------------------------
    print(raw_code)
    print(main_code)
    print(procedure_code)
    # -------------------------
    return raw_code


compile_file('code.txt')
