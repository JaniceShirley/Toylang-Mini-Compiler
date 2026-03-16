def expr_to_python(expr):
    # If expression is just a number or variable (string)
    if isinstance(expr, str):
        return expr

    node_type = expr.__class__.__name__

    if node_type == "AddNode":
        return f"{expr.left} + {expr.right}"
    if node_type == "SubNode":
        return f"{expr.left} - {expr.right}"
    if node_type == "MulNode":
        return f"{expr.left} * {expr.right}"
    if node_type == "DivNode":
        return f"{expr.left} / {expr.right}"

    raise Exception("Unknown expression")


def generate(ast):
    python_code = ""

    for node in ast:
        node_type = node.__class__.__name__

        # Variable assignment
        if node_type == "LetNode":
            value_code = expr_to_python(node.value)
            python_code += f"{node.name} = {value_code}\n"

        # Print statement
        elif node_type == "PrintNode":
            expr_code = expr_to_python(node.expression)
            python_code += f"print({expr_code})\n"

    return python_code