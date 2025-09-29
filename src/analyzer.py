import ast

def analyze_code(file_path):
    with open(file_path, "r") as f:
        tree = ast.parse(f.read(), filename=file_path)

    report = []

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            # Function length
            length = node.body[-1].lineno - node.body[0].lineno + 1
            if length > 10:
                report.append(f"⚠️ Function '{node.name}' is long ({length} lines)")
            
            # Naming convention
            if not node.name.islower():
                report.append(f"⚠️ Function '{node.name}' should be lowercase")

    # Unused imports (basic)
    imports = [n.names[0].name for n in ast.walk(tree) if isinstance(n, ast.Import)]
    report.append(f"ℹ️ Imported modules: {imports}")

    return report
