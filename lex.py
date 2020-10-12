import re
from typing import NamedTuple, Iterable


class Token(NamedTuple):
    kind: str
    value: str


def lex(code: str) -> Iterable[Token]:
    """
    Retorna sequência de objetos do tipo token correspondendo à análise léxica
    da string de código fornecida.
    """
    token_specification = [
        ("STRING",  r"\".*\""),
        ("LPAR",    r"\("),
        ("RPAR",    r"\)"),
        ("NUMBER",  r"(\+|\-|)?\d+(\.\d*)?"),
        ("NAME",    r"([a-zA-Z_%\+\-]|\.\.\.)[a-zA-Z_0-9\-\>\?\!]*"),
        ("CHAR",    r"#\\[a-zA-Z]*"),
        ("BOOL",    r"#[t|f]"),
        ("SINGLEQUOTE", r"\'"),
    ]

    #removing comments from code
    code = re.sub(r";;.*", "", code)

    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)

    for mo in re.finditer(tok_regex, code):
        kind = mo.lastgroup
        value = mo.group()
        yield Token(kind, value)

    

    return [Token('INVALIDA', 'valor inválido')]