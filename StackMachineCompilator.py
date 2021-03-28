# copyright Merzlov Nikolay merzlovnik@mail.ru

import tokenize


def make_procedure_map(procedure_code):
    f_new_procedure = True  # for correct dictionary of procedures
    procedure_stack = []
    procedure_name = None
    procedures_map = {}
    for element in procedure_code:
        if element == ':':
            f_new_procedure = True
            procedure_stack = []
            procedure_name = None
            continue
        if f_new_procedure:
            procedure_name = element
            f_new_procedure = False
            continue
        if not element == ";":
            procedure_stack.append(element)
        else:
            procedure_stack.append("return")
            procedures_map.update({procedure_name: procedure_stack})
    return procedures_map


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
    f_address_in_procedure = True  # if procedure is depth by another procedures, implement %address% for calling
    for element in raw_code:
        if element == ":":
            procedure_depth += 1
            procedure_code.append(element)
            f_address_in_procedure = False
            continue
        if element == ";":
            procedure_depth -= 1
            procedure_code.append(element)
            continue
        if procedure_depth:
            if instructions.count(element) == 0 and element.find('"') and f_address_in_procedure:
                procedure_code.append("%address%")
            procedure_code.append(element)
            f_address_in_procedure = True
        else:
            if instructions.count(element) == 0 and element.find('"'):
                main_code.append("%address%")
            main_code.append(element)

    total_length = len(main_code)
    procedure_map = make_procedure_map(procedure_code)

    # change procedure names to address in procedure and main code
    for key_implement in procedure_map:
        for key in procedure_map:
            for i in range(len(procedure_map[key])):
                if key_implement == procedure_map[key][i]:
                    procedure_map[key][i] = "call"
                    procedure_map[key][i - 1] = total_length
        for i in range(len(main_code)):
            if key_implement == main_code[i]:
                main_code[i] = "call"
                main_code[i - 1] = total_length
        total_length += len(procedure_map[key_implement])

    # adding procedures at the end of main code
    for key in procedure_map:
        for value in procedure_map[key]:
            main_code.append(value)
    return main_code
