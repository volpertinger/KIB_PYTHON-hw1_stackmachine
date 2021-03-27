# copyright Merzlov Nikolay merzlovnik@mail.ru

import tokenize


def compile_file(filename):
    code = []
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
                code.append(int(tokval))
                continue
            elif not f_comment:
                code.append(tokval)
    print(code)
    return code


compile_file('code.txt')
