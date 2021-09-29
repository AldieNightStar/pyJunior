# pyJunior - Java Code Generator in Python

# Install
```sh
pip install git+https://github.com/AldieNightStar/pyJunior.git
```

# Usage
```py
jclass(access, name, extends, implements, *code)
jfield(acess, type, name, assign)
jparam(type, name)
jmethod(acess, type, name, args, *code)
jmain(*code)
```

# Sample
* More samples in `samples` folder
* Run sample with command `./sample.sh javaFile`
```py
from pyJunior import *

className = "Profile"

# First class (Main)
class1 = jclass(PUBLIC, className, None, None,
        jconstructor(PUBLIC, className, "int age", "this.age = age;"),
        jparam("int", "age"),
        jmethod(PUBLIC, "void", "countAge", "",
            jforCount("i", "0", "this.age",
                "System.out.println(i);",
                jif("i % 2 == 0", [
                    "System.out.println(\"Is odd\");"
                ])
            )
        ),
        jfield(PUBLIC, "String", "note", "\"Just a simple note\""),
        jmain(
            f"{className} obj = new {className}(1);",
            f"obj.setAge(18);",
            f"obj.countAge();",
        )
    )

# Second class
class2 = jclass("", className+"2", className, None, jconstructor(PUBLIC, className+"2", "", "super(18);"))

# Print to the screen
print(
    javaFile("some.package", ["java.util.Map"], class1, class2)
)
```
