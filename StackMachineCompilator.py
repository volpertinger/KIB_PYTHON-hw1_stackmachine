# copyright Merzlov Nikolay merzlovnik@mail.ru

import tokenize


def compile_file(filename):
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
            if tokval == "\n" or tokval == "', '":
                continue
            if toknum == tokenize.NUMBER and not f_comment:
                raw_code.append(int(tokval))
                continue
            elif not f_comment:
                raw_code.append(tokval)
        f.close()
    procedure_depth = 0  # 0-main, 1,2,3... - for other procedures

    main_code = []
    procedure_code = []

    procedure_depth = 0;
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
            procedure_code.append(element)
        else:
            main_code.append(element)
    print(raw_code)
    print(main_code)
    print(procedure_code)
    return raw_code


compile_file('code.txt')
