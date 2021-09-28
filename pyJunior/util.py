from typing import List

PRIVATE = "private"
PUBLIC = "public"
PUBLIC_STATIC = "public static"
PRIVATE_STATIC = "private static"

def tab(n: int, s: str) -> str:
    arr = []
    for line in s.splitlines():
        arr.append((" " * n) + line)
    return "\n".join(arr)

def firstCap(s: str):
    if len(s) > 1:
        return s[0].capitalize() + s[1:]
    return s


def block(title, *code) -> str:
    code = "\n".join(code)
    return f"{title} {{\n{tab(4, code)}\n}}\n"


def jclass(acess, name, extends, implements, *code) -> str:
    impls = []
    if not extends is None:
        impls.append(f"extends {extends}")
    if not implements is None:
        impls.append(f"implements {implements}")
    impls = " ".join(impls)
    return block(f"{acess} class {name} {impls}", *code)

def jmethod(acess, type, name, args, *code) -> str:
    return block(f"{acess} {type} {name}({args})", *code)

def jfield(acess: str, type: str, name: str, assign: str) -> str:
    s = f"{acess} {type} {name}"
    if not assign is None:
        s += f" = {assign}"
    s += ";\n"
    return s

def jparam(type: str, name: str) -> str:
    return "".join([
        jfield(PRIVATE, type, name, None),
        jmethod(PUBLIC, type, f"get{firstCap(name)}", "", f"return this.{name};"),
        jmethod(PUBLIC, "void", f"set{firstCap(name)}", f"{type} {name}", f"this.{name} = {name};"),
    ])

def jconstructor(acess: str, className: str, args: str, *code) -> str:
    return block(f"{acess} {className}({args})", *code)

def jif(condition: str, codeTrue: List[str], elseCode: List[str]=None) -> str:
    end = "\n"
    codeTrue = tab(4, "\n".join(codeTrue))
    if not elseCode is None:
        elseCode = tab(4, "\n".join(elseCode))
    s = f"if ({condition}) {{\n{codeTrue}\n}}"
    if not elseCode is None:
        s += f" else {{\n{elseCode}\n}}"
    return s + "\n"

def jforCount(name: str, start: int, end: int, *code: str) -> str:
    return block(f"for (int {name} = {start}; {name} < {end}; {name}++)", *code)

def jwhile(condition: str, *code) -> str:
    return block(f"while ({condition})", *code)

def jmain(*code):
    return jmethod(PUBLIC_STATIC, "void", "main", "String[] args", *code)

def javaFile(packageName: str, imports: List[str], *code: str):
    imps = []
    for imp in imports:
        imps.append(f"import {imp};")
    imps = "\n".join(imps)
    code = "\n".join(code)
    return f"package {packageName}\n\n{imps}\n\n{code}"