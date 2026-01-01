import ast

import calculator

operators = {
    ast.Add: calculator.addition,
    ast.Sub: calculator.subtraction,
    ast.Mult: calculator.multiplication,
    ast.Div: calculator.division,
}
functions = {
    'sin': calculator.sine,
    'tan': calculator.tangent,
    '√': calculator.sqrt,
    'log': calculator.log,
    'fac': calculator.factorial,
    'pow': calculator.power
}


def evaluate_node(node):
    if isinstance(node, ast.Constant):  # Number
        return node.value
    elif isinstance(node, ast.BinOp):  # <left> <operator> <right>
        return operators[type(node.op)](evaluate_node(node.left), evaluate_node(node.right))
    elif isinstance(node, ast.UnaryOp):  # - <number>
        return operators[type(node.op)](evaluate_node(node.operand))
    elif isinstance(node, ast.Call):  # Functions (scientific)
        func_name = node.func.id
        args = [evaluate_node(arg) for arg in node.args]
        return functions[func_name](*args)
    else:
        raise TypeError(f"Unsupported expression node: {node}")


def calculate(equation):
    tree = ast.parse(equation, mode="eval")
    print(tree.body)
    return evaluate_node(tree.body)
