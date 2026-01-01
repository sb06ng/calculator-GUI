import ast
import operator

import calculator

# Maps AST operator types to actual logic from the calculator module
operators = {
    ast.Add: calculator.addition,
    ast.Sub: calculator.subtraction,
    ast.Mult: calculator.multiplication,
    ast.Div: calculator.division,
    ast.USub: operator.neg,
}

# Maps function names found in strings to calculator methods
functions = {
    'sin': calculator.sine,
    'tan': calculator.tangent,
    'sqrt': calculator.sqrt,
    'log': calculator.log,
    'fac': calculator.factorial,
    'pow': calculator.power
}


def evaluate_node(node):
    """
    Recursively evaluates an AST node.
    """
    # If the node is a literal number (e.g., 42)
    if isinstance(node, ast.Constant):
        return node.value

    # If the node is a binary operation (e.g., x + y)
    elif isinstance(node, ast.BinOp):
        left = evaluate_node(node.left)
        right = evaluate_node(node.right)
        return operators[type(node.op)](left, right)

    # If the node is a unary operation (e.g., -x)
    elif isinstance(node, ast.UnaryOp):
        return operators[type(node.op)](evaluate_node(node.operand))

    # If the node is a function call (e.g., sqrt(16))
    elif isinstance(node, ast.Call):
        func_name = node.func.id
        # Evaluate all arguments inside the function call
        args = [evaluate_node(arg) for arg in node.args]
        return functions[func_name](*args)

    else:
        raise TypeError(f"Unsupported expression node: {node}")


def calculate(equation):
    """
    Parses a string equation and returns the calculated result.

    Args:
        equation: The equation to parse.

    Returns:
        The calculated result.
    """
    # mode="eval" ensures only single expressions are parsed (no loops or assignments)
    tree = ast.parse(equation, mode="eval")
    return evaluate_node(tree.body)
