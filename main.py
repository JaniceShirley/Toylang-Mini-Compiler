from lexer import tokenize
from parser import Parser
from codegen import generate

code = """
let a = 20
let b = 5
let c = a / b
let d = a - b
let e = a * b

print c
print d
print e
print a + b
"""

# Step 1: Tokenize
tokens = tokenize(code)

# Step 2: Parse
parser = Parser(tokens)
ast = parser.parse()

# Step 3: Generate Python code
python_code = generate(ast)

print("Generated Python Code:\n")
print(python_code)

# Step 4: Run generated code
print("Program Output:")
exec(python_code)