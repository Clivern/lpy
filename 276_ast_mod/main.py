# 276. ast
#
# ast.parse builds a tree from source. ast.literal_eval evaluates literals safely, unlike
# eval. Walkers rewrite or lint code.
#
# Run: python 276_ast_mod/main.py

import ast
tree = ast.parse("a = 1 + 2")
print(type(tree.body[0]).__name__)
print(ast.literal_eval("[1, {'a': 2}]"))
